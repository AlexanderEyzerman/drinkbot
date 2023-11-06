import telebot 
import webbrowser
import time
from telebot import types

api_token= '6944672764:AAHqOLGcNqNWPR5cEe2WBIEXIm7FAnxQ5bo' #token

bot = telebot.TeleBot(api_token) 

#словарь с локациями; value здесь это кол-во бутылок в автомате по адресу
locations = {
    'ТРЦ "Ривьера"':40,
    'ТЦК "Смоленский пассаж"':25,
    'Центральный Детский Магазин':0,
    'ТРЦ "Океания"':19,
    'ТРЦ "РИО" Ленинский':100
}
#по-идее мусор и можно делитнуть
socials = {
    'Instagram':'ref',
    'Website':'ref',
    'VK':'ref',
    'Telegram':'ref'
}
#отправляем приветствие и инициализируем кнопки
@bot.message_handler(commands = ['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Карта "ПЕЙ"')
    btn2 = types.KeyboardButton('Выбрать автомат')
    markup.row(btn2)
    btn3 = types.KeyboardButton('Поддержка')
    btn4 = types.KeyboardButton('Наши соцсети')
    markup.row(btn1,btn3)
    btn5 = types.KeyboardButton('FAQ')
    markup.row(btn4,btn5)
    bot.send_message(message.chat.id, f'''\
    Привет, {message.from_user.first_name}, добро пожаловать в мир, где вода бесплатна!
ПЕЙ – это социальный проект, ты можешь получать бесплатную воду и интересные предложения от наших партнеров каждый день!\
    ''', reply_markup = markup
    )

    inlinemarkup = types.InlineKeyboardMarkup()
    inlbtn1 = types.InlineKeyboardButton('НАШ САЙТ', url = 'https://peii.ru')
    inlbtn2 = types.InlineKeyboardButton('Telegram',callback_data = 'tg')
    inlinemarkup.row(inlbtn1,inlbtn2)
    inlbtn3 = types.InlineKeyboardButton('Instagram',callback_data = 'inst')
    inlbtn4 = types.InlineKeyboardButton('VK',callback_data = 'vk')
    inlinemarkup.row(inlbtn3,inlbtn4)
    time.sleep(3)
    bot.send_message(message.chat.id,'Присоединяйся к нашему сообществу:',reply_markup=inlinemarkup)
    bot.send_photo(message.chat.id,open("D:\\Bots\\drinkbot\\drinkbotpic1.jpg",'rb')) #хз как вставить path с гита, пока только так
 
#работа с запросами от кнопок
@bot.message_handler(content_types=['text'])
def on_click(message):
    if message.text == 'Карта "ПЕЙ"':
        bot.send_message(message.chat.id,'card info')
    
    elif message.text == 'Выбрать автомат':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        loc1 = types.KeyboardButton('ТРЦ "Ривьера"')
        loc2 = types.KeyboardButton('ТЦК "Смоленский пассаж"')
        loc3 = types.KeyboardButton('Центральный Детский Магазин')
        loc4 = types.KeyboardButton('ТРЦ "Океания"')
        loc5 = types.KeyboardButton('ТРЦ "РИО" Ленинский')

        back = types.KeyboardButton('Главное меню')
        markup.add(loc1)
        markup.add(loc2)
        markup.add(loc3)
        markup.add(loc4)
        markup.add(loc5)
        markup.add(back)
        bot.send_message(message.chat.id, text= 'Выберите адрес автомата', reply_markup=markup)

    elif message.text in locations:
        inlinemarkup = types.InlineKeyboardMarkup()
        inlbtn1 = types.InlineKeyboardButton('Получить бутылку',callback_data = 'get bottle')
        #inlbtn2 = types.InlineKeyboardButton('Назад',callback_data = 'back')
        inlinemarkup.add(inlbtn1) #,inlbtn2)
        bot.send_message(message.chat.id,f'В автомате {locations[message.text]} бутылок',reply_markup = inlinemarkup)
        
  
    elif message.text == 'Поддержка':
        bot.send_message(message.chat.id,'send support url')
    
    elif message.text == 'Наши соцсети':
        inlinemarkup = types.InlineKeyboardMarkup()
        inlbtn1 = types.InlineKeyboardButton('НАШ САЙТ', url = 'https://peii.ru')
        inlbtn2 = types.InlineKeyboardButton('Telegram',callback_data = 'tg')
        inlinemarkup.row(inlbtn1,inlbtn2)
        inlbtn3 = types.InlineKeyboardButton('Instagram',callback_data = 'inst')
        inlbtn4 = types.InlineKeyboardButton('VK',callback_data = 'vk')
        inlinemarkup.row(inlbtn3,inlbtn4)
        bot.reply_to(message,'Присоединяйся к нашему сообществу:',reply_markup=inlinemarkup)

    
    elif message.text == 'FAQ':
        bot.send_message(message.chat.id,'send FAQ ref')

    elif message.text == 'Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Карта "ПЕЙ"')
        btn2 = types.KeyboardButton('Выбрать автомат')
        markup.row(btn2)
        btn3 = types.KeyboardButton('Поддержка')
        btn4 = types.KeyboardButton('Наши соцсети')
        markup.row(btn1,btn3)
        btn5 = types.KeyboardButton('FAQ')
        markup.row(btn4,btn5)
        bot.send_message(message.chat.id,text = "Вы вернулись в главное меню", reply_markup=markup)
    
    else:
        bot.send_message(message.chat.id,'unknown query')

#работа с запросами от inline кнопок, пока что это только запрос кода из автомата, кнопка back я считаю не нужна 
@bot.callback_query_handler(func = lambda callback:True)
def callback_message(callback):
    if callback.data == 'get bottle':
        bot.send_message(callback.message.chat.id,'Для получения бутылки воды введите на автомате код 12135  и нажмите кнопку “ОК” ')
        time.sleep(3)
        bot.send_message(callback.message.chat.id,'Возьми бутылку и насладись вкусной водой. Хорошего дня!')
        bot.send_message(callback.message.chat.id,'picture2ref')
    elif callback.data == 'back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        loc1 = types.KeyboardButton('ТРЦ "Ривьера"')
        loc2 = types.KeyboardButton('ТЦК "Смоленский пассаж"')
        loc3 = types.KeyboardButton('Центральный Детский Магазин')
        loc4 = types.KeyboardButton('ТРЦ "Океания"')
        loc5 = types.KeyboardButton('ТРЦ "РИО" Ленинский')
    
        back = types.KeyboardButton('Главное меню')
        markup.add(loc1)
        markup.add(loc2)
        markup.add(loc3)
        markup.add(loc4)
        markup.row(loc5)
        markup.add(back)
        bot.send_message(callback.message.chat.id, text= 'Выберите адрес автомата', reply_markup=markup)
        
bot.infinity_polling()
