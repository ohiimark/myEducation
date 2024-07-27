# функция, которая кодирует слово
def encryption(text):
    return ([((i), chr(ord((VR, NR)[i.islower()]) + (ord(i) -
                                                     ord((VR, NR)[i.islower()]) + rot) % LANG))[i.isalpha()] for i in text])

# длина алфавита, буквы верхнего и нижнего регистров англ алфавита
LANG = 26
VR = 'A'
NR = 'a'

# ввожу сообщение и сразу строку перевожу в список
text = input().split()

new_list = list()
for i in text:
    counter = 0

    for j in i:
        if j.isalpha():
            counter += 1
    
    # смещение алфавита
    rot = counter

    # для каждого слова вызываем функцию кодировки и добавляем новое слово в общий финальный массив
    new_list.append(encryption(i))

# просто приводил финальный результат к нужному виду
new_list_2 = list()
for i in new_list:
    new_list_2.append(''.join(i))

print(*new_list_2)
