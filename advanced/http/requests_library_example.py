# pip install requests
import requests

response1 = requests.get('http://example.com')
# response1 = requests.post('http://example.com')
# response1 = requests.put('http://example.com')
# response1 = requests.delete('http://example.com')
# response1 = requests.head('http://example.com')

for key, value in response1.headers.items():
    print(key, ':', value)