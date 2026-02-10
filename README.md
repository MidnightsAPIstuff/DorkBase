# 🚀 DorkBase

**DorkBase** is a high-performance command-line automation tool designed for security researchers and OSINT enthusiasts. It streamlines the process of using **Google Dorks** to identify vulnerabilities, exposed logs, and publicly accessible IoT devices with a single command.



---

## ✨ Features

* **Categorized Intelligence**: Organized dorks for SQL Injection, XSS, sensitive Logs, and IP Cameras.
* **Global Access**: Once installed via setup, run the tool from **any** folder on your computer using the `dorkbase` command.
* **Automatic Browser Integration**: Encodes queries and launches them directly in your default web browser.
* **Custom Search**: Ability to input your own custom dorks directly through the interface.
* **Interactive UI**: Colorful terminal output using `colorama` for better readability.

---

## 🛠️ Installation

### 1. Clone the Repository
git clone https://github.com/YourUsername/DorkBase.git
cd DorkBase

### 2. Run the Setup
Execute the provided batch file to install all necessary Python dependencies (such as `colorama`, `selenium`, and `requests`).
setupOPENFIRST.bat

### 3. Install Globally
To use the `dorkbase` command from any directory, run this command in the project folder:
pip install .

---

## 🎮 Usage

You can launch the tool in **Interactive Mode** or jump directly to a **Category Menu**.

### Interactive Mode
Simply type the command to see the main menu:
dorkbase

### Direct Commands
Jump straight to a specific dork category using arguments:
* **SQL Injection**: dorkbase -sql
* **Exposed Logs**: dorkbase -log
* **IP Cameras/Devices**: dorkbase -ip
* **XSS Vulnerabilities**: dorkbase -xss

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| **main.py** | Entry point handling global commands and the main loop. |
| **config.py** | Contains the database of dorks and visual themes. |
| **search.py** | Logic for URL encoding and browser automation. |
| **setup.py** | Configuration for global system installation. |
| **utils.py** | Helper functions like screen clearing. |

---

## ⚖️ Disclaimer
*This tool is for educational and authorized security testing purposes only. The developer is not responsible for any misuse or damage caused by this program.*

**Developed by MidnightsAPIstuff**.

---
