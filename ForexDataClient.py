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
        self.api_key = api_key
        self.base_uri = 'https://api.1forge.com/'
        self.socket_uri = "wss://sockets.1forge.com/socket"
        self.ws = None
        self.onUpdateFunc = None
        self.onConnectFunc = None
        self.onMessageFunc = None

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

    def onUpdate(self, func):
        self.onUpdateFunc = func

    def onConnect(self, func):
        self.onConnectFunc = func

    def onMessage(self, func):
        self.onMessageFunc = func

    def connect(self):
        self.ws = websocket.WebSocketApp(self.socket_uri,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open()
        self.ws.run_forever()

    def subscribeTo(self, pair):
        if(type(pair) == str):
            self.ws.send("subscribe_to|" + pair)
        else:
            for p in pair:
                self.subscribeTo(p)

    def subscribeToAll(self):
        self.ws.send("subscribe_to_all")

    def unsubscribeFrom(self, pair):
        if(type(pair) == str):
            self.ws.send("unsubscribe_from|" + pair)
        else:
            for p in pair:
                self.unsubscribeFrom(p)

    def unsubscribeFromAll(self):
        self.ws.send("unsubscribe_from_all")

    def on_message(self, message):
        if "post_login_success" in message:
            self.onConnectFunc()
        elif "update" in message:
            msg = message.split("|")
            self.onUpdateFunc(msg[1])
        elif "message" in message:
            msg = message.split("|")
            self.onMessageFunc(msg[1])
        else:
            pass

    def on_error(self, error):
        print(error)

    def on_close(self):
        ws.close()

    def on_open(self):
        def run(*args):
            for i in range(3):
                time.sleep(1)
                self.ws.send("login|" + self.api_key)
            time.sleep(1)
        thread.start_new_thread(run, ())
