import urllib, json


class ForexDataClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_uri = 'http://forex.1forge.com/1.0.3/'  # Reflects v1.0.3 as on the web documentation

    def fetch(self, uri):
        response = urllib.urlopen(self.base_uri + uri + '&api_key=' + self.api_key)
        return json.load(response)

    def quota(self):
        return self.fetch('quota?cache=false')

    def getSymbols(self):
        return self.fetch('symbols?cache=false')

    def getQuotes(self, pairs):
        return self.fetch('quotes?pairs=' + ','.join(pairs))

    def marketIsOpen(self):
        data = self.fetch('market_status?cache=false')
        try:
            return data['market_is_open']
        except:
            print data

    def convert(self, currency_from, currency_to, quantity):
        return self.fetch('convert?from=' + currency_from + '&to=' + currency_to + '&quantity=' + str(quantity))
