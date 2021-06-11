import telebot,time
bot = telebot.TeleBot('1805324087:AAELyPBQQTw274xfkBfmOyJx7WTjktBAurQ')

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    print(message)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, создатель этого бота @Danil_278 \n'
                                      'Его сообщение:\n'
                                      '"Зай, ты самая лучшая моя девочка , я тебя очень сильно люблю🥰🥰 Ты милая и прикольная 😍😘 Ты наверное не знала, '
                                      ' что я такое умею делать,  но вот умею), сейчас скину твои фоточки :) Они очень классные "')
    time.sleep(5)
    bot.send_photo(message.chat.id,'AgACAgIAAxkBAAMIYMMZVneE3lZcDdE2VPugbUskelIAAq2yMRuy_RhK-m1-iYz8vnAKBY-hLgADAQADAgADbQAD0oQDAAEfBA')
    time.sleep(5)
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMJYMMZYYlDD8QTorK7HCjuOgIAAU20AAKWtTEbKXAZSjixL0Bel4TlkGsAAZ8uAAMBAAMCAANtAAMtTQUAAR8E')
    time.sleep(5)
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMKYMMZcY7UrW_4AAE3ccbGgaENk6ZQAAKXtTEbKXAZSowIueYCjukkbY9UpC4AAwEAAwIAA20AA-guAgABHwQ')
    time.sleep(5)
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMLYMMZcvIdDdk4EPJkR8qkVym7obQAAj2zMRsAAakZSog6eBPSI-yJI-_Noi4AAwEAAwIAA20AA5kyAwABHwQ')
    time.sleep(5)
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMMYMMZcoYQh6iAgVgt_tTWWuUh0zQAApi1MRspcBlK-Wp7TMJhremvmAGeLgADAQADAgADbQADO74AAh8E')
    time.sleep(5)
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMNYMMZc0j1sn4JwKGISU9Q_D5nEooAApm1MRspcBlKP_7RTwLxFgxRdU6kLgADAQADAgADbQADvVQCAAEfBA')
    time.sleep(5)
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAMOYMMZdaaNJa1vFMcTczZ7v0-xdD4AApu1MRspcBlKG-FyrRXBI6hpp5ahLgADAQADAgADbQAD3mYDAAEfBA')
    time.sleep(5)
    bot.send_message(message.chat.id,'Зай, ты самая красивая девочка!'
                                    'Я тебя очень сильно люблю 💋💋💋')
@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'лох':
        bot.send_message(message.chat.id,'Гандоны они и на то гандоны!')
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECafNgwxPSOnZFkOig9l12RYfLMvTYpgACBgADwDZPE8fKovSybnB2HwQ')

bot.polling()
