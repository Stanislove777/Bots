import telebot
import config
import connect_db
from pathlib import Path

tokenTG = config.tokens['TOKEN_TG']
bot = telebot.TeleBot(tokenTG)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, 'Type number and get something...')
	pass

@bot.message_handler(content_types=['text'])
def send_message(message):
	name = message.from_user.username
	if message.text.isdigit() and name in config.whitelist:
		sql_query(message.text)

		name_xlsx = message.text + '.xlsx'
		name_csv = message.text + '.csv'

		with open(name_csv, 'rb') as csv:
			bot.send_document(message.chat.id, csv)
			path_csv = Path(name_csv)
			try:
				path_csv.unlink()
			except OSError as e:
				print("Error: %s: %s" % (path_csv, e.strerror))

		with open(name_xlsx, 'rb') as xlsx:
			bot.send_document(message.chat.id, xlsx)
			path_xlsx = Path(name_xlsx)
			try:
				path_xlsx.unlink()
			except OSError as e:
				print("Error: %s: %s" % (path_xlsx, e.strerror))

	elif name not in config.whitelist:
		bot.send_message(message.chat.id, 'ERROR: No authorization')
	else:
		bot.send_message(message.chat.id, 'ERROR: Wrong number')

bot.polling()