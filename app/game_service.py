from dataclasses import dataclass, field

from app.game_logic import (
    check_bingo,
    generate_board,
    generate_card_deck,
    get_winning_square_ids,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode, GameState


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False
    mode: GameMode = GameMode.BINGO
    deck: list[str] = field(default_factory=list)
    current_card: str | None = None

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.game_state == GameState.BINGO

    @property
    def total_items(self) -> int:
        return len([square for square in self.board if not square.is_free_space])

    @property
    def checked_items(self) -> int:
        return sum(
            1 for square in self.board if square.is_marked and not square.is_free_space
        )

    @property
    def remaining_cards(self) -> int:
        return len(self.deck)

    @property
    def progress_percent(self) -> int:
        if self.total_items == 0:
            return 0
        return int(self.checked_items / self.total_items * 100)

    def start_game(self, mode: GameMode = GameMode.BINGO) -> None:
        self.mode = mode
        self.winning_line = None
        self.show_bingo_modal = False
        self.current_card = None
        if mode == GameMode.CARD_DECK:
            self.board = []
            self.deck = generate_card_deck()
            self.game_state = GameState.PLAYING
            return

        self.board = generate_board()
        self.deck = []
        self.game_state = GameState.PLAYING

    def draw_card(self) -> None:
        if self.mode != GameMode.CARD_DECK or self.game_state != GameState.PLAYING:
            return
        if not self.deck:
            return
        self.current_card = self.deck.pop(0)

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.board = toggle_square(self.board, square_id)

        if self.mode == GameMode.BINGO and self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self.winning_line = bingo
                self.game_state = GameState.BINGO
                self.show_bingo_modal = True

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False
        self.mode = GameMode.BINGO
        self.deck = []
        self.current_card = None

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
