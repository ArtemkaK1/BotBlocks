import pymysql
import requests
import bs4
import uuid


class DbWork:
    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self.get_username(user_id)
        self._CONNECTION = self.get_connection()

        self._PLACES = ['cofix купон', 'one price coffee купон', 'surf coffee купон', 'starbucks купон', 'krispy kreme купон', 'хлеб насущный',
                        'subway купон', 'mcdonalds купон', 'kfc купон', 'burger king купон', 'му-му купон', 'хлеб насущный купон', 'bb & burgers купон',
                        'франклинс бургер купон',
                        'шоколадница купон', '#farш купон', 'шоколадница купон', 'grill crafted bar купон', 'чайхона №1 купон', 'вареничная купон',
                        'тануки купон',
                        'якитория купон', 'арбатский базар купон', 'джон джоли купон', 'депо купон']

    def get_username(self, user_id):
        request = requests.get('https://vk.com/id' + str(user_id))
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

    def get_connection(self):
        connection = pymysql.connect(
            user='root',
            password='root',
            host='localhost',
            db='placeadvisor',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        print('Соединение установлено')
        return connection

    def add_user(self, email):
        connection = self._CONNECTION
        cursor = connection.cursor()
        sql = 'INSERT INTO users (name, email) VALUES (%s, %s)'
        cursor.execute(sql, (self._USERNAME, email))
        connection.commit()
        connection.close()

    def select_coupon(self, place):
        connection = self._CONNECTION
        cursor = connection.cursor()
        sql = 'SELECT coupon FROM coupons WHERE place=%s'
        cursor.execute(sql, (place + ' купон',))
        result = cursor.fetchone()
        connection.close()
        return result['coupon']

    def add_coupons(self, place):
        connection = self._CONNECTION
        cursor = connection.cursor()
        sql = 'INSERT INTO coupons (place, coupon) VALUES (%s, %s)'
        cursor.execute(sql, (place, str(uuid.uuid4())))
        connection.commit()
        connection.close()

    def add_mark(self, placeMark):
        connection = self._CONNECTION
        cursor = connection.cursor()
        sql = 'INSERT INTO feedback (`place: mark`, name) VALUES (%s, %s)'
        cursor.execute(sql, (placeMark, self._USERNAME))
        connection.commit()
        connection.close()

    def add_description(self, place, description):
        connection = self._CONNECTION
        cursor = connection.cursor()
        sql = 'INSERT INTO aboutPlace (place, description) VALUES (%s, %s)'
        cursor.execute(sql, (place, description))
        connection.commit()
        connection.close()

    def add_menu(self, place, menu):
        connection = self._CONNECTION
        cursor = connection.cursor()
        sql = 'INSERT INTO aboutPlace (place, menu) VALUES (%s, %s)'
        cursor.execute(sql, (place, menu))
        connection.commit()
        connection.close()

    def sql_message(self, message):  # Сообщения о работе с базой данных

        # Создание скидочного купона (1 шт. за раз)
        if ('оценка' or '@' or 'описание' or 'меню' or 'получить' or 'создать') not in message.lower():
            for i in range(len(self._PLACES)):
                if self._PLACES[i] in message.lower():
                    return f'Я создал скидочный {message} купон.'

        # Внесение пользователя в базу данных

        if '@' in message.lower():
            return f'{self._USERNAME}, твое имя и адрес электронной почты ({message}) внесены мою базу данных.'

        # Получение купона из базы данных

        if 'оценка' in message.lower():
            return f'Спасибо, {self._USERNAME}, я записал твою оценку'


