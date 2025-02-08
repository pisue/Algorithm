n = int(input())
call_time_list = list(map(int, input().split()))

Y_price = 0
M_price = 0
for call_time in call_time_list:
    Y_price += (call_time // 30)*10 + 10 # 영식 요금제로 계산
    M_price += (call_time // 60)*15 + 15 # 민식 요금제로 계산
if Y_price < M_price:
    print("Y",Y_price)
elif M_price < Y_price:
    print("M",M_price)
else: print("Y M", Y_price)