import telebot
from function_script import get_id  # Import the get_id function
from ip1 import get_ip  # Import the get_ip function
from bin1 import get_bin_info  # Import the get_bin_info function
from credit_card_gen import generate_cc

BOT_TOKEN = '6023140310:AAFWwGXvsIOqFKqdKwx5q8CUF7DUAJJy7jA'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Bot started!')

@bot.message_handler(commands=['id'])
def handle_me(message):
    response = get_id(message)
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['ip'])
def handle_ip(message):
    response = get_ip(message)
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['gen'])
def handle_gen(message):
    card_info = message.text.split('/gen ', 1)[1]  # Extract the text after '/gen '
    response = generate_cc(card_info, message.from_user.id, message.from_user.username)
    bot.send_message(message.chat.id, response, parse_mode='HTML')  # Updated parse_mode to 'HTML' for better formatting

@bot.message_handler(commands=['bin'])
def handle_bin(message):
    response = get_bin_info(message)
    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)
