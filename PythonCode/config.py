import vk_api
import pymysql
from vk_api.longpoll import VkEventType, VkLongPoll
import requests
from vk_api.utils import get_random_id
from vk_bot import VKBot
import uuid

def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

def get_connection():
    connection = pymysql.connect(
        user='root',
        password='Volrik1603',
        host='localhost',
        db='placeadvisor',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return connection

def add_user(usermane, email):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO users (username, email) VALUES (%s, %s)'
    vkbot = VKBot(event.user_id)
    cursor.execute(sql, (vkbot._USERNAME, email))
    connection.close()

def select_coupon(place):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT coupon FROM coupons WHERE place=%s'
    cursor.execute(sql, (place,))
    result = cursor.fetchone()
    connection.close()
    return result

def add_coupons(place):
    connection =  get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO coupons (place, coupon) VALUES (%s, %s)'
    cursor.execute(sql, (place, str(uuid.uuid4())))
    connection.commit()
    connection.close()


vk = vk_api.VkApi(token='3450416addd2c309015d7fdcec9e2d25059ec3c57b6e5f60308ad121065539febf66c9dd436b4e486adba')
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if (event.text == 'создать купоны' or event.text == 'Создать купоны') and event.from_user:
            write_msg(event.user_id, "Напиши мне название своего заведения", get_random_id())
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    add_coupons(event.text)
                    break
        elif event.to_me:
            vkbot = VKBot(event.user_id)
            write_msg(event.user_id, vkbot.messages_send(event.text), get_random_id())
            print(event.text)


