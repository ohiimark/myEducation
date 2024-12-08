from string import digits, ascii_letters

# функция, отделяющая имя пользователя


def nick(test):
    pre_nickname = test[:test.index('@')]
    return pre_nickname.strip(digits)

# функция, возвращающая номер


def num_nick(test):
    pre_nickname = test[:test.index('@')].replace('-', '')
    return int(pre_nickname.strip(ascii_letters)) if pre_nickname.strip(ascii_letters) else 0

# функция, добавляющая почту в реестр


def true_add(test):
    name_glossari[nick(test)] = name_glossari.get(nick(test), [])
    name_glossari[nick(test)].append(num_nick(test))
    name_glossari[nick(test)].sort()

# функция, возвращающая НОВЫЙ номер почты


def current_num(test):
    num_list = name_glossari[test]
    # если в начальный список был добавлен базовый ник без номера, то следующий будет 1
    if len(num_list) == 1 and num_list[-1] == 0:
        name_glossari[test].append(1)
        return num_list[-1]
    # ситуация когда например [0, 2, 3]
    elif num_list != list(range(num_list[-1]+1)):
        for i in range(num_list[-1]+1):
            if i not in num_list:
                name_glossari[test].append(i)
                name_glossari[test].sort()
                return i
    else:
        name_glossari[test].append(num_list[-1]+1)
        return num_list[-1]


name_glossari = {}
creat_nickname = []

# вводим базовый список почты
for _ in range(int(input())):
    mail = input()
    true_add(mail)

# собираем новые никнеймы
for _ in range(int(input())):
    mail = input()
    if mail not in name_glossari.keys():
        name_glossari[mail] = [0]
        creat_nickname.append(mail+'@beegeek.bzz')
        continue
    new_num = current_num(mail)
    if new_num:
        creat_nickname.append(mail+str(new_num)+'@beegeek.bzz')
    else:
        creat_nickname.append(mail+'@beegeek.bzz')


print(*creat_nickname, sep='\n')
print('=====')
print(name_glossari)
