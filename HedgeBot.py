import ccxt
import time
import websocket
import json
import threading


binance_key = 'insert key here'
binance_secret = 'insert secret here'
exchange = ccxt.binance({'apiKey': binance_key, 'secret': binance_secret, 'enableRateLimit': True, 'options': {'defaultType': 'future'}})

symbol = 'ETH/USDT'


TriggerOpenShortOrder = 2400 #Price for Short Order

TriggerStartPrice = TriggerOpenShortOrder + 2 #Threshold between Script Start and Order Price

TriggerCloseShortOrder = TriggerOpenShortOrder + 2

OrderAmount = 10 #Amount in Dollar you want to spend

OrderLeverage = 20 #Leverage



def open_short_stop_limit(symbol, amount, leverage, price, stopPrice):
    # Set the leverage
    exchange.fapiPrivate_post_leverage({'symbol': symbol.replace('/', ''), 'leverage': leverage})
    # Calculate position size based on current price, order amount, and used leverage
    #cur_price = float(exchange.fapiPublic_get_premiumindex({'symbol': symbol.replace('/', '')})['markPrice'])
    cur_price = bidprice
    amt = (amount*leverage) / cur_price
    # Create the order

    # price above -5
    exchange.create_order(symbol=symbol, amount=amt, side='sell', type='STOP', price=price, params={'stopPrice': stopPrice, 'positionSide':'SHORT'})

def close_short_stop_limit(symbol, amount, leverage, price, stopPrice):
    # Set the leverage
    exchange.fapiPrivate_post_leverage({'symbol': symbol.replace('/', ''), 'leverage': leverage})
    # Calculate position size based on current price, order amount, and used leverage
    #cur_price = float(exchange.fapiPublic_get_premiumindex({'symbol': symbol.replace('/', '')})['markPrice'])
    cur_price = bidprice
    amt = (amount*leverage) / cur_price
    # Create the order

    #price + 5 from short order
    exchange.create_order(symbol=symbol, amount=amt, side='buy', type='STOP', price=price, params={'stopPrice': stopPrice, 'positionSide':'SHORT'})


socket = 'wss://fstream.binance.com/ws/ethusdt@bookTicker'
price = None
closeConnection = False
def on_message(ws, message):
    global price
    json_message = json.loads(message)
    price = json_message['b']
    if closeConnection:
        ws.close()


ws = websocket.WebSocketApp(socket, on_message = on_message)
wst = threading.Thread(target=ws.run_forever)
wst.start()

time.sleep(5)

bidprice = float(price)


while True: #loop


    bidprice = float(price)
    print(bidprice)

    while bidprice > TriggerStartPrice:


        bidprice = float(price)
        print(bidprice)


    #opening short

    open_short_stop_limit(symbol, amount=OrderAmount, leverage=OrderLeverage, price=TriggerOpenShortOrder, stopPrice=TriggerOpenShortOrder)



    bidprice = float(price)
    print(bidprice)

    #same price as order price
    while bidprice > TriggerOpenShortOrder:


        bidprice = float(price)
        print(bidprice)

        #closing short

    close_short_stop_limit(symbol, amount=OrderAmount, leverage=OrderLeverage, price=TriggerCloseShortOrder, stopPrice=TriggerCloseShortOrder)

    while bidprice < TriggerCloseShortOrder:


        bidprice = float(price)
        print(bidprice)

    bidprice = float(price)
    print(bidprice)
