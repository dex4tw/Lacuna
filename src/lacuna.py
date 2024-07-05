"""
Lacuna 'Lacuna Launcher'
"""
import os, requests, ctypes
winDLL = ctypes.windll
user32 = winDLL.user32
lacunaBuild = requests.get('https://raw.githubusercontent.com/dex4tw/Lacuna/main/base/build').text

if not os.path.exists(os.getcwd() + "/base"):
    os.mkdir(os.getcwd() + "/base")
    cBuild = open(os.getcwd() + "/base/build", "w")
    cBuild.close()
if not os.path.exists(os.getcwd() + "/base/build"):
    cBuild = open(os.getcwd() + "/base/build", "w")
    cBuild.close()

if not open(os.getcwd() + "/base/build").read() == lacunaBuild:
    user32.MessageBoxW(None, f"Installing the latest build of Lacuna ({lacunaBuild})", "Lacuna", 0)
    reqLacuna = requests.get("https://github.com/dex4tw/Lacuna/raw/main/base/lacuna-c.exe")
    cLacuna = open(f"{os.getcwd()}/base/lacuna-c.exe", "wb")
    cLacuna.write(reqLacuna.content)
    cLacuna.close()
    cBuild = open(os.getcwd() + "/base/build", "w")
    cBuild.write(lacunaBuild)
    cBuild.close()
    os.system(f'start "" "{os.getcwd()}/base/lacuna-c.exe"')
else:
    if os.path.exists(os.getcwd() + "/base/lacuna-c.exe"):
        os.system(f'start "" "{os.getcwd()}/base/lacuna-c.exe"')
    else:
        user32.MessageBoxW(None, f"There is an issue, please remove your 'base' directory.", "Lacuna", 0)