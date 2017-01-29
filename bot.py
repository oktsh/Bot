import config
import telebot
import datetime
import requests

now = str (datetime.date.today())
s_city = "Moscow,RU"
city_id = 524901

def listener(messages):
    for m in messages:
        if m.text == 'дата' or m.text == 'Дата':
            bot.send_message(m.chat.id, now)
        elif m.text == 'Жендос педрила':
            bot.send_message(m.chat.id, 'согласен')
        elif m.text =='погода' or m.text =='Погода':
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': config.appid})
                data = res.json()
                bot.send_message(m.chat.id, 'Погода в Москве')
                conditions = data['weather'][0]['description']
                bot.send_message(m.chat.id, 'На улице' + ' ' + conditions)
                temp =  data['main']['temp']
                bot.send_message(m.chat.id, 'Температура' + ' ' + str(temp))
                mintemp =  data['main']['temp_min']
                bot.send_message(m.chat.id, 'Мин. температура' + ' ' + str(mintemp))
                maxtemp = data['main']['temp_max']
                bot.send_message(m.chat.id, 'Макс. температура' + ' ' + str(maxtemp))
            except Exception as e:
                print("Exception (weather):", e)
                pass
if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)

