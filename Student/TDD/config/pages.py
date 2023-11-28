from requests import get

response = get('https://google.com')
print ('Google', response)
print(response.text)