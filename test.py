import requests
response = requests.get('http://grantsautomotiveinc.com')
print(response.history)
for resp in response.history:
    print(resp.status_code, resp.url)

