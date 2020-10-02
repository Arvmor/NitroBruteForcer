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
proxies = {"http": proxy}
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
            break
        except:
            proxy = choice(proxyIP).strip()
            proxies = {"http": proxy}
            proxyIP.remove(proxy+'\n')
        
    # Validating results
    message = json.loads(response.decode("utf-8"))["message"]
    print(code,message,proxy, end=' \r')
    if message != "Unknown Gift Code" or message == "You are being rate limited.":
        if message == "You are being rate limited.":
            print("Just got limited, Changing PROXY ...")
            proxy = choice(proxyIP).strip()
            proxies = {"http": proxy}
            proxyIP.remove(proxy+'\n')
        else:
            print(url,response)
            exit()
    code = ''