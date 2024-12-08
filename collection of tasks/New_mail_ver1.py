base_list = set(input().split('@')[0] for _ in range(int(input())))
example_list = list(input() for _ in range(int(input())))

for i in range(len(example_list)):
    n = 1

    pre_name = example_list[i][::]
    while pre_name in base_list:
        pre_name = example_list[i] + str(n)
        n += 1
    base_list.add(pre_name)
    example_list[i] = pre_name

example_list = list(map(lambda i: f'{i}@beegeek.bzz', example_list))

print(*example_list, sep='\n')
