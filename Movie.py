class Movie(object):  # Базовый класс для всех фильмов.

    def __init__(self, input_string):  # Конструктор, в строковом параметре
        # через пробел содержатся название фильма и год выпуска.
        self.name = input_string.split(sep=' ')[0]
        self.year = int(input_string.split(sep=' ')[1])

    def function(self):  # Функция общая для всех альтернатив.
        return self.year/len(self.name)

    def to_string(self):  # Абстрактный метод строкового представления объекта типа Movie.
        pass
