import Movie


class Documentary(Movie):  # Класс для описания документального фильма, методы аналогичны классу FictionFilm.

    def __init__(self, input_string):
        Movie.__init__(self, input_string)
        self.length = input_string.split(sep=' ')[2]

    def to_string(self):
        return 'Documentary film: name - {}, year of release - {},' \
               ' duration - {}'.format(self.name, self.year, self.length)

