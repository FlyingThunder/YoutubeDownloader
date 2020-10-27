import sys
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["sys","youtube_dlc","audioclipextractor","os"],
    "includes": ["Output"] # <-- Include easy_gui
}

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(  name = "Youtube_Download",
        version = "0.1",
        description = "Python 3 Youtube Downloader with PyQt5 and Youtube-dlc",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Main.py", base=base)])