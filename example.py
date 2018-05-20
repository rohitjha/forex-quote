from forex_quote import ForexClient

API_KEY = ''
CLIENT = ForexClient(API_KEY)

print(CLIENT.get_quota())
print(CLIENT.is_market_open())
print(CLIENT.get_symbols())
print(CLIENT.get_quotes(['USDBTC', 'BTCUSD']))
print(CLIENT.convert('USD', 'BTC', 10000))
