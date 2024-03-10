from telebot.types import KeyboardButton,ReplyKeyboardMarkup


def search():
    markub=ReplyKeyboardMarkup(resize_keyboard=True)
    markub.add(KeyboardButton('🔎search'))
    return markub


def Meniu():
    markub=ReplyKeyboardMarkup(resize_keyboard=True)
    markub.add(
        KeyboardButton('ташкент'),
        KeyboardButton('гулистан'),
        KeyboardButton('навои'),
        KeyboardButton('андижан'),
        KeyboardButton('джизак'),
        KeyboardButton('наманган'),
        KeyboardButton('самарканд'),
        KeyboardButton('фергана'),
        KeyboardButton('ургенч'),
        KeyboardButton('бухара')
    )
    return markub