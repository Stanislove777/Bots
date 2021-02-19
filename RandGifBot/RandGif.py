"""

RandGifBot

author: LSS (@Stanislove777)

"""

import telebot
import re
import json
import requests

# GIPHY Token - https://developers.giphy.com/docs/sdk
# Telegram Token - @BotFather
tokenTG = '1686388345:AAGsD3NsaCMI5oVFgSTK99iokm50jIO7rEI'
tokenGI = 'sB02XyKSLsdP4tgrcQaGY3EJFXjqykH6'
bot = telebot.TeleBot(tokenTG)

# Обработка Комманд
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Hello this is a bot\nI am sending a random GIF\nby the key symbol "₽"')

# Обработка текста сообщения
@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text.lower() == 'hi':
		bot.send_message(message.chat.id, 'Hello, you are awesome')
	elif message.text.lower() == 'bye':
		bot.send_message(message.chat.id, 'Goodbye my friend...')
	# Обработка ключевого слова в сообщении
	elif '₽' in message.text.lower():
		tag = re.findall(r'₽(\w+)', message.text.lower())
		sendGifMsg(tag, message)

# Отправка Гиф
def sendGifMsg(tag, message):
	url = "https://api.giphy.com/v1/gifs/random?api_key=" + tokenGI + "&tag=" + "".join(tag) + "&rating=r"

	r = requests.get(url)
	if r.status_code == 200:
		page = json.loads(r.content)
		bot.send_animation(message.chat.id, page['data']['images']['downsized_large']['url'])
	else:
		bot.send_message(message.chat.id, 'ERROR')
	# Вывод ссылки с файлом гиф в командную строку
	print(page['data']['images']['downsized_large']['url'])

bot.polling()

