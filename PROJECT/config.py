import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.utils import get_random_id

from vk_bot import VKBot
from vk_sql import DbWork

def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

places_adm = ['Cofix', 'One Price Coffee', 'Surf Coffee', 'Starbucks', 'Krispy Kreme', 'Хлеб насущный', 'Subway',
          'Mcdonalds', 'KFC', 'Burger King', 'МУ-МУ', 'Хлеб насущный', 'BB & Burgers','Франклинс бургер',
          'Шоколадница', '#FARШ', 'Шоколадница', 'Grill Crafted Bar', 'Чайхона №1', 'Вареничная', 'Тануки',
          'Якитория', 'Арбатский базар', 'Джон Джоли', 'Депо']

vk = vk_api.VkApi(token='3450416addd2c309015d7fdcec9e2d25059ec3c57b6e5f60308ad121065539febf66c9dd436b4e486adba')
longpoll = VkLongPoll(vk)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        # Создание купонов
        if event.to_me and ('купон' in event.text.lower()) and ('купоны' not in event.text.lower()) and ('создать' not in event.text.lower()):
            vksql = DbWork(event.user_id)
            vksql.add_coupons(event.text)
            write_msg(event.user_id, vksql.sql_message(event.text), get_random_id())
            print(event.text)

        # Авторизация пользователя
        elif event.to_me and ('@' in event.text):
            vksql = DbWork(event.user_id)
            vksql.add_user(event.text)
            write_msg(event.user_id, vksql.sql_message(event.text), get_random_id())
            print(event.text)

        # Оценка заведения
        elif event.to_me and ('оценка' in event.text.lower()):
            vksql = DbWork(event.user_id)
            vksql.add_mark(event.text)
            write_msg(event.user_id, vksql.sql_message(event.text), get_random_id())
            print(event.text)

        # Получение купона пользователем
        elif event.to_me and event.text in places_adm:
            vksql = DbWork(event.user_id)
            coupon = vksql.select_coupon(event.text)
            write_msg(event.user_id, f"Твой купон для {event.text}: {coupon}", get_random_id())
            print(event.text)

        # Добавить описание
        elif event.to_me and (('описание' in event.text) or ('меню' in event.text)):
            place_description = event.text
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me and 'описание' in event.text.lower():
                        vksql = DbWork(event.user_id)
                        vksql.add_description(place_description, event.text)
                        write_msg(event.user_id, f"Описание для {place_description} добавлено", get_random_id())
                        break
                    elif event.to_me and 'меню' in event.text.lower():
                        vksql = DbWork(event.user_id)
                        vksql.add_menu(place_description, event.text)
                        write_msg(event.user_id, f"Меню для {place_description} добавлено", get_random_id())
                        break

        # Сообщения с советами и командами
        elif event.to_me:
            vkbot = VKBot(event.user_id)
            write_msg(event.user_id, vkbot.messages_send(event.text), get_random_id())
            print(event.text)


