' Lacuna Launcher '
import os, requests, ctypes
winDLL = ctypes.windll
user32 = winDLL.user32
lacunaBuild = requests.get('https://raw.githubusercontent.com/dex4tw/Lacuna/main/build').text

if not os.path.exists(os.getcwd() + "/base"):
    os.mkdir(os.getcwd() + "/base")
    cbuild = open(os.getcwd() + "/base/build", "w")
    cbuild.close()

if not open(os.getcwd() + "/base/build").read() == lacunaBuild:
    user32.MessageBoxW(None, f"Installing the latest build of Lacuna ({lacunaBuild})", "Lacuna", 0)
    reqLacuna = requests.get("https://raw.githubusercontent.com/dex4tw/Lacuna/main/build/lacuna-c.exe")
    cLacuna = open(f"{os.getcwd()}/base/lacuna-c.exe", "wb")
    cLacuna.write(reqLacuna.content)
    cLacuna.close()
    os.system(f'start "" "{os.getcwd()}/base/lacuna.exe"')
else:
    os.system(f'start "" "{os.getcwd()}/base/lacuna.exe"')