import numpy as np
import pandas as pd
from binance.client import Client
import config
import datetime

def return_positions():
	client = Client(config.api_key,config.api_secret)

	client.get_open_orders()

	info = client.get_account()

	traded_coins = list()

	for balance in info['balances']:
	    if float(balance['free']) != 0 :
	        traded_coins.append(balance['asset'])

	current_time = datetime.datetime.now()
	updated_time = current_time - datetime.timedelta(minutes=5)
	updated_time = updated_time.timestamp()

	new_trades = list()

	for traded_coin in traded_coins:
	    coin_name = f'{traded_coin}USDT'
	    if coin_name == "USDTUSDT":
	        continue
	    trades = client.get_my_trades(symbol=f'{traded_coin}USDT')
	    for trade in trades:
	        if (trade['time']/1000 > updated_time):
	            new_trades.append(trade)

	return new_trades
	# for new_trade in new_trades:
	#     print("coin:", new_trade['symbol'])
	#     if new_trade['isBuyer'] == True:
	#         print("BUY")
	#     else:
	#         print("SELL")
	#     print("price:", new_trade['price'])
	#     print("quantity:", new_trade['qty'])
	#     print("position size:", new_trade['quoteQty'])
	#     print("time:",datetime.datetime.fromtimestamp(new_trade['time']/1000.0))
	    

