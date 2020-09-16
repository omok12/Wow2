import requests
import json
import gzip
from datetime import datetime


class AhCall:
    def __init__(self):
        pass

    def get_token(self, client_id, client_secret):
        data = {'grant_type': 'client_credentials'}
        r = requests.post('https://us.battle.net/oauth/token', data=data, auth=(client_id, client_secret))
        return r.json()['access_token']

    def api_to_gz(self, connected_realm_id, access_token):
        filename = datetime.now().strftime('%Y%m%d%H')
        r = requests.get(f'https://us.api.blizzard.com/data/wow/connected-realm/{connected_realm_id}/auctions?namespace=dynamic-us&locale=en_US&access_token={access_token}')
        json_data = json.dumps(r.json())
        encoded = json_data.encode('utf-8')
        compressed = gzip.compress(encoded)
        with gzip.open(f'{filename}.gz', 'wb') as f:
            f.write(compressed)

if __name__ == '__main__':
    ah_call = AhCall()
    access_token = ah_call.get_token('41aa51073e5c4ef1a80682f2f4b24cec', 'Vx0dE7jjw7zPoekWjiI3fcNiYkAN6lxb')
    ah_call.api_to_gz('5', access_token)


