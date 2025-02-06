n = int(input())
d_list = list(map(int, input().split()))
d_list.sort()

print(d_list[0]*d_list[-1])