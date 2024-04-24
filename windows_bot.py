import telebot
from telebot import types

API_TOKEN = '6650787865:AAEVTVwsYlXA3Ua-dGz19a4yracehT_U5WE'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_price = types.KeyboardButton('Прайс')
    btn_order = types.KeyboardButton('Оставить заявку')
    markup.add(btn_price, btn_order)

    bot.send_message(message.chat.id, "Привет!\n\nМы занимаемся установкой и ремонтом металлопластиковых окон, а также остеклением балконов в городе Батуми! Мы предоставляем такие услуги как регулировка механизмов и установка москитных сеток. Выезжаем на замер в день получения заявки. Выполним заказ качественно и в кратчайшие сроки!\n\nЧтобы увидеть весь список наших услуг и ознакомиться с ценами нажмите на кнопку ""Прайс""\n\nНажмите на кнопку ""Оставить Заявку"", заполните форму и мы вам перезвоним!\n\nВы также можете сами позвонить нам по номеру с 09:00 до 20:00 в любой день!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Прайс')
def send_price(message):
    bot.send_message(message.chat.id, "Прайс лист! Цена на нестандартные проекты обговаривается с мастером до и после проведения замеров.\n\nОстекление балконов - 320 лари/кв.м\nМоскитные сетки на петлях - 50 лари/кв.м\nРаздвижные москитные сетки плиссе - 120 лари/кв.м\nРеулировка окон - 30 лари/окно")
    # Отправить прайс

@bot.message_handler(func=lambda message: message.text == 'Оставить заявку')
def request_info(message):
    msg = bot.send_message(message.chat.id, "Введите ваше имя")
    bot.register_next_step_handler(msg, ask_phone)

def ask_phone(message):
    global user_name
    user_name = message.text
    msg = bot.send_message(message.chat.id, "Введите ваш номер телефона")
    bot.register_next_step_handler(msg, send_request)

def send_request(message):
    phone_number = message.text
    bot.send_message(829420123, f"Новая заявка!\nИмя: {user_name}\nНомер телефона: {phone_number}")
    bot.send_message(message.chat.id, f"Спасибо, {user_name}! Ваша заявка успешно принята, мы скоро свяжемся с Вами!")

bot.remove_webhook()

bot.polling()