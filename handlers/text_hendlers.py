
import requests
from bs4 import BeautifulSoup as BS
from telebot.types import Message,ReplyKeyboardRemove
from loadr import bot
from keyboards import *

@bot.message_handler(func=lambda message:message.text=='🔎search' )
def reaction_search(message:Message):
   chat_id =message.chat.id
   svg=bot.send_message(chat_id,'Shahar nomini 🌁',reply_markup=Meniu())
   bot.register_next_step_handler(svg,Ob_havo)


def Ob_havo(message:Message):
    chat_id=message.chat.id
    t=requests.get(f'https://sinoptik.ua/погода-{message.text.title()}')
    html_t=BS(t.content,'html.parser')

    for el in html_t.select('#content'):
       min=el.select('.temperatura.min')[0].text
       max=el.select('.temperatura .max')[0].text
       t_min=min[4:]
       t_max=max[5:]
       bot.send_message(chat_id,f'Harorat Min: {t_min} Min:{t_max}',reply_markup=search())

