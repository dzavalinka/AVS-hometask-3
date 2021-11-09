import string
import random
from random import randint



def generate_random_test(ostream):
    key = randint(1,3)
    ostream.write('{}'.format(key))
    ostream.write('\n')
    name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=randint(4,15)))
    year = randint(1895, 2022)
    if(key == 1):
        unique_param = ''.join(random.choices(string.ascii_uppercase, k=randint(4,15)))
    elif(key == 2):
        unique_param = randint(1,3)
    elif(key == 3):
        unique_param = randint(5, 240)
    ostream.write('{} {} {}\n'.format(name, year, unique_param))

if __name__ == '__main__':
    output_file = open('input4.txt', 'w')  # Задаем имя выходного файла.
    for i in range (1, 100):  # Задаем количество элементов в контейнере.
        generate_random_test(output_file)
    output_file.close()