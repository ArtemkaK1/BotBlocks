import vk_api
import pymysql.cursors
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})


def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='Artemiy',
                                 password='Artemka1603',
                                 db='placeadvisor',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def add_to_database(function_mode, x):
    connection = get_connection()
    cursor = connection.cursor()
    sql = ""
    cursor.execute()
    connection.commit()
    connection.close()
    return function_mode


vk = vk_api.VkApi(token='3450416addd2c309015d7fdcec9e2d25059ec3c57b6e5f60308ad121065539febf66c9dd436b4e486adba')
longpoll = VkLongPoll(vk)
# Проверка действий
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if '' != event.text and event.from_user:
            if event.text == "выпить кофе" or event.text == "Выпить кофе":
                write_msg(event.user_id, "Отлично, чтобы подобрать тебе классную кофейню, скажи, сколько денег ты готов потратить: 100, 250 или 400 рублей?", get_random_id())
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.from_user and event.text == "100":
                            write_msg(event.user_id, "Отлично, а теперь последний шаг, расскажи, какая станция метро в центре Москвы ближе всего к тебе?", get_random_id())
            elif event.text == "перекусить" or event.text == "Перекусить":
                write_msg(event.user_id, "Я знаю много разных забегаловок, чтобы выбрать идеальную для тебя скажи мне, сколько у тебя денег на все про все?", get_random_id())
            elif event.text == "покушать" or event.text == "Покушать" or event.text == "хорошенько покушать" or event.text == "Хорошенько покушать":
                write_msg(event.user_id, "Расскажи мне о своем бюджете, чтобы я мог выбрать для тебя идеальное кафе или ресторан за приятные деньги", get_random_id())
            elif event.text == "поработать" or event.text == "Поработать":
                write_msg(event.user_id, "Сколько ты готов потратить на комфотрное и приятное место для работы?", get_random_id())
            elif event.text == "Еще" or event.text == "еще":
                write_msg(event.user_id, "Помимо подбора места, ты можешь:\n\n"
                                         "1. Получить скидочный купон, если у меня таковой имеется,\n"
                                         "2. Оставить оценку заведения,\n"
                                         "3. Если ты владелец заведения, то авторизоваться и добавить описание своего заведения и его ассортимент.\n\n"
                                         "Чтобы продолжить, напиши мне номер нужного действия в списке.", get_random_id())
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if '' != event.text and event.from_user:
                            if event.text == "1":
                                write_msg(event.user_id, "Напиши название кафе или ресторана, куда хочешь сходить.", get_random_id())
                            elif event.text == "2":
                                write_msg(event.user_id, "Напиши мне свою оценку от 1 до 10 того места, куда сходил по моей рекомендации.", get_random_id())
                            elif event.text == "3":
                                write_msg(event.user_id, "Для авторизации личности, напиши мне свой E-mail.", get_random_id())



