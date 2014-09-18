import requests

r = requests.get('https://api.instagram.com/v1/tags/festember/media/recent?access_token=234543206.3d00603.f2a81227325e429a8acc11230965a8ba')
print r.json()
