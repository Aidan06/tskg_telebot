from telebot import TeleBot, types
from time import sleep
from bs4 import BeautifulSoup
import random
import requests


token = '6158477696:AAEsSPOTTBjH3wB9VBn3st28qZxuiN8pxXs'
bot = TeleBot(token)

#
@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Привет, я телеграм-бот по сайту ts.kg! ')
    bot.send_message(message.chat.id, 'Напиши какой сериал ты хотел_а найти, постараемся найти его вместе ;)')


@bot.message_handler(content_types=['text'])
def search(message):
    bot.send_message(message.chat.id, 'Начинаю поиск, пажжи..')

@bot.message_handler(content_types=['text'])
def parser(message:types.message):
    url='https://www.ts.kg/search='+message.text
    request = requests.get(url)
    soup= BeautifulSoup(request.text, "html.parser")


    all_links = soup.find_all("a", class_="app-search-item")
    for link in all_links:
        url = "https://www.ts.kg/" + link["href"]
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        name = soup.find("div", class_="app-search-item-description")
        country = name.find("a").text
        name.find("div").extract()
        name = name.text


        img = soup.find('div', class_="app-search-item-poster")
        img = img.findChildren("img")[0]
        img = "https://www.ts.kg/" + img["src"]

@bot.send_photo(message.chat.id, img,
    caption="<b>"+name + "</b>\n<i>" + country + f"</i>\na href='{url}'>Ссылка на сайт</a>",
    parse_mode="html")
        for link in all_links:
            if all_links.index(link) == 9:
                 break

bot.infinity_polling()

