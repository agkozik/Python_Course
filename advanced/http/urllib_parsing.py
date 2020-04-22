from urllib import request

response = request.urlopen('http://example.com')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
# получаем заголовки в виде всех заголовков
print(response.headers)
# получаем словарь всех загловков
print(response.getheaders())
# получение заголовка
print(response.headers.get('Content-type'))
print(response.getheader('Content-type'))