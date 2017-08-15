# -*- coding: utf-8 -*-
import logging
from config.config import config
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters
import Database 

updater = Updater(token=config["token"])
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def start(bot, update):
    # on start,  save user to database
    user = update.message.from_user
    # save (user.id, user.first_name, user.last_name, user.username)
    print("user:" ,user)
    bot.send_message(chat_id=update.message.chat_id, text="Hello")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry")

def sendArticles(user, article):
    """ Article contains id, title, short summary and link
    user has chat_id, user's first name(personalization)
    Reply is sent as marked up html.
    After sending, save chat id and article id to avoid repeating
    """
    pass
def subscribe(bot, update):
    """ When user subscribes to receive articles, we send a custom
    message to user. Send the first article, with some instructions
    (namely, when next article will come and how to unsubscribe)
    """
    pass
def unsubscribe(bot, update):
    """ When user unsubscibes, send message that he has been
    unsubscribed, and remove him from the subscription list
    """
    pass 

start_handler = CommandHandler('start', start)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(unknown_handler)



if __name__ == '__main__':
    updater.start_polling()