from telebot import *

import consts
import lessons_text

bot = telebot.TeleBot(consts.TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    lessons_text.start_mess(message)


@bot.message_handler(content_types=["text"])
def send_course(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(consts.RETURN_BUTTON)
    if message.text == consts.RETURN_BUTTON:
        lessons_text.return_btn(message)

    elif message.text == consts.first_lesson_btn:
        lessons_text.first_lesson(message, markup)

    elif message.text == consts.second_lesson_btn:
        lessons_text.second_lesson(message, markup)

    elif message.text == consts.third_lesson_btn:
        lessons_text.third_lesson(message, markup)

    elif message.text == consts.fourth_lesson_btn:
        lessons_text.fourth_lesson(message, markup)

    elif message.text == consts.fifth_lesson_btn:
        lessons_text.fifth_lesson(message, markup)

    elif message.text == consts.sixth_lesson_btn:
        lessons_text.sixth_lesson(message, markup)

    elif message.text == consts.seventh_lesson_btn:
        lessons_text.seventh_lesson(message, markup)

    elif message.text == consts.eight_lesson_btn:
        lessons_text.eight_lesson(message, markup)


bot.infinity_polling()
