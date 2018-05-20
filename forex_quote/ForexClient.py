import requests
import json


class ForexClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_uri = 'https://forex.1forge.com/1.0.3/'

    def _get(self, path, params={}):
        payload = {'api_key': self.api_key}
        payload = { **params, **payload }
        response = requests.get(self.base_uri + path, params=payload, timeout=10)
        return json.loads(response.text)
    
    def get_quota(self):
        return self._get('quota')
    
    def get_symbols(self):
        return self._get('symbols')
    
    def is_market_open(self):
        response = self._get('market_status')
        return response['market_is_open']
    
    def convert(self, from_currency, to_currency, quantity):
        return self._get('convert', {'from': from_currency, 'to': to_currency, 'quantity': quantity})
    
    def get_quotes(self, currency_pairs):
        return self._get('quotes', {'pairs': ','.join(currency_pairs)})
