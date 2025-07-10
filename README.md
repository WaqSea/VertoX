# VertoX 🔒

**VertoX** is an advanced Python-based Discord bot-powered tool. It can create user-specific widgets, send webhooks, and offer some automated functionality. It also operates with a self-cleaning system after installation.

---

## 🚀 Features

- ✅ Creates a keylogger by obtaining the user's Discord token and channel information.
- 🧠 Intelligent token and channel ID verification.
- 🔐 Control via a bot that sends private messages to Discord.
- 🧩 Creates an .exe file with PyInstaller.
- 🧼 Self-cleans `setup.bat` and `requirements.txt` after installation.
- 🎨 Colorful and stylish terminal interface with `colorama`.

---

## 📦 Requirements

- Python 3.10+ (3.13 tested)
- pip (Python package manager)

Required Python packages to install:

```bash
pip install -r requirements.txt
````

---

## ⚙️ Installation

### 🔸 Automatic Installation (recommended)

```bash
Double-click: setup.bat
```

This process:

* Installs required packages (`requirements.txt`)
* Runs the file `mainfiles/setup.py`
* Deletes itself and `requirements.txt` after installation

---

### 🔹 Manual Installation (alternative)

1. Install required dependencies:

```bash
pip install -r requirements.txt
```
2. Run the setup script:

```bash
python mainfiles/setup.py
```

---

## 📁 .env File Example

Create an `.env` file in the project's root folder:

```env
TOKEN=your_discord_bot_token
CHANNEL_ID=123456789012345678
ADMIN_ID=123456789012345678
```

---

## 🔧 Compilation (Keylogger)

After installation, when `main.py` is run, the user is prompted for:

* Discord Token
* Channel ID

and then a hidden `.exe` file is created with PyInstaller.

---

## ⚠️ Warning

> This project is for **educational**, **testing**, and **development** purposes only. Using it on any system without permission may be a crime under the laws of your country.

---

## 👤 Developer

* Made with ❤️ by [WaqSea](https://github.com/WaqSea)

---

## 📜 License

Released under the MIT License. Check the `LICENSE` file for details.

```
