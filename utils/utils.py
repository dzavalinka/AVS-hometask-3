import string
import random
from random import randint
from movies import Movie


def read_input(input_string):  # Функция, которая по данным из входного файла создает контейнер и возвращает его.
    res = []
    lines = input_string.split('\n')
    counter = 0
    while counter < len(lines)-1:
        line = lines[counter]
        key = int(line.split(sep=' ')[0])
        if key == 1:  # Признак игрового фильма
            res.append(Movie.FictionFilm(lines[counter]))
        elif key == 2:  # Признак анимационного фильма
            res.append(Movie.AnimationFilm(lines[counter]))
        elif key == 3:  # Признак документального фильма
            res.append(Movie.Documentary(lines[counter]))
        else:
            print('Incorrect input')
            exit()
        counter += 1
    return res


def write_result(output_stream, container):  # Функция для записи содержимого контейнера в выходной файл.
    output_stream.write("Container stores {} movies:\n".format(len(container)))
    for movie in container:
        output_stream.write(movie.to_string())
        output_stream.write('\n')


def insertion_sort(container):  # Функция, сортирующая фильмы в контейнере прямым включением в обратном порядке.
    for k in range(1, len(container)):
        key = container[k]
        j = k - 1
        while j >= 0 and key.function() > container[j].function():
            container[j + 1] = container[j]
            j -= 1
        container[j + 1] = key
    container.reverse()


def generate_random_test(ostream):
    key = randint(1, 3)
    ostream.write('{}'.format(key))
    ostream.write(' ')
    name = ''.join(
        random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=randint(4, 15)))
    year = randint(1895, 2022)
    unique_param = 0
    if key == 1:
        unique_param = ''.join(random.choices(string.ascii_uppercase, k=randint(4, 15)))
    elif key == 2:
        unique_param = randint(1, 3)
    elif key == 3:
        unique_param = randint(5, 240)
    ostream.write('{} {} {}\n'.format(name, year, unique_param))
