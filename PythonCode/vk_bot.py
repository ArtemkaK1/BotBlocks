import requests
import bs4

class VKBot:
    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self.get_username(user_id)

        self._COMMANDS = ['начать', 'выпить кофе', 'перекусить', 'покушать', 'поработать']


    def get_username(self, user_id):
        request = requests.get('https://vk.com/id'+str(user_id))
        bs = bs4.BeautifulSoup(request.text, 'html.parser')
        username = self.clean_tags(bs.findAll('title')[0])
        return username.split()[0]


    @staticmethod
    def clean_tags(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

    def messages_send(self, message):
        if message.lower() == self._COMMANDS[0]:
            return f'Привет, {self._USERNAME}! Расскажи мне, что ты хочешь: выпить кофе, перекусить, хорошенько поесть или, может быть, поработать?\n\nНапиши мне "Еще", чтобы узнать о всех моих возможностях)'

        if message.lower() == self._COMMANDS[1]:
            return 'Отлично, чтобы подобрать тебе классную кофейню, скажи, сколько денег ты готов потратить: 100, 250 или 400 рублей?'

        if message.lower() == self._COMMANDS[2]:
            return 'Я знаю много разных забегаловок, чтобы выбрать идеальную для тебя скажи мне, сколько у тебя денег на все про все: 200-300, 300-500 рублей или больше?'

        if message.lower() == self._COMMANDS[3]:
            return 'Расскажи мне о своем бюджете, чтобы я мог выбрать для тебя идеальное кафе или ресторан за приятные деньги'

        if message.lower() == self._COMMANDS[4]:
            return 'Сколько ты готов потратить на комфотрное и приятное место для работы?'

        