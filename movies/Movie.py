import enum


class Movie(object):  # Базовый класс для всех фильмов.

    def __init__(self, input_string):  # Конструктор, в строковом параметре
        # через пробел содержатся название фильма и год выпуска.
        self.name = input_string.split(sep=' ')[0]
        self.year = int(input_string.split(sep=' ')[1])

    def function(self):  # Функция общая для всех альтернатив.
        return self.year / len(self.name)

    def to_string(self):  # Абстрактный метод строкового представления объекта типа Movie.
        pass


class AnimationType(enum.Enum):  # Перечисление для представления признака альтернативы анимационного фильма.
    painted = 1
    puppet = 2
    plasticine = 3


class AnimationFilm(Movie):  # Класс для описания анимационного фильма, методы аналогичны предыдущему классу.

    def __init__(self, input_string):
        Movie.__init__(self, input_string)
        self.animation_type = AnimationType(int(input_string.split(sep=' ')[2])).name

    def to_string(self):
        return 'Animation film: name - {}, year of release - {}, ' \
               'animation type - {}'.format(self.name, self.year, self.animation_type)


class Documentary(Movie):  # Класс для описания документального фильма, методы аналогичны классу FictionFilm.

    def __init__(self, input_string):
        Movie.__init__(self, input_string)
        self.length = input_string.split(sep=' ')[2]

    def to_string(self):
        return 'Documentary film: name - {}, year of release - {},' \
               ' duration - {}'.format(self.name, self.year, self.length)


class FictionFilm(Movie):  # Класс для описания игрового фильма.

    def __init__(self, input_string):  # Конструктор, ссылающийся на конструктор базового класса
        Movie.__init__(self, input_string)
        self.director = input_string.split(sep=' ')[2]  # Признак альтернативы игрового фильма - режиссер.

    def to_string(self):  # Переопределенный метод для получения строкового представления объекта типа FictionFilm.
        return 'Fiction film: name - {}, year of release - {}, director - {}'.format(self.name,
                                                                                     self.year, self.director)
