import Movie


class FictionFilm(Movie):  # Класс для описания игрового фильма.

    def __init__(self, input_string):  # Конструктор, ссылающийся на конструктор базового класса
        Movie.__init__(self, input_string)
        self.director = input_string.split(sep=' ')[2]  # Признак альтернативы игрового фильма - режиссер.

    def to_string(self):  # Переопределенный метод для получения строкового представления объекта типа FictionFilm.
        return 'Fiction film: name - {}, year of release - {}, director - {}'.format(self.name,
                                                                                     self.year, self.director)
