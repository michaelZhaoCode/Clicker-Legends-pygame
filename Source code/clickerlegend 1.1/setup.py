import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"
elif sys.platform == "win64":
    base = "Win64GUI"

executables = [cx_Freeze.Executable("main.py", base=base, icon='icon.ico', target_name="Clicker Legends.exe")]

cx_Freeze.setup(
    name="Clicker of Legends",
    version="1.2",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["pictures/", "saves/", "sounds/"]
        }
    },
    executables=executables
)

# 'includes':['PyQt4.QtCore','PyQt4.QtGui','sqlite3','sys','os'],
# "excludes":[""]
