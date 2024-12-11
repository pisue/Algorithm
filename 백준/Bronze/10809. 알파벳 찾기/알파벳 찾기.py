alp = [-1] * 26
s = input()
cnt = 0
for char in s:
    idx = ord(char) - ord('a')
    if alp[idx] == -1:
        alp[idx] = cnt
    cnt += 1

print(" ".join(map(str, alp)))