import telebot 

bot = telebot.TeleBot('token from @BotFather') 

@bot.message_handler(commands = ['start']) 
def main(message): 
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}, you used TG bot from github!")
bot.polling(none_stop=True)
