from random import choice
import requests
import json
from time import sleep





# Variables
chracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
code = ''



while True:
    try:
        # Generating Code
        for _ in range(16):
            code += choice(chracters)
        print(code, end=' \r')
        # Request to check the code
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=true&with_subscription_plan=true"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            "X-Fingerprint": "622832459796709396.no-ggtFhW5yweBngUZhaXThqlKk"
        }
        response = requests.request("GET", url, headers=headers).text.encode("utf8")
        message = json.loads(response.decode("utf-8"))["message"]
        if message != "Unknown Gift Code" and message != "You are being rate limited.":
            print(url,response)
            break
        code = ''
    except:
        code = ''
        sleep(2)