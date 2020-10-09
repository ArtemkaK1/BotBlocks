import vk_api
import pymysql
from vk_api.longpoll import VkEventType, VkLongPoll
import requests
from vk_api.utils import get_random_id
from vk_bot import VKBot

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

vk = vk_api.VkApi(token='3450416addd2c309015d7fdcec9e2d25059ec3c57b6e5f60308ad121065539febf66c9dd436b4e486adba')
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            vkbot = VKBot(event.user_id)
            write_msg(event.user_id, vkbot.messages_send(event.text))
            print(event.text)

