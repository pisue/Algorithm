def rev(input_str):
    return input_str[::-1]

a, b = map(str, input().split())

print(int(rev(str(int(rev(a))+int(rev(b))))))