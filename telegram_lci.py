import telebot
import trading_position
import datetime
import passes
import threading
from time import time, sleep


bot = telebot.TeleBot('1829818070:AAE-hOUleoW8yuyvmKeE4ISFVJ7C2dnP7U8')

def trigger_info(message):
	while True:	
		try:
			new_trades = trading_position.return_positions()
			for new_trade in new_trades:
				answer_str = f"coin: {new_trade['symbol']} \n {new_trade['isBuyer']} \n price: {new_trade['price']} \n position_size: {new_trade['quoteQty']} \n time: {datetime.datetime.fromtimestamp(new_trade['time']/1000.0)}"
				bot.send_message(message.from_user.id, answer_str)

			sleep(300)
		except:
			print("something wrong")
		
    
    # threading.Timer(100, trigger_info).start()
	    # print("coin:", new_trade['symbol'])
	    # if new_trade['isBuyer'] == True:
	    #     print("BUY")
	    # else:
	    #     print("SELL")
	    # print("price:", new_trade['price'])
	    # print("quantity:", new_trade['qty'])
	    # print("position size:", new_trade['quoteQty'])
	    # print("time:",datetime.datetime.fromtimestamp(new_trade['time']/1000.0)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

	# @bot.message_handler(content_types=['text', 'document', 'audio'])

	if (message.text == passes.bot_access):
		bot.send_message(message.from_user.id, "Привет!")
	    trigger_info(message)

bot.polling(none_stop=True, interval=0)

