from random import *

rand_num = randint(1, 100)


print('Добро пожаловать в числовую угадайку, иии начинай (:')


def is_valid(n):
    return 1 <= n <= 100


def search_rand_num():
    counter = 0
    while True:
        check_num = int(input())
        if not is_valid(check_num):
            print('А может быть все-таки введем целое число от 1 до 100?')
            counter += 1
            continue
        else:
            if check_num < rand_num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter += 1
                continue
            elif check_num > rand_num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                counter += 1
                continue
            else:
                print('Вы угадали число с', counter, 'попытки, поздравляем!')
                break


flag = True
while flag:
    search_rand_num()
    again = input('Еще раз? (:').capitalize()
    if again == 'Нет':
        flag = False

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
