import telebot
import sqlite3

bot = telebot.TeleBot('6379992634:AAHZQGYIG1KtJ3ILgO2ttK46olfpeqj5JhA')

oragnization_name = ''
full_name = ''
job_title = ''
chat_id = ''


@bot.message_handler(commands=['start'])
def start(message):


    bot.send_message(message.chat.id, 'Привет, регистрация началась! Введите название организации')
    bot.register_next_step_handler(message, get_oragnization_name)

def get_oragnization_name(message):
    global oragnization_name

    oragnization_name = message.text
    bot.send_message(message.chat.id, 'Введите ФИО')
    bot.register_next_step_handler(message, get_full_name)

def get_full_name(message):
    global full_name

    full_name = message.text
    bot.send_message(message.chat.id, 'Введите вашу должность')
    bot.register_next_step_handler(message,get_job_title)

def get_job_title(message):
    global job_title, chat_id

    job_title = message.text
    chat_id = message.chat.id

    conn = sqlite3.connect('oprosniki2.db')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (id_inc, user_fullname, user_job, tg_id) VALUES (?, ?, ?, ?)', (oragnization_name, full_name, job_title, chat_id))
    conn.commit()
    conn.close()

    bot.send_message(message.chat.id, 'Пользователь зарегистрирован')

@bot.message_handler(commands=['users'])
def send_users(message):
    conn = sqlite3.connect('oprosniki2.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, \n ID Telegram: {el[2]}, \n Название организации: {el[3]}, \n Должность: {el[4]} \n'
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, info)

bot.infinity_polling()