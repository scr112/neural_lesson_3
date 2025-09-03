import random
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
error_answer = 0
accept_answer = 0
question_count = 0
repeat_answer = 1
question_list = [
    {"name": "В. В. Путин", "birthdate": "10-7-1952"},
    {"name": "Д. В. Медведев", "birthdate": "14-09-1952"},
    {"name":"Б. Н. Ельцин", "birthdate" : "02-01-1931"}, 
    {"name":"М. С. Горбачев", "birthdate": "03-02-1931"}, 
    {"name":"Л. И. Брежнев", "birthdate":"19-12-1906"}, 
    {"name":"В. А. Андропов","birthdate":"15-06-1914"},
    {"name":"Д. Байден","birthdate":"20-11-1942"},
    {"name":"Б. Обама","birthdate":"04-08-1961"},
    {"name":"Д. Буш Младший","birthdate":"14-06-1946"}

    ]

selected_question = random.sample(question_list, 5)
question_count = len(selected_question)

for i in range(len(selected_question)):
    birthdate_str = selected_question[i]['birthdate']
    birthdate_obj = datetime.strptime(birthdate_str, '%d-%m-%Y').date()
    days = {
        "01": "первое",
        "02": "второе",
        "03": "третье",
        "04": "четвертое",
        "05": "пятое",
        "06": "шестое",
        "07": "седьмое",
        "08": "восьмое",
        "09": "девятое",
        "10": "десятое",
        "11": "одиннадцатое",
        "12": "двенадцатое",
        "13": "тринадцатое",
        "14": "четырнадцатое",
        "15": "пятнадцатое",
        "16": "шестнадцатое",
        "17": "семнадцатое",
        "18": "восемнадцатое",
        "19": "девятнадцатое",
        "20": "двадцатое",
        "21": "двадцать первое",
        "22": "двадцать второе",
        "23": "двадцать третье",
        "24": "двадцать четвертое",
        "25": "двадцать пятое",
        "26": "двадцать шестое",
        "27": "двадцать седьмое",
        "28": "двадцать восьмое",
        "29": "двадцать девятое",
        "30": "тридцатое",
        "31": "тридцать первое"
    }
    day = birthdate_obj.day
    day_str = f"{day:02d}"
    if day_str in days:
        day = days[day_str]
    else:
        print("день не найден в словаре")
    try:
        user_input = (input (f"Когда родился {selected_question[i]['name']}? (формат dd.mm.yyyy): ").strip())
        user_input = datetime.strptime(user_input, '%d.%m.%Y').date()
        if user_input == birthdate_obj:
            print(f'Правильно')
            accept_answer += 1
        if user_input != birthdate_obj:
            print(f'не правильно, правильный ответ: ', selected_question[i]['name'], 'родился', day, birthdate_obj.strftime("%B %Y"))
            error_answer += 1
    except:
        print(f'неверный формат данных')
print(f'количество правильных ответов: {accept_answer}\nколичество неправильных ответов: {error_answer}')
