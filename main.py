import os
import telebot


bot = telebot.TeleBot("5139895429:AAHdoOcFODAV9ixTPvmNT59Y3KbO2Q6cPdA")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Arosha Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://t.me/aastrem")
  
@bot.message_handler(commands=["Hi"])
def sned_message(message):
  bot.send_message(message,"HI! how are you")
  
@bot.message_handler(commands=["123"])
def send_message(message):
  bot.send_message(message,"me mage palamu bot thawa bot keneggen hamu wemu bye!")


bot.polling()
