'''
    This library is provided without warranty under the MIT license
    Created by Jacob Davis <jacob@1forge.com>
'''

import python_forex_quotes

client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')

if client.marketIsOpen() == True:
    print "Market is open!"

print client.getSymbols()
print client.getQuotes(['EURUSD', 'GBPJPY'])
print client.quota()
print client.convert('EUR', 'USD', 100)
