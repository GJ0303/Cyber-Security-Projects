import requests

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

try:
    response = requests.get("https://check.torproject.org/api/ip", proxies=proxies, timeout=15)

    if response.status_code == 200:
        print(response.json())
    else:
        print("Tor responded, but something went wrong:", response.status_code)

except Exception as e:
    print("Error:", e)
