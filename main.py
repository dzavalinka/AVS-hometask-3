import sys
from utils import utils

if __name__ == '__main__':
    if len(sys.argv) == 3:
        inputFileName = sys.argv[1]
        outputFileName = sys.argv[2]
    elif len(sys.argv) == 5:
        if sys.argv[1] == "random":
            outputFileName = sys.argv[4]
            inputFileName = sys.argv[3]
            output_file = open(inputFileName, 'w')  # Задаем имя выходного файла.
            if not sys.argv[2].isdigit():
                print("Incorrect command line! Check Readme file for more information.")
                exit()
            if sys.argv[2] == '0':
                print("Incorrect command line! Check Readme file for more information.")
                exit()
            for i in range(0, int(sys.argv[2])):  # Задаем количество элементов в контейнере.
                utils.generate_random_test(output_file)
            output_file.close()
    else:
        print("Incorrect command line! Check Readme file for more information.")
        exit()
    input_file = open(inputFileName)
    file_content = input_file.read()
    input_file.close()
    cont = utils.read_input(file_content)
    utils.insertion_sort(cont)
    output_file = open(outputFileName, 'w')
    utils.write_result(output_file, cont)
    output_file.close()
