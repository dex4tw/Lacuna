' Lacuna Installer '
import os, requests, ctypes
windll = ctypes.windll
user32 = windll.user32
lbuild = requests.get('https://raw.githubusercontent.com/dex4tw/Lacuna/main/build').text
user32.MessageBoxW(None, f"Installing the latest build of Lacuna ({lbuild})", "Lacuna", 0)