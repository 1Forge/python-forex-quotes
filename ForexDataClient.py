from __future__ import print_function
import json
import websocket
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
try:
    import thread
except ImportError:
    import _thread as thread
import time


class ForexDataClient:
    def __init__(self, api_key):
        self.isPair = False
        self.test = ""
        self.api_key = api_key
        self.base_uri = 'https://api.1forge.com/'
        self.socket_uri = "wss://sockets.1forge.com/socket"
        '''added'''
        self.ws = None
        # self.sym =

# REST

    def fetch(self, uri):
        response = urlopen(self.base_uri + uri + '&api_key=' + self.api_key)
        return json.load(response)

    def quota(self):
        return self.fetch('quota?cache=false')

    def getSymbols(self):
        return self.fetch('symbols?cache=false')

    def getQuotes(self, pairs):
        [len(i) for i in pairs]
        count = sum(len(i)for i in pairs)
        if (count > 6750):
            return TimeoutError("Error: No more than 963 pairs and 1926 curriencies")
        else:
            return self.fetch('quotes?pairs=' + ','.join(pairs))

    def marketIsOpen(self):
        data = self.fetch('market_status?cache=false')
        try:
            return data['market_is_open']
        except:
            print(data)

    def convert(self, currency_from, currency_to, quantity):
        return self.fetch('convert?from=' + currency_from + '&to=' + currency_to + '&quantity=' + str(quantity))

# SOCKET

    def connect(self):
        self.ws = websocket.WebSocketApp(self.socket_uri,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open()
        self.ws.run_forever()

    def subscribeTo(self, pairs):
        self.sym = pairs
        self.test = "subscribe_to|"
        self.isPair = True

    def subscribeToAll(self):
        self.test = "subscribe_to_all"

    def unsubscribeFrom(self, pairs):
        self.sym = pairs
        self.test = "unsubscribe_from|"
        self.isPair = True

    def unsubscribeFromAll(self):
        self.test = "unsubscribe_from_all"

    def on_message(self, message):

        print("Triggered")
        return 'true'

        # if "post_login_success" in message:
        #     return 'LOGGED IN'
        #     # self.ws.send("subscribe_to|BTC/USD")
        #     # if self.isPair == True:
        #     #     for s in self.sym:
        #     #         self.ws.send(self.test + s)
        #     # else:
        #     #     self.ws.send(self.test)
        #     # print(message)
        # else:
        #     print(message)

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("### closed ###")

    def on_open(self):
        def run(*args):
            for i in range(3):
                time.sleep(1)
                self.ws.send("login|" + self.api_key)
            time.sleep(1)
            # ws.close()
        thread.start_new_thread(run, ())
