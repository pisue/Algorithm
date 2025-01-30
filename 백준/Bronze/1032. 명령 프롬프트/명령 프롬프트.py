n = int(input())
d_list = []

for i in range(n):
    d = input()
    if i == 0:
        d_list = list(d)
    else:
        idx = 0
        for char in d:
            if d_list[idx] != char:
                d_list[idx] = "?"
            idx += 1

print(''.join(d_list))