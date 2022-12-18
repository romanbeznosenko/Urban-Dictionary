import telebot
import config
import functions

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id,text = 'Urban Dictionary Bot\nYour search:')


@bot.message_handler()
def welcome(message):
	output = functions.answer(message.text)
	bot.send_message(message.chat.id,text = output, parse_mode = "Markdown")

bot.polling(none_stop=True)
