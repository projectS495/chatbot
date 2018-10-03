from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('JomBot')
bot.set_trainer(ListTrainer)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print("Sandra :", reply)
    if message.strip() == 'Bye':
        print('Sandra : Bye')
        break