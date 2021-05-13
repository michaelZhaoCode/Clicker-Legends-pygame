import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"
elif sys.platform == "win64":
    base = "Win64GUI"

executables = [
    cx_Freeze.Executable(
        "main.py",
        base=base,
        icon='pictures/general/icon.ico',
        target_name="Clicker Legends.exe",
    )
]

shortcuts = [
    ("DesktopShortcut",         # Shortcut
     "DesktopFolder",           # Directory_
     "Clicker Legends",                 # Name
     "TARGETDIR",               # Component_
     "[TARGETDIR]Clicker Legends.exe",  # Target
     None,                      # Arguments
     None,                      # Description
     None,                      # Hotkey
     None,                      # Icon
     None,                      # IconIndex
     None,                      # ShowCmd
     'TARGETDIR'                # WkDir
     ),
    ("StartShortcut",         # Shortcut
     "StartMenuFolder",           # Directory_
     "Clicker Legends",                 # Name
     "TARGETDIR",               # Component_
     "[TARGETDIR]Clicker Legends.exe",  # Target
     None,                      # Arguments
     None,                      # Description
     None,                      # Hotkey
     None,                      # Icon
     None,                      # IconIndex
     None,                      # ShowCmd
     'TARGETDIR'                # WkDir
     )
    ]

cx_Freeze.setup(
    name="Clicker Legends",
    version="1.2",
    options={
        'bdist_msi': {
                'data': {
                    "Shortcut": shortcuts
                },
            },
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["pictures/", "saves/", "sounds/"]
        }
    },
    executables=executables
)

# 'includes':['PyQt4.QtCore','PyQt4.QtGui','sqlite3','sys','os'],
# "excludes":[""]
