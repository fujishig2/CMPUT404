import requests

r = requests.get('https://raw.githubusercontent.com/fujishig2/CMPUT404/main/Lab1/getGoogle.py')
print('Status Code:', r, '\n')
print('Headers:', r.headers, '\n')
print('Encoding:', r.encoding, '\n')
print('Text:', '\"' + r.text + '\"')