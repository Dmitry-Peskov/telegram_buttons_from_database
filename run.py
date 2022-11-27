import telebot

from db import CreateMenu

bot = telebot.TeleBot("ТОКЕН ВАШЕГО БОТА")
cm = CreateMenu()

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать", reply_markup= cm.create_menu('main'))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'buy':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Что покупаем?", reply_markup= cm.create_menu('buy'))
    if call.data == 'sell':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Что продаём?", reply_markup= cm.create_menu('sell'))
    if call.data == 'back':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать", reply_markup= cm.create_menu('main'))
    if call.data == 'help':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ничем не могу помочь тебе", reply_markup= cm.create_menu('help'))

if __name__ == "__main__":
    bot.polling(none_stop=True)