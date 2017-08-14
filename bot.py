# -*- coding: utf-8 -*-
import logging
import config
import telebot 

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hey, how are you today?')
    
@bot.message_handler(content_types=["text"])
def echo_back(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.polling(none_stop=True)