import requests

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Foundations of Python Network Programming example search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print(reply)
    print(reply[0]['lat'], reply[0]['lon'])

if __name__ == '__main__':
    geocode('Bajpe, Dakshina Kannada, Karnataka, India')