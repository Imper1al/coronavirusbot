#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('980573609:AAH6xwvvXgQQ_rLwJ5PUuGzUvviEnwnFsDg')

# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Украина')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Беларусь')
    markup.add(btn1, btn2, btn3, btn4)

    send_message = f"Привет {message.from_user.first_name}! \nВведите страну, о которой хотите узнать информацию!"
    bot.send_message(message.chat.id, send_message, reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "сша":
		location = covid19.getLocationByCountryCode("US")
	elif get_message_bot == "украина":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "россия":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "беларусь":
		location = covid19.getLocationByCountryCode("BY")
	elif get_message_bot == "казакхстан":
		location = covid19.getLocationByCountryCode("KZ")
	elif get_message_bot == "италия":
		location = covid19.getLocationByCountryCode("IT")
	elif get_message_bot == "франция":
		location = covid19.getLocationByCountryCode("FR")
	elif get_message_bot == "германия":
		location = covid19.getLocationByCountryCode("DE")
	elif get_message_bot == "япония":
		location = covid19.getLocationByCountryCode("JP")
	else:
		location = covid19.getLatest()
	final_message = f"Данные по всему миру:\nЗаболевших: {location['confirmed']:,}\nСметрей: {location['deaths']:,}"

	if final_message == "":
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"Данные по стране: \nНаселение: {location[0]['country_population']:,}" \
				f"\nПоследнее обновление: {date[0]} {time[0]}\nПоследние данные: " \
				f"\nЗаболевших: {location[0]['latest']['confirmed']:,}\nСметрей: " \
				f"{location[0]['latest']['deaths']:,}"

	bot.send_message(message.chat.id, final_message)

# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)








