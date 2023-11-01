import requests
from requests.structures import CaseInsensitiveDict

url = "https://huntress.ctf.games/api/v1/containers/"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Accept-Language"] = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
headers["Content-Length"] = "16"
headers["Content-Type"] = "application/json"
headers["Cookie"] = "cf723453-db94-47ba-827d-39aaf0bcc140.l0kVQOuF8VLcd1Mkmz-MZIx4YCU"
headers["Csrf-Token"] = "1efee8cad59279c772c9d5c672e1b086a3325e024831397a50c8fc6c27dd4b5b"
headers["Origin"] = "https://huntress.ctf.games"
headers["Referer"] = "https://huntress.ctf.games/challenges"
headers["Sec-Ch-Ua"] = "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
headers["Sec-Ch-Ua-Mobile"] = "?0"
headers["Sec-Ch-Ua-Platform"] = "Windows"
headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "same-origin"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

data = '{"challenge":70}'

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
