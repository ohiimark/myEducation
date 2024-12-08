n, x, y, a, b = map(lambda i: int(i), input().split())

malist = list(range(1, n+1))


def swap(test_list, a, b):
    cut = test_list[a-1:b][::-1]
    return test_list[:a-1] + cut + test_list[b:]


malist = swap(malist, x, y)
malist = swap(malist, a, b)

print(*malist)


# https://stepik.org/lesson/569749/step/3?unit=564263
