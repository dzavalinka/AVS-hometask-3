import enum
import sys
import Movie
import FictionFilm
import AnimationFilm
import Documentary


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
