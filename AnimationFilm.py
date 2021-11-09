import Movie


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

