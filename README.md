Smart Personal Assistant (Desktop App)

A Python-based desktop personal assistant powered by Large Language Models (LLM), designed to execute system tasks like adjusting volume and brightness, running applications, and performing web searches — all through natural language.

## 📌 Features

* 🎤 Natural Language Understanding using OpenAI LLM
* 🖥️ Desktop GUI built with Tkinter
* 🔊 Control system volume and screen brightness
* 📸 Take screenshots
* 🌐 Perform Google searches
* 🗂️ Launch Microsoft Word
* 🧠 Custom intent recognition system

---

## 🗂️ Project Structure

```bash
Smart-Personal-Assistant/
│
├── actions.py         # Functions to perform actual desktop actions
├── intents.py         # Intent classification and matching
├── llm.py             # Handles communication with OpenAI GPT API
├── gui.py             # Main GUI app with user interface
├── requirements.txt   # All required Python packages
└── README.md
```

---

## ⚙️ Installation

> ✅ Recommended to run this on a **local machine with GUI (Windows/Linux/Mac)** for full functionality.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Smart-Personal-Assistant.git
cd Smart-Personal-Assistant
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Or directly replace `"your_openai_api_key"` in `llm.py` (not recommended for production).

---

## ▶️ Running the App

```bash
python gui.py
```

A GUI window will open. You can enter commands like:

* `"Increase volume"`
* `"Take a screenshot"`
* `"Search for Python tutorials"`
* `"Open a Word project"`

---

## 💡 Example Commands & Intents

| Example Input                | Detected Intent      | Action                      |
| ---------------------------- | -------------------- | --------------------------- |
| `"Turn up the volume"`       | `raise_volume`       | Raises system volume        |
| `"Make screen brighter"`     | `raise_brightness`   | Increases screen brightness |
| `"Google Python decorators"` | `google_search`      | Opens a search in browser   |
| `"Capture screen"`           | `take_screenshot`    | Takes a screenshot          |
| `"Open Microsoft Word"`      | `start_word_project` | Launches MS Word            |

---

## 🛠️ Dependencies

* `openai`
* `tkinter`
* `pyautogui`
* `keyboard`
* `webbrowser`
* `dotenv`
* `requests`

Install with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Notes

* **GUI actions like volume/brightness/screenshot won't work on remote environments like GitHub Codespaces or Replit.**
* Make sure to run the app on a **local desktop OS**.
* For safety, the assistant limits to predefined actions only — no arbitrary code execution.

---

## 🙌 Contribution

Feel free to fork and improve. Ideas like voice input, task scheduling, or calendar integration are welcome.

---

## 📄 License

MIT License


