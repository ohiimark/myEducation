def get_biggest(numbers):
    if not numbers:
        return -1

    else:
        loc_numbers_str = list(map(str, numbers))
        max_len_el = max(map(lambda x: len(x), loc_numbers_str))

        loc_numbers_sorted = sorted(loc_numbers_str, key=lambda x: str(
            x)*max_len_el if len(str(x)) <= max_len_el else str(x), reverse=True)

        return int(''.join(loc_numbers_sorted))


print(get_biggest([123, 33, 4, 43]))
