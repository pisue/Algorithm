n = int(input())
def new_n(nn, cnt):
    if n == nn and cnt > 0:
        print(cnt)
    elif nn < 10:
        new_n(10*nn+nn, cnt+1)
    else:
        new_n((nn%10)*10+((nn//10 + nn%10)%10), cnt+1)
new_n(n, 0)