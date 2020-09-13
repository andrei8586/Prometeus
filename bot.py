import telebot
from telebot import types
bot = telebot.TeleBot('1209790679:AAEB6lFuu00wI3nIpnoUqjBxCrwkwVO-ZxE')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        key_one = types.InlineKeyboardButton(text="Какую поддержку я могу получить?", callback_data='1')
        keyboard.add(key_one)
        bot.send_message(message.from_user.id, text="Привет, я бот команды Prometeus, чем могу быть полезен?", reply_markup=keyboard)
    else :
        bot.send_message(message.from_user.id, "Напиши 'Привет'")
@bot.message_handler(content_types=['text'])
@bot.callback_query_handler(func=lambda call: True, )
def callback_worker(call):
    if call.data == '1':
       send = bot.send_message(call.message.chat.id, 'Для расчёта мне необходима информация\n')
    elif call.data == '2':
        global academ_stip
        academ_stip = 1
        achievments()
    elif call.data == '4':
        global achiev_ments
        achiev_ments = 1
    bot.register_next_step_handler(send, get_family_money)

@bot.message_handler(content_types=['text'])
def achievments(message):
    keyboard3 = types.InlineKeyboardMarkup()
    key_two = types.InlineKeyboardButton(text="Да", callback_data=4)
    key_three = types.InlineKeyboardButton(text="Нет", callback_data=5)
    keyboard3.add(key_two, key_three)
    bot.send_message(message.chat.id, text="Получаете ли вы академическую стипендию?", reply_markup=keyboard2)


def get_family_money(message):
    keyboard2 = types.InlineKeyboardMarkup()
    key_two = types.InlineKeyboardButton(text = "Да", callback_data = 2)
    key_three = types.InlineKeyboardButton(text = "Нет", callback_data = 3)
    keyboard2.add(key_two,key_three)
    bot.send_message(message.from_user.id,text = "Получаете ли вы академическую стипендию?", reply_markup=keyboard2)



def get_num_of_months(message):
    global num_of_months
    num_of_months = 0
    while num_of_months == 0:
        try:
            num_of_months = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введены некоректные данные. Повторите попытку ввода.')
    send = bot.send_message(message.chat.id, 'Количество членов семьи?')
    bot.register_next_step_handler(send, get_num_of_family_members)

def get_num_of_family_members(message):
    global num_of_family_members
    num_of_family_members = 0
    while num_of_family_members == 0:
        try:
            num_of_family_members = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введены некоректные данные. Повторите попытку ввода.')
    send = bot.send_message(message.chat.id, ('Среднедушевой доход равен ' +get_result(num_of_family_members, num_of_months, family_money)))



def get_result(a, b, c):
    return str((c / b / a))

bot.polling(none_stop=True, interval=0)


"""def get_num_of_employable_family_members(message):
    global  num_of_employable_family_members
    num_of_employable_family_members = 0
    while num_of_employable_family_members == 0:
        try:
            num_of_employable_family_members = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id,'Введены некоректные данные. Повторите попытку ввода.')
    send = bot.send_message(message.chat.id,'Какого количество детей в семье, до 15-лет включительно?')
    bot.register_next_step_handler(send, get_num_of_children_under_15_yo)

def get_num_of_children_under_15_yo(message):
    global num_of_children_under_15_yo
    num_of_children_under_15_yo = 0
    while  num_of_children_under_15_yo == 0:
        try:
            num_of_children_under_15_yo = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введены некоректные данные. Повторите попытку ввода.')
    send = bot.send_message(message.chat.id,'Какого количество пенсионеров и инвалидов в семье?')
    bot.register_next_step_handler(send, get_num_of_disabled_people)

def get_num_of_disabled_people(message):
    global num_of_disabled_people
    num_of_disabled_people = 0
    while num_of_disabled_people == 0:
        try:
            num_of_disabled_people = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введены некоректные данные. Повторите попытку ввода.')
    send = bot.send_message(message.chat.id, 'Какую сумму вы платите за ЖКХ?')
    bot.register_next_step_handler(send, get_num_of_housing_fees)


def get_num_of_housing_fees(message):
    global num_of_housing_fees
    num_of_housing_fees = 0
    while num_of_housing_fees == 0:
        try:
            num_of_housing_fees = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введены некоректные данные. Повторите попытку ввода.')
    send = bot.send_message(message.chat.id, 'Какого общее количество членов семьи?')
    bot.register_next_step_handler(send, get_total_num_of_family_members)

def get_total_num_of_family_members(message):
    global total_num_of_family_members
    total_num_of_family_members = 0
    while total_num_of_family_members == 0:
        try:
            total_num_of_family_members = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введены некоректные данные. Повторите попытку ввода.')
            
    send = bot.send_message(message.chat.id, 'Проводится расчёт...')
"""



