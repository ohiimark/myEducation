def choose_plural(amount, declensions):
    suffixes = {
        1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2,
        11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 0: 2,
    }

    last_num = suffixes.get(amount%100, suffixes.get(amount%10, 'Huy tebe :3'))
    

    return f'{amount} {declensions[last_num]}'


print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))