import requests
import bs4


class VKBot:
    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self.get_username(user_id)

        self._COMMANDS = ['начать', 'выпить кофе', 'перекусить', 'поесть', 'поработать', 'еще']
        self._COMMANDS_MORE = ['оставить оценку', 'авторизоваться', 'получить купоны']
        self._COMMANDS_AUTHORIZED = ['создать купон', 'добавить ассортимент', 'добавить информацию']
        self._COFFEE_PRICES = ['100 рублей', '250 рублей', '400 рублей']
        self._LUNCH_PRICES = ['200-300 рублей', '300-500 рублей', '500-700 рублей']
        self._REST_PRICES = ['600-800 рублей', '1000-1500 рублей', '2000+ рублей']
        self._WORK_PRICES = []
        self._LUNCH_TIME = ['10 минут', '20 минут', '30 минут']
        self._REST_TIME = ['45-60 минут', '90 минут', '120 минут']
        self._WORK_TIME = []
        self._MARKS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self._PLACES_M = ['cofix оценка', 'starbucks оценка', 'surf coffee оценка', 'krispy kreme оценка',
                          'хлеб насущный оценка', 'one price coffee оценка', 'subway оценка']
        self._PLACES_D = ['cofix описание', 'starbucks описание', 'surf coffee описание', 'krispy kreme описание',
                          'хлеб насущный описание', 'one price coffee описание', 'subway описание']

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

    def messages_send(self, message):

        if message.lower() == self._COMMANDS[0]:
            return f'Привет, {self._USERNAME}! Расскажи мне, что ты хочешь: выпить кофе, перекусить, хорошенько поесть или, может быть, поработать?\n\nНапиши мне "Еще", чтобы узнать о всех моих возможностях)'

        if message.lower() == self._COMMANDS[1]:
            return 'Отлично, чтобы подобрать тебе классную кофейню, скажи, сколько денег ты готов потратить: 100, 250 или 400 рублей?'

        if message.lower() == self._COMMANDS[2]:
            return 'Я знаю много разных забегаловок, чтобы выбрать идеальную для тебя скажи мне, сколько у тебя денег на все про все: 200-300, 300-500 или 500-700 рублей, также мне нужно чтобы ты сказал, сколько свободного времени у тебя есть?'

        if message.lower() == self._COMMANDS[3]:
            return 'Расскажи мне о своем бюджете, чтобы я мог выбрать для тебя идеальное кафе или ресторан за приятные деньги'

        if message.lower() == self._COMMANDS[4]:
            return 'Сколько ты готов потратить на комфотрное и приятное место для работы?'

        if message.lower() == self._COMMANDS[5]:
            return ("Помимо подбора места, ты можешь:\n\n"
                    "1. Получить скидочный купон, если у меня таковой имеется,\n"
                    "2. Оставить оценку заведения,\n"
                    "3. Если ты владелец заведения, то авторизоваться и добавить описание своего заведения и его ассортимент, а также создать скидочный купоны.")

        # Оценка заведения
        if message.lower() == self._COMMANDS_MORE[0]:
            return ('Чтобы оставить оценку о посещененном заведении, ввесообщение в формате'
                    ' "<Название заведения>, оценка <оценка от 1 до 10>"')

        # Авторизация
        if message.lower() == self._COMMANDS_MORE[1]:
            return 'Напиши мне свой E-mail адрес'

        # Получение купона
        if message.lower() == self._COMMANDS_MORE[2]:
            return 'Введи название заведения, для которого хочешь получить купоны'

        # Создание купонов
        if message.lower() == self._COMMANDS_AUTHORIZED[0]:
            return 'Введи название своего заведеня, для которого надо создать купон на скидку + слово купон'

        # Добавить меню
        if message.lower() == self._COMMANDS_AUTHORIZED[1]:
            return 'Введи название своего заведения + слово меню, а затем его меню'

        # Добавить описание
        if message.lower() == self._COMMANDS_AUTHORIZED[2]:
            return 'Введи название своего заведения + слово описание, а затем его описание'

        # Кофе - сообщения

        if message.lower() == self._COFFEE_PRICES[0]:
            return ("Предлагаю тебе сходить в Cofix, вот ссылка на сайт кофейни:\n https://www.cofix.ru\n\n"
                    "Предлагаю тебе сходить в One Price Coffee, вот ссылка на сайт кофейни:\n https://onepricecoffee.com\n\n")

        if message.lower() == self._COFFEE_PRICES[1]:
            return ("Предлагаю тебе сходить в Surf Coffee, вот ссыдка на сайт кофейни:\n https://www.surfcoffee.ru\n\n"
                    "Предлагаю тебе сходить в Krispy Kreme, вот ссылка на сайт кафе:\n https://www.krispykremerussia.ru\n\n")

        if message.lower() == self._COFFEE_PRICES[2]:
            return ("Предлагаю тебе сходить в Starbucks, вот ссылка на сайт кофейни:\n https://www.starbucks.ru\n\n"
                    "Предлагаю тебе сходить в Хлеб Насущный, вот ссылка на сайт пекарни:\n https://hlebnasushny.ru\n\n")

        # Перекус - сообщения

        if self._LUNCH_PRICES[0] in message.lower() and self._LUNCH_TIME[0] in message.lower():
            return (
                f"Предлагаю тебе сходить в Subway, но имея в запасе только {self._LUNCH_TIME[0]}, ты сможешь взять заказ только с собой \n"
                f"Вот ссылка на сайт фастфуда: https://subway.ru\n\n"
                f"Также ты можешь зайти в пиццерию Додо пицца и взять с собой кусочки пиццы, во ссыдка на сайт заведения:\n"
                f"https://dodopizza.ru")

        if (self._LUNCH_PRICES[0] and self._LUNCH_TIME[1]) in message.lower():
            return (f"Предлагаю тебе за {self._LUNCH_TIME[1]} сходить в один из известных мировых фастфудов:"
                    f" KFC, Burger King, Mcdonalds, вот ссылки на сайты заведений:\n"
                    f"KFC: https://www.kfc.ru \n"
                    f"Burger King: https://burgerking.ru \n"
                    f"Mcdonalds: https://mcdonalds.ru/")

        if (self._LUNCH_PRICES[0] and self._LUNCH_TIME[2]) in message.lower():
            return (f"Раз у тебя есть {self._LUNCH_TIME[2]}, то ты можешь сходить перекурисить в МУ-МУ,"
                    f" за сравнительно небольшую сумму в {self._LUNCH_PRICES[0]} ты получишь комплексный обед или ужин,"
                    f" что гораздо лучше фастфуда, вот ссылка на сайт заведения:\n"
                    f"https://www.cafemumu.ru")

        if (self._LUNCH_PRICES[1] and self._LUNCH_TIME[0]) in message.lower():
            return (f"Сложно куда-то успеть, имея всего {self._LUNCH_TIME[0]} в запасе,"
                    f" тем не менее ты можешь заскочить в Хлеб Насущный и взять с собой сэндвич и кофе,"
                    f" что будет отличным перекусом, вот ссылка на сайт пекарни:\n"
                    f"https://hlebnasushny.ru")

        if (self._LUNCH_PRICES[1] in message.lower()) and (self._LUNCH_TIME[1] in message.lower()):
            return (
                f"Имея и у тебя достатосно большой выбор, но могу посоветовать сходить в BB & Burgers или Франклинс бургер,"
                f" это отличные бургерные, где ты сможешь вкусно и быстро перекусить, также их достаточно много по всей Москве, вот ссылки на сайты заведений:\n"
                f"https://www.franklins.ru\n"
                f"https://bbburgers.ru\n")

        if (self._LUNCH_PRICES[1] and self._LUNCH_TIME[2]) in message.lower():
            return (f'Имея {self._LUNCH_TIME[2]} отличным выбором станет кофейня Шоколодадница.'
                    f' Не смотря на то что это кофейня там можно вкусно и относительно недорого покушать,'
                    f' но за твою сумму можно взять только бизнес-ланч.'
                    f' Вот ссылка на сайт кофени:\nhttps://shoko.ru')

        if (self._LUNCH_PRICES[2] and self._LUNCH_TIME[0]) in message.lower():
            return (f'Извини, но по заданным параметрам я не могу подобрать тебе заведение :(\n'
                    f'Попробуй еще раз, изменив один из параметров.')

        if (self._LUNCH_PRICES[2] and self._LUNCH_TIME[1]) in message.lower():
            return (
                f'Имея {self._LUNCH_PRICES[2]} и {self._LUNCH_TIME[1]} ты можешь сходить в фаст-фуд ресторан Pizza Hut,'
                f' известный по всей Европе, основной кухней является итальянская, но также есть и блюда из стрит фуд меню других стран'
                f'Вот ссылка на сайт заведения:\nhttps://pizzahut.ru')

        if (self._LUNCH_PRICES[2] and self._LUNCH_TIME[2]) in message.lower():
            return (
                f'За {self._LUNCH_PRICES[2]} и {self._LUNCH_TIME[2]} отличным быром станет бар-ресторан американской кухни #FАRШ'
                f' Вот ссылка на сайт ресторана:\nhttps://farshburger.ru')

        # Рестораны - сообщения

        if (self._REST_PRICES[0] and self._REST_TIME[0]) in message.lower():
            return (f'Имея {self._REST_PRICES[0]} и {self._REST_TIME[0]} отличным выбором станет кофейня Шоколодадница.'
                    f' Не смотря на то что это кофейня там можно вкусно и относительно недорого покушать,'
                    f' а еще там очень быстро готовят, что позволит сэконить время.'
                    f' Вот ссылка на сайт кофени:\nhttps://shoko.ru')

        if (self._REST_PRICES[0] and self._REST_TIME[1]) in message.lower():
            return (f'Имея {self._REST_PRICES[0]} и {self._REST_TIME[1]} ты можешь сходить в ресторан-бургерную'
                    f' GRILL CRAFTED BAR. Вот ссылка на сайт заведения: https://www.crafted-grillbar.ru')

        if (self._REST_PRICES[0] and self._REST_TIME[2]) in message.lower():
            return (f'Извини, но по заданным параметрам я не могу подобрать тебе заведение :(\n'
                    f'Попробуй еще раз, изменив один из параметров.')

        if (self._REST_PRICES[1] and self._REST_TIME[0]) in message.lower():
            return (
                f'Имея {self._REST_PRICES[1]} и {self._REST_TIME[0]} ты можешь сходить в рестрон восточной кухни Чайхопа №1.'
                f'Вот ссылка на сайт ресторана:\nhttps://chaihona1.ru')

        if (self._REST_PRICES[1] and self._REST_TIME[1]) in message.lower():
            return (
                f'Имея {self._REST_PRICES[1]} и {self._REST_TIME[1]} предлагаю тебе сходить в ресторан традиционнной русской'
                f' кухни под названием Вареничная. '
                f'Вот ссылка на сайт ресторана:\nhttp://varenichnaya.ru')

        if (self._REST_PRICES[1] and self._REST_TIME[2]) in message.lower():
            return (f'За {self._REST_PRICES[1]} и {self._REST_TIME[2]} ты можешь сходить в один из известных ресторанов'
                    f' японской кухни: Тануки и Якитория. Вот ссылки на сайты заведений:\n'
                    f'https://www.tanuki.ru\n'
                    f'https://yakitoriya.ru')

        if (self._REST_PRICES[2] and self._REST_TIME[0]) in message.lower():
            return (f'Имея {self._REST_PRICES[2]} и {self._REST_TIME[1]} ты можешь сходить'
                    f' в шикарный ресторан "Арбатский базар" около метро Смоленская.\n'
                    f'Вот ссылка на сайт ресторана:\nhttp://www.arbatskiybazar.ru')

        if (self._REST_PRICES[2] and self._REST_TIME[1]) in message.lower():
            return (f'Имея {self._REST_PRICES[2]} и {self._REST_TIME[1]} ты можешь сходить в ресторан'
                    f' грузинской кухни Джон Джоли. Вот ссылка на сайт сети ресторанов:\nhttps://ch1ef.ru/restaurant/jonjoli')

        if (self._REST_PRICES[2] and self._REST_TIME[2]) in message.lower():
            return (f'Имея {self._REST_PRICES[2]} и {self._REST_TIME[2]} ты можещь сходить в шикарное место'
                    f' - фудмолл "Депо" около метро Белорусская, там ты можешь попробовать кухню разных стран. '
                    f'Вот ссылка на сайт заведения:\nhttps://depomoscow.ru')

        else:
            return f"Прости, {self._USERNAME}, но я тебя не понимаю("
