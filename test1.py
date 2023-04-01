import json #Подключаем библиотеку, отвечающую за работу с JSON
from pprint import pprint #подключили Pprint для красоты выдачи текста

with open("personal.json", "r", encoding="utf-8") as f: #открываем файл personal.json и указываем его кодировку — что бы можно было работать с русскими буквами
    text = json.load(f) #загоняем в переменную все, что получилось в результате работы библиотеки
    pprint(text) #выводим результат на экран

for a in text['personal']: #создали цикл, который будет работать построчно
    print(a['name'], ':', a['salary']) #и выводим на экран все, что в значении ключей name и salary


stroke = '{"food": "banana"}' #json-строка
stroke_s = json.loads(stroke) #загоняем в переменную результат чтения json-строки
print(stroke_s) #выводим результат на экран"'