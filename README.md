🌐 **Languages:** [Português (BR)](README.pt_BR.md) • [Español](README.es.md)

<div align="center">

# 🎮 Soc Ops

### **Break the Ice, Build the Network**

> A fun, interactive **Social Bingo game** that transforms any in-person mixer into an engaging experience. Find people who match the prompts and get 5 in a row!

[![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue?style=for-the-badge)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.115+-00a651?style=for-the-badge)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

[🚀 Quick Start](#-quick-start) • [📚 Learn](#-learn) • [💡 Features](#-features) • [🤝 Contribute](#-contribute)

</div>

---

## ✨ Features

- **🎯 Interactive Bingo Gameplay** – Server-rendered bingo cards with real-time state management
- **👥 Social Connection** – Designed to help people mingle and network at events
- **⚡ HTMX-Powered** – Smooth, responsive interactions without page reloads
- **🎨 Beautiful UI** – Clean, modern interface built with Jinja2 templates
- **🔧 Extensible** – Easy to customize prompts and game rules
- **🧪 Well-Tested** – Comprehensive test coverage with pytest
- **📱 Session-Based** – Seamless experience across devices with cookie-based sessions

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI + Uvicorn |
| **Templating** | Jinja2 |
| **Interactivity** | HTMX + Vanilla JS |
| **Styling** | Custom CSS utilities |
| **Testing** | pytest |
| **Runtime** | Python 3.13+ |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13 or higher
- `uv` package manager ([install here](https://docs.astral.sh/uv/))

### Installation & Running

```bash
# Clone the repository
git clone https://github.com/21nadhiri/my-soc-ops-python.git
cd my-soc-ops-python

# Install dependencies
uv sync

# Start the development server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open your browser to **`http://localhost:8000`** and start playing!

### Useful Commands

```bash
# Run tests
uv run pytest

# Check code quality
uv run ruff check .

# Format code
uv run ruff format .
```

---

## 📚 Learn & Develop

### 🎓 Guided Lab

Learn how to build social networking features with AI agents. Choose your path:

| Part | Title | Focus |
|------|-------|-------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Checklist | Get started |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering | Configure your environment |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend | Build beautiful UIs |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master | Generate engaging prompts |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development | Orchestrate AI workflows |

> 📝 **Offline Access:** All guides are available in the [`workshop/`](workshop/) directory

---

## 📂 Project Structure

```
my-soc-ops-python/
├── app/
│   ├── main.py                    # FastAPI application
│   ├── game_service.py            # Game session management
│   ├── game_logic.py              # Bingo logic
│   ├── models.py                  # Data models
│   ├── static/                    # CSS & JS
│   └── templates/                 # Jinja2 templates
├── tests/                         # Pytest test suite
├── workshop/                      # Guided learning materials
└── pyproject.toml                 # Project configuration
```

---

## 🎮 How to Play

1. **Start the Game** – Click "Start Game" to begin
2. **Read the Prompts** – Each square contains a fun prompt or question
3. **Find People** – Mingle with others and find people who match the prompts
4. **Mark Your Card** – Click squares when you find matches
5. **Get 5 in a Row** – Win by completing a row, column, or diagonal!

---

## 🤝 Contribute

We love contributions! Whether it's bug fixes, new features, or documentation improvements:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📜 License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

---

## 🙋 Questions & Support

- 📖 Check the [workshop guides](workshop/) for learning materials
- 🐛 Found a bug? Open an [issue](https://github.com/21nadhiri/my-soc-ops-python/issues)
- 💬 Have questions? Start a [discussion](https://github.com/21nadhiri/my-soc-ops-python/discussions)

---

<div align="center">

**Made with ❤️ for bringing people together**

[⬆ Back to top](#-soc-ops)

</div>
