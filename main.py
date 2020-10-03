from random import choice
import requests
import json
from time import sleep

# Load proxies
proxyFile = open("proxy.txt", '+r')
proxyIP = proxyFile.readlines()
proxyFile.close()
# Pick proxy
proxy = choice(proxyIP).strip()
proxies = {"socks4": proxy}
proxyIP.remove(proxy+'\n')

# Variables
chracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
code = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    "X-Fingerprint": "622832459796709396.no-ggtFhW5yweBngUZhaXThqlKk"}

while True:
    # Generating Code
    for _ in range(16):
        code += choice(chracters)

    # Request to check the code
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=true&with_subscription_plan=true"
    while True:
        try:
            response = requests.request("GET", url=url, headers=headers, proxies=proxies).text.encode("utf8")
            # Validating results
            print(code,response,proxy, end='\r')
            if "You are being rate limited." in response:
                raise Exception("Just got limited, Changing PROXY ...")
            elif "Unknown Gift Code" in response:
                break
            elif (not "Unknown Gift Code" in response) and (not "You are being rate limited." in response):
                print(url,response)
                exit()
        except:
            proxy = choice(proxyIP).strip()
            proxies = {"http": proxy}
            proxyIP.remove(proxy+'\n')
    code = ''