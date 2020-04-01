import telebot
from telebot import types
import COVID19Py

try:
	covid19 = COVID19Py.COVID19()
	bot = telebot.TeleBot('980573609:AAFOVG1Ia-A9-ve_zbcI27cn_HDQTvAz4kc')

	# Функция, что сработает при отправке команды Старт
	# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
	@bot.message_handler(commands=['start'])
	def start(message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('Во всём мире')
		btn2 = types.KeyboardButton('Украина')
		btn3 = types.KeyboardButton('Россия')
		btn4 = types.KeyboardButton('США')
		markup.add(btn1, btn2, btn3, btn4)

		send_message = f"Привет {message.from_user.first_name}! \nВведите страну, о которой хотите узнать информацию!\nby @Imper1al"
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
		elif get_message_bot == "австралия":
			location = covid19.getLocationByCountryCode("AU")
		elif get_message_bot == "австрия":
			location = covid19.getLocationByCountryCode("AT")
		elif get_message_bot == "азербайджан":
			location = covid19.getLocationByCountryCode("AZ")
		elif get_message_bot == "Антарктика":
			location = covid19.getLocationByCountryCode("AQ")
		elif get_message_bot == "Аргентина":
			location = covid19.getLocationByCountryCode("AR")
		elif get_message_bot == "афганистан":
			location = covid19.getLocationByCountryCode("AF")
		elif get_message_bot == "бельгия":
			location = covid19.getLocationByCountryCode("BE")
		elif get_message_bot == "болгария":
			location = covid19.getLocationByCountryCode("BG")
		elif get_message_bot == "бразилия":
			location = covid19.getLocationByCountryCode("BR")
		elif get_message_bot == "венгрия":
			location = covid19.getLocationByCountryCode("HU")
		elif get_message_bot == "вьетнам":
			location = covid19.getLocationByCountryCode("VN")
		elif get_message_bot == "греция":
			location = covid19.getLocationByCountryCode("GR")
		elif get_message_bot == "грузия":
			location = covid19.getLocationByCountryCode("GE")
		elif get_message_bot == "дания":
			location = covid19.getLocationByCountryCode("DK")
		elif get_message_bot == "египет":
			location = covid19.getLocationByCountryCode("EG")
		elif get_message_bot == "израиль":
			location = covid19.getLocationByCountryCode("IL")
		elif get_message_bot == "индия":
			location = covid19.getLocationByCountryCode("IN")
		elif get_message_bot == "иран":
			location = covid19.getLocationByCountryCode("IQ")
		elif get_message_bot == "ирак":
			location = covid19.getLocationByCountryCode("IR")
		elif get_message_bot == "ирландия":
			location = covid19.getLocationByCountryCode("IE")
		elif get_message_bot == "исландия":
			location = covid19.getLocationByCountryCode("IS")
		elif get_message_bot == "испания":
			location = covid19.getLocationByCountryCode("ES")
		elif get_message_bot == "канада":
			location = covid19.getLocationByCountryCode("CA")
		elif get_message_bot == "китай":
			location = covid19.getLocationByCountryCode("CN")
		elif get_message_bot == "латвия":
			location = covid19.getLocationByCountryCode("LV")
		elif get_message_bot == "литва":
			location = covid19.getLocationByCountryCode("LT")
		elif get_message_bot == "мексика":
			location = covid19.getLocationByCountryCode("MX")
		elif get_message_bot == "норвегия":
			location = covid19.getLocationByCountryCode("NO")
		elif get_message_bot == "польша":
			location = covid19.getLocationByCountryCode("PL")
		elif get_message_bot == "португалия":
			location = covid19.getLocationByCountryCode("PT")
		elif get_message_bot == "турция":
			location = covid19.getLocationByCountryCode("TR")
		elif get_message_bot == "уругвай":
			location = covid19.getLocationByCountryCode("UY")
		elif get_message_bot == "хорватия":
			location = covid19.getLocationByCountryCode("HR")
		elif get_message_bot == "чехия":
			location = covid19.getLocationByCountryCode("CZ")
		elif get_message_bot == "швеция":
			location = covid19.getLocationByCountryCode("SE")
		elif get_message_bot == "швейцария":
			location = covid19.getLocationByCountryCode("CH")
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
except:
	print("Error")
# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)








