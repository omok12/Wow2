import requests
import json
import gzip
from datetime import datetime

filename = datetime.now().strftime('%Y%m%d%H')

r = requests.get('https://us.api.blizzard.com/data/wow/connected-realm/5/auctions?namespace=dynamic-us&locale=en_US&access_token=US7HcOymVW43TaOzGvctT7AlEJLjcH9NlK')
json_data = json.dumps(r.json())
encoded = json_data.encode('utf-8')
compressed = gzip.compress(encoded)
with gzip.open(f'{filename}.gz', 'wb') as f:
    f.write(compressed)
