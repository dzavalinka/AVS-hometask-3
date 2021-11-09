import enum
import sys


class AnimationType(enum.Enum):  # Перечисление для представления признака альтернативы анимационного фильма.
    painted = 1
    puppet = 2
    plasticine = 3


class Movie(object):  # Базовый класс для всех фильмов.

    def __init__(self, input_string):  # Конструктор, в строковом параметре
        # через пробел содержатся название фильма и год выпуска.
        self.name = input_string.split(sep=' ')[0]
        self.year = int(input_string.split(sep=' ')[1])

    def function(self):  # Функция общая для всех альтернатив.
        return self.year/len(self.name)

    def to_string(self):  # Абстрактный метод строкового представления объекта типа Movie.
        pass


class FictionFilm(Movie):  # Класс для описания игрового фильма.

    def __init__(self, input_string):  # Конструктор, ссылающийся на конструктор базового класса
        Movie.__init__(self, input_string)
        self.director = input_string.split(sep=' ')[2]  # Признак альтернативы игрового фильма - режиссер.

    def to_string(self):  # Переопределенный метод для получения строкового представления объекта типа FictionFilm.
        return 'Fiction film: name - {}, year of release - {}, director - {}'.format(self.name,
                                                                                     self.year, self.director)


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


def read_input(input_string):  # Функция, которая по данным из входного файла создает контейнер и возвращает его.
    res = []
    lines = input_string.split('\n')
    counter = 0
    while counter < len(lines) - 1:
        line = lines[counter]
        key = int(line)
        if key == 1:  # Признак игрового фильма
            res.append(FictionFilm(lines[counter+1]))
        elif key == 2:  # Признак анимационного фильма
            res.append(AnimationFilm(lines[counter+1]))
        elif key == 3:  # Признак документального фильма
            res.append(Documentary(lines[counter+1]))
        else:
            print('Incorrect input')
            exit()
        counter += 2
    return res


def write_result(output_stream, container):  # Функция для записи содержимого контейнера в выходной файл.
    output_stream.write("Container stores {} movies:\n".format(len(container)))
    for movie in container:
        output_stream.write(movie.to_string())
        output_stream.write('\n')


def insertion_sort(container):  # Функция, сортирующая фильмы в контейнере прямым включением в обратном порядке.
    for i in range(1, len(container)):
        key = container[i]
        j = i-1
        while j >= 0 and key.function() < container[j].function():
            container[j + 1] = container[j]
            j -= 1
        container[j + 1] = key
    container.reverse()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Incorrect command line! You must write: python main <inputFileName> [<outputFileName>]")
        exit()
    else:
        if len(sys.argv) == 3:
            inputFileName = sys.argv[1]
            outputFileName = sys.argv[2]
        elif len(sys.argv) == 2:
            inputFileName = sys.argv[1]
            outputFileName = "output.txt"

        input_file = open(inputFileName)
        file_content = input_file.read()
        input_file.close()
        cont = read_input(file_content)
        insertion_sort(cont)
        output_file = open(outputFileName, 'w')
        write_result(output_file, cont)
        output_file.close()
