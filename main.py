import requests
import json
from datetime import datetime
from sys import settrace, stdout
from os import name, stat,system
from random import choice
from threading import Thread,Lock,active_count
from string import ascii_letters,ascii_lowercase,ascii_uppercase,digits
from time import sleep
from xeger.xeger import Xeger

version = 'v1.0.0'
colors = {'white': "\033[1;37m", 'green': "\033[0;32m", 'red': "\033[0;31m", 'yellow': "\033[1;33m"}

def clear():
    if name == 'posix':
        system('clear')
    elif name in ('ce', 'nt', 'dos'):
        system('cls')
    else:
        print("\n") * 120


def setTitle(title: str):
    if name == 'posix':
        stdout.write(f"\x1b]2;{title}\x07")
    elif name in ('ce', 'nt', 'dos'):
        system(f'title {title}')
    else:
        stdout.write(f"\x1b]2;{title}\x07")


def printText(lock, bracket_color, text_in_bracket_color, text_in_bracket, text):
    lock.acquire()
    stdout.flush()
    text = str(text).encode('ascii', 'replace').decode()
    stdout.write(bracket_color + '[' + text_in_bracket_color + text_in_bracket + bracket_color + '] ' + bracket_color + text + '\n')
    lock.release()


def readJson(filename, method):
    with open(filename, method) as f:
        return json.load(f)


def readFile(filename, method):
    with open(filename, method, encoding='utf8') as f:
        content = [line.strip('\n') for line in f]
        return content


def getRandomProxy(use_proxy, proxy_type):
    proxies_file = readFile('[Data]/proxies.txt', 'r')
    proxies = {}
    if use_proxy == 1:
        proxy = choice(proxies_file)
        if proxy_type == 1:
            proxies = {
                "http": "http://{0}".format(proxy),
                "https": "https://{0}".format(proxy)
            }
        elif proxy_type == 2:
            proxies = {
                "http": "socks4://{0}".format(proxy),
                "https": "socks4://{0}".format(proxy)
            }
        else:
            proxies = {
                "http": "socks5://{0}".format(proxy),
                "https": "socks5://{0}".format(proxy)
            }
    else:
        proxies = {
            "http": None,
            "https": None
        }
    return proxies


def sendWebhook(session, webhook_url, title, message, icon_url, thumbnail_url, proxy, useragent, webhook_retries):
    try:
        timestamp = str(datetime.utcnow())

        message_to_send = {"embeds": [{"title": title, "description": message, "color": 65362,
                                       "author": {"name": "AUTHOR'S DISCORD SERVER [CLICK HERE]",
                                                  "url": "https://discord.gg/9bHfzyCjPQ", "icon_url": icon_url},
                                       "footer": {"text": "MADE BY ONEMANBUILDS", "icon_url": icon_url},
                                       "thumbnail": {"url": thumbnail_url}, "timestamp": timestamp}]}

        headers = {
            'User-Agent': useragent,
            'Pragma': 'no-cache',
            'Accept': '*/*',
            'Content-Type': 'application/json'
        }

        payload = json.dumps(message_to_send)

        response = session.post(webhook_url, data=payload, headers=headers, proxies=proxy)

        if response.text == "":
            pass
        elif "You are being rate limited." in response.text:
            webhook_retries += 1
            sendWebhook(title, message, icon_url, thumbnail_url, proxy, useragent)
        else:
            webhook_retries += 1
            sendWebhook(title, message, icon_url, thumbnail_url, proxy, useragent)
    except Exception:
        webhook_retries += 1
        sendWebhook(title, message, icon_url, thumbnail_url, proxy, useragent)


def getRandomLine(path):
    array = readFile(path,'r')
    return choice(array)

def genName(generate_method, username_case, username_include_digits, username_prefix, username_length, username_suffix,x):
    try:
        if generate_method == 1:
            if username_case == 1:
                if username_include_digits == 1:
                    name = username_prefix + ''.join(choice(ascii_lowercase + digits) for num in range(username_length)) + username_suffix
                else:
                    name = username_prefix + ''.join(choice(ascii_lowercase) for num in range(username_length)) + username_suffix
            elif username_case == 2:
                if username_include_digits == 1:
                    name = username_prefix + ''.join(choice(ascii_uppercase + digits) for num in range(username_length)) + username_suffix
                else:
                    name = username_prefix + ''.join(choice(ascii_uppercase) for num in range(username_length)) + username_suffix
            elif username_case == 3:
                if username_include_digits == 1:
                    name = username_prefix + ''.join(choice(ascii_letters + digits) for num in range(username_length)) + username_suffix
                else:
                    name = username_prefix + ''.join(choice(ascii_letters) for num in range(username_length)) + username_suffix
            elif username_case == 4:
                name = username_prefix + ''.join(choice(digits) for num in range(username_length)) + username_suffix
            else:
                if username_include_digits == 1:
                    name = username_prefix + ''.join(choice(ascii_lowercase + digits) for num in range(username_length)) + username_suffix
                else:
                    name = username_prefix + ''.join(choice(ascii_lowercase) for num in range(username_length)) + username_suffix
            return name
        else:
            name = x.xeger(getRandomLine('[Data]/regex.txt'))
            return name
    except Exception:
        pass

def find_string_between(string, first, last ):
    try:
        start = string.index( first ) + len( first )
        end = string.index( last, start )
        return string[start:end]
    except:
        pass

class Main:
    def __init__(self):
        setTitle(f'[OneManBuilds Minecraft Name Checker] {version}')
        clear()
        self.title = colors['white'] + """
                          ╔═════════════════════════════════════════════════════════════════════╗
                              ╔╦╗╦╔╗╔╔═╗╔═╗╦═╗╔═╗╔═╗╔╦╗  ╔╗╔╔═╗╔╦╗╔═╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
                              ║║║║║║║║╣ ║  ╠╦╝╠═╣╠╣  ║   ║║║╠═╣║║║║╣   ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
                              ╩ ╩╩╝╚╝╚═╝╚═╝╩╚═╩ ╩╚   ╩   ╝╚╝╩ ╩╩ ╩╚═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═
                          ╚═════════════════════════════════════════════════════════════════════╝                                         
        """
        print(self.title)
        self.lock = Lock()
        self.xeger = Xeger()

        self.available = 0
        self.taken = 0
        self.invalid = 0
        self.retries = 0
        self.webhook_retries = 0

        config = readJson('[Data]/configs.json','r')

        self.use_proxy = config['use_proxy']
        self.proxy_type = config['proxy_type']
        self.threads = config['threads']
        self.webhook_enable = config['webhook_enable']
        self.webhook_url = config['webhook_url']
        self.gen_type = config['gen_type']
        self.check_method = config['check_method']
        self.username_case = config['username_case']
        self.username_include_digits = config['username_include_digits']
        self.username_length = config['username_length']
        self.username_prefix = config['username_prefix']
        self.username_suffix = config['username_suffix']

        self.session = requests.Session()

    def titleUpdate(self):
        while True:
            setTitle(f'[OneManBuilds Minecraft Name Checker] {version} ^| AVAILABLES: {self.available} ^| TAKENS: {self.taken} ^| INVALIDS: {self.invalid} ^| RETRIES: {self.retries} ^| WEBHOOK RETRIES: {self.webhook_retries} ^| THREADS: {active_count() - 1}')
            sleep(0.1)

    def worker(self,username):
        try:
            useragent = getRandomLine('[Data]/useragents.txt')

            headers = {
                'User-Agent':useragent
            }

            proxy = getRandomProxy(self.use_proxy,self.proxy_type)

            response = self.session.get(f'https://namemc.com/search?q={username}',headers=headers,proxies=proxy)

            status = find_string_between(response.text,'<meta name="description" content="Status: ',', Searches:')
 
            if status == 'Unavailable':
                self.taken += 1
                printText(self.lock,colors['white'],colors['red'],'TAKEN',username)
                with open('[Data]/[Results]/takens.txt','a',encoding='utf8') as f:
                    f.write(f'{username}\n')
            elif status == 'Available*':
                self.available += 1
                printText(self.lock,colors['white'],colors['green'],'AVAILABLE',username)
                with open('[Data]/[Results]/availables.txt','a',encoding='utf8') as f:
                    f.write(f'{username}\n')
                if self.webhook_enable == 1:
                    sendWebhook(self.session,self.webhook_url,'MC NAME',f'```{username}```','https://media.discordapp.net/attachments/776819723731206164/796935218166497352/onemanbuilds_new_logo_final.png','https://www.minecraft.net/etc.clientlibs/minecraft/clientlibs/main/resources/img/minecraft-creeper-face.jpg',proxy,useragent,self.webhook_retries)
            elif status == 'Too Long':
                self.invalid += 1
                printText(self.lock,colors['white'],colors['red'],'INVALID',username)
                with open('[Data]/[Results]/invalids.txt','a',encoding='utf8') as f:
                    f.write(f'{username}\n')
            else:
                self.retries += 1
                self.worker(username)
        except Exception:
            self.retries += 1
            self.worker(username)

    def start(self):
        Thread(target=self.titleUpdate).start()
        if self.check_method == 1:
            while True:
                if active_count() <= self.threads:
                    username = genName(self.gen_type, self.username_case, self.username_include_digits,self.username_prefix, self.username_length, self.username_suffix, self.xeger)
                    Thread(target=self.worker, args=(username,)).start()
        else:
            usernames = readFile('[Data]/usernames.txt', 'r')
            for username in usernames:
                Run = True
                while Run:
                    if active_count() <= self.threads:
                        Thread(target=self.worker, args=(username,)).start()
                        Run = False

if __name__ == '__main__':
    main = Main()
    main.start()
