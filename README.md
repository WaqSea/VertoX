<p align="center">
  <img src="https://github.com/user-attachments/assets/5f11f467-377d-4658-b919-48d5ae308b6f" alt="Vertox_github_banner" />
</p>
# VertoX 🔐

**VertoX** is a modular Python-based toolkit for creating advanced Discord-integrated utilities such as keyloggers, token validators, and webhook message automation. It is designed for **developers, security researchers, and automation enthusiasts** who want a customizable setup with minimal overhead and smart cleanup logic.

---

## 📂 Project Structure

```

VertoX/
├── main.py
├── .env
├── requirements.txt
├── setup.bat
├── VertoX.bat
├── setup.py
├── services/
│   ├── gui.py
│   ├── keylogger.py
│   ├── tokenvalidator.py
│   └── webhooksender.py

````

---

## 🚀 Features

- ✅ Simple keylogger generator with PyInstaller integration
- 🔐 Validates Discord tokens and bot credentials
- 🕵️ Sends logs or keystrokes through bot or webhook
- ⚙️ Auto `.exe` builder with token/channel injection
- ♻️ Self-cleaning setup using `setup.bat`
- 📡 Webhook sender utility
- 🖥️ GUI-based setup tools included
- 🧪 All-in-one modular service design

---

## 📦 Requirements

- ![Python](https://img.shields.io/badge/python-3.8%2B-blue)
- pip package manager
- Internet connection for Discord.

### Python packages (auto-installed via `setup.bat`):

- `discord.py`
- `pynput`
- `python-dotenv`
- `colorama`

Install manually (optional):
```bash
pip install -r requirements.txt
````

---

## ⚙️ Setup & Usage

### 🔧 Option 1 — One-click Setup (Recommended)

Simply run:

```bat
setup.bat
```

This will:

1. Install required dependencies via pip
2. Run the Python setup logic (`msetup.py`)
3. Clean itself and remove temporary files after setup

---

### 🔧 Option 2 — Manual Setup

```bash
pip install -r requirements.txt
python setup.py
```

---

## 🧪 .env File Format

> Place a `.env` file in the root directory with the following structure:

```env
TOKEN=your_discord_bot_token
CHANNEL_ID=123456789012345678
ADMIN_ID=987654321098765432
```

---

## 🛠️ Generating the Keylogger EXE

* When user chooses the Keylogger option in `main.py`, they’ll be asked for a Discord Token and Channel ID.
* A Python script is dynamically generated and compiled using PyInstaller.
* The `.exe` is placed next to `main.py`, while `dist/` and `build/` folders are auto-removed.

---

## 🔐 Disclaimer

> This project is **strictly for educational, ethical hacking, and automation testing purposes.**

Any misuse of this tool is the sole responsibility of the user. The developers are **not liable for any illegal or unethical usage.**

---

## 👨‍💻 Developed by

**[WaqSea](https://waqsea.com)**
🔗 *You Can Contact Me at contact@waqsea.com*

## 📜 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
