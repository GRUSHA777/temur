from data.txt import *
from data.setup import *
import telebot
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    meal_markup = types.InlineKeyboardMarkup(row_width=1)
    meal1_button = types.InlineKeyboardButton(sel1opt1_txt, callback_data='zavtrak')
    meal2_button = types.InlineKeyboardButton(sel1opt2_txt, callback_data='obed')
    meal3_button = types.InlineKeyboardButton(sel1opt3_txt, callback_data='dinner')
    meal_markup.add(meal1_button, meal2_button, meal3_button)
    id = message.from_user.id
    bot.send_message(id, welcome_msg, reply_markup=meal_markup)

@bot.callback_query_handler(func=lambda call: True)
def query(call):
    print(call.data)
    id = call.from_user.id
    if call.data == 'zavtrak':
        markup = types.InlineKeyboardMarkup(row_width=1)
        for i in range(len(zavtraknames.keys())):
            keys = list(zavtraknames.keys())
            markup.add(types.InlineKeyboardButton(
                text=zavtraknames[keys[i]],
                callback_data='diszavtrak' + keys[i]))
        bot.send_message(id, choose_breakfast_txt, reply_markup=markup)
    elif 'diszavtrak' in call.data and 'sel' not in call.data:
        print(call.data)
        select_markup = types.InlineKeyboardMarkup()
        select_markup.add(types.InlineKeyboardButton(select_button_txt, callback_data='sel'+call.data))
        message = open('assets/photoes/' + call.data + '.jpeg', 'rb')
        bot.send_photo(id, message, caption=zavtrakdis[call.data[-1]]+disclaimer, reply_markup=select_markup, parse_mode='HTML')
        message.close()
    elif call.data == 'obed':
        markup = types.InlineKeyboardMarkup(row_width=4)
        keys = list(obed_base_names.keys())
        markup.add(
            types.InlineKeyboardButton(text=obed_base_names[keys[0]], callback_data='disobedbase' + keys[0]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[1]], callback_data='disobedbase' + keys[1]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[2]], callback_data='disobedbase' + keys[2]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[3]], callback_data='disobedbase' + keys[3]))
        markup.add(
            types.InlineKeyboardButton(text=obed_base_names[keys[4]], callback_data='disobedbase' + keys[4]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[5]], callback_data='disobedbase' + keys[5]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[6]], callback_data='disobedbase' + keys[6]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[7]], callback_data='disobedbase' + keys[7]))
        bot.send_message(id, obed_base_txt, reply_markup=markup)
    elif call.data == 'dinner':
        markup = types.InlineKeyboardMarkup(row_width=4)
        keys = list(obed_base_names.keys())
        markup.add(
            types.InlineKeyboardButton(text=obed_base_names[keys[0]], callback_data='disdinbase' + keys[0]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[1]], callback_data='disdinbase' + keys[1]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[2]], callback_data='disdinbase' + keys[2]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[3]], callback_data='disdinbase' + keys[3]))
        markup.add(
            types.InlineKeyboardButton(text=obed_base_names[keys[4]], callback_data='disdinbase' + keys[4]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[5]], callback_data='disdinbase' + keys[5]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[6]], callback_data='disdinbase' + keys[6]),
                   types.InlineKeyboardButton(text=obed_base_names[keys[7]], callback_data='disdinbase' + keys[7]))
        bot.send_message(id, obed_base_txt, reply_markup=markup)
    elif 'disdinbase' in call.data and 'sel' not in call.data:
        select_markup = types.InlineKeyboardMarkup()
        select_markup.add(types.InlineKeyboardButton(select_button_txt, callback_data='sel'+call.data))
        message = open('assets/photoes/disobedbase' + call.data[-1] + '.jpeg', 'rb')
        bot.send_photo(id, message, caption=disobedbase[call.data[-1]]+disclaimer, reply_markup=select_markup, parse_mode='HTML')
        message.close()
    elif 'disobedbase' in call.data and 'sel' not in call.data:
        select_markup = types.InlineKeyboardMarkup()
        select_markup.add(types.InlineKeyboardButton(select_button_txt, callback_data='sel'+call.data))
        message = open('assets/photoes/' + call.data + '.jpeg', 'rb')
        bot.send_photo(id, message, caption=disobedbase[call.data[-1]]+disclaimer, reply_markup=select_markup, parse_mode='HTML')
        message.close()
    elif 'disside' in call.data and 'sel' not in call.data:
        select_markup = types.InlineKeyboardMarkup()
        select_markup.add(types.InlineKeyboardButton(select_button_txt, callback_data='sel'+call.data))
        message = open('assets/photoes/disside' + call.data[-1] + '.jpeg', 'rb')
        bot.send_photo(id, message, caption=side_dishes_dis[call.data[-1]]+disclaimer, reply_markup=select_markup, parse_mode='HTML')
        message.close()
    elif 'sel' in call.data:
        if 'diszavtrak' in call.data:
            bot.send_message(id, your_zavtrak_txt + zavtraknames[call.data[-1]])
            bot.send_message(id, comeback_txt)
            bot.send_message(id, drinks)
        elif 'disobedbase' in call.data:
            ask_for_side_dish(call, protein_base=call.data[-1])
        elif 'disdinbase' in call.data:
            ask_for_side_dish_din(call, protein_base=call.data[-1])
        elif 'dissidedin' in call.data:
            dinner = obed_base_real_names[call.data[-2]]
            bot.send_message(id, your_dinner_txt + dinner + ' + ' + dinner_side_dishes_names[call.data[-1]])
            bot.send_message(id, comeback_txt)
            bot.send_message(id, drinks)
        elif 'disside' in call.data:
            obed = obed_base_real_names[call.data[-2]]
            bot.send_message(id, your_obed_txt + obed + ' + ' + side_dishes_names[call.data[-1]])
            bot.send_message(id, comeback_txt)
            bot.send_message(id, drinks)


def ask_for_side_dish(call, protein_base):
    id = call.from_user.id
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i in range(len(side_dishes_names.keys())):
        keys = list(side_dishes_names.keys())
        print(keys)
        markup.add(types.InlineKeyboardButton(
            text=side_dishes_names[keys[i]],
            callback_data='disside'+protein_base+keys[i]))
    bot.send_message(id, ask_for_side, reply_markup=markup)


def ask_for_side_dish_din(call, protein_base):
    id = call.from_user.id
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i in range(len(dinner_side_dishes_names.keys())):
        keys = list(dinner_side_dishes_names.keys())
        print(keys)
        markup.add(types.InlineKeyboardButton(
            text=dinner_side_dishes_names[keys[i]],
            callback_data='dissidedin'+protein_base+keys[i]))
    bot.send_message(id, ask_for_side, reply_markup=markup)


bot.polling()