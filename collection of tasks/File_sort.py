

# функция пересчета памяти в байты
def tranc(list):
    size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
    for i in range(len(list)):
        list[i][0] = int(list[i][0])*size_file[list[i][1]]
        list[i][1] = 'B'

# функция сбора файлов по расширениям


def group_extension(list):
    extension_dict = {}
    for name in list:
        extension_dict[name.split(
            '.')[-1]] = extension_dict.get(name.split('.')[-1], [])
        extension_dict[name.split('.')[-1]].append(name)
    return extension_dict

# функция подсчета общей памяти файлов
# dict1 - РАСШИРЕНИЕ: СПИСОК ФАЙЛОВ
# dict2 - ИМЯ_ФАЙЛА: САЙЗ


def size_sum(extension, dict1, dict2):
    size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
    summary_byte = 0

    ext_name = list(size_file.keys())
    ext_mult = list(size_file.values())

    for name in dict1[extension]:
        summary_byte += dict2[name]

    mult_ind = 0
    for i in range(len(ext_mult)):
        if summary_byte/ext_mult[i] > 1:
            mult_ind = i
        else:
            break

    return f'{round(summary_byte/ext_mult[mult_ind])} {ext_name[mult_ind]}'


# читаем файл
with open(r"D:\myEducation\python\files.txt", 'r', encoding='utf-8') as fuck_list:
    name_list = list(map(lambda i: i.split()[0], fuck_list.readlines()))
    fuck_list.seek(0)
    size_list = list(map(lambda i: i.split()[1:], fuck_list.readlines()))
    tranc(size_list)


# собрали файл-словарь: ИМЯ_ФАЙЛА: САЙЗ
file_plus_size = dict(zip(name_list, map(lambda i: i[0], size_list)))

# собрали файл-словарь: РАСШИРЕНИЕ: СПИСОК ФАЙЛОВ
extension_plus_namelist = group_extension(name_list)
sorted_epn = dict(sorted(extension_plus_namelist.items()))

# вывод
for key, value in sorted_epn.items():
    print(*sorted(value), sep='\n')
    print('----------')
    print('Summary:', size_sum(key, sorted_epn, file_plus_size))
    print()


# https://stepik.org/lesson/569749/step/9?thread=solutions&unit=564263
