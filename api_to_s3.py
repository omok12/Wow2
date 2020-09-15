import requests

r = requests.get('https://us.api.blizzard.com/data/wow/connected-realm/5/auctions?namespace=dynamic-us&locale=en_US&access_token=US7HcOymVW43TaOzGvctT7AlEJLjcH9NlK')
print(r.json())
