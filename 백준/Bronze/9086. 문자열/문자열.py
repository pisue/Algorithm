n = int(input())

for _ in range(n):
    s = input()
    first_char = s[0]
    last_char = s[len(s)-1]
    print(f"{first_char}{last_char}")