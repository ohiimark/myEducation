from random import *

# функция, проверяющая пароль на соответстиве критериям


def generate_password(pswd, length):
    flag = True

    while flag:
        check_list_generate_password = [0, 0, 0, 0]
        new_pswd = sample(pswd, length)

        for i in new_pswd:
            # проверка наличия цифр
            if digOn == 'y' and i in DIGITS:
                check_list_generate_password[0] = 1
            # если i не цифра, то проверка верхних регистров
            elif ABCon == 'y' and i in UPPERCASE_LETTERS:
                check_list_generate_password[1] = 1
            # если i не цифра и не верхний регистр
            elif abcOn == 'y' and i in LOWERCASE_LETTERS:
                check_list_generate_password[2] = 1
            # если i не..., а знак
            elif chOn == 'y' and i in PUNCTUATION:
                check_list_generate_password[3] = 1
        if check_list_generate_password == check_list:
            break

    return new_pswd


cntPw = int(input('Укажите количество паролей для генерации: '))
lenPw = int(input('Укажите длину одного пароля: '))

digOn = input('Включать ли цифры 0123456789? (y/n) ')
DIGITS = '0123456789'

ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
PUNCTUATION = '!#$%&*+-=?@^_'

excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')

chars = ''
res_chars = ''
check_list = [0, 0, 0, 0]

if digOn == 'y':
    chars += DIGITS
    check_list[0] = 1
if ABCon == 'y':
    chars += UPPERCASE_LETTERS
    check_list[1] = 1
if abcOn == 'y':
    chars += LOWERCASE_LETTERS
    check_list[2] = 1
if chOn == 'y':
    chars += PUNCTUATION
    check_list[3] = 1
if excOn == 'y':
    for i in chars:
        if i not in 'il1Lo0O':
            res_chars += i
else:
    res_chars += chars

print('Пароли, удовлетворяющие вашим критериям:')
for i in range(cntPw):
    print((i+1), '. ', *generate_password(res_chars, lenPw), sep='')
