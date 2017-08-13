# -*- coding: utf-8 -*-
import config
import telebot 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hey, how are you today?')
    
@bot.message_handler(content_types=["text"])
def echo_back(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.polling(none_stop=True)