'''
    This library is provided without warranty under the MIT license
    Created by Jacob Davis <jacob@1forge.com>
'''

import python_forex_quotes

client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')

# For websocket

if client.marketIsOpen() == True:
    print("Market is open!"
          )
print(client.getSymbols())
print(client.getQuotes(['EURUSD', 'GBPJPY']))
print(client.quota())
print(client.convert('EUR', 'USD', 100))

# For websocket


def onUpdate(value):
    print(value)


def onMessage(value):
    print(value)


def onConnect():
    client.subscribeTo("USD/CHF")
    client.subscribeTo(["EUR/USD", "BTC/USD"])
    client.subscribeToAll()
    client.unsubscribeFrom("USD/CHF")


client.onUpdate(onUpdate)
client.onConnect(onConnect)
client.onMessage(onMessage)
client.connect()
