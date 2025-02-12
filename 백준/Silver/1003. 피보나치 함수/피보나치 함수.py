def fib(N):
    zeros = [1,0,1] # 0이 출력되는 횟수 리스트 (초기값: fib(0) = (1,0), fib(1) = (0,1), fib(2) = (1,1))
    ones = [0,1,1] # 1이 출력되는 횟수 리스트 (초기값 동일)
    
    if N >= 3:
        for i in range(2,N):
            zeros.append(zeros[i-1] + zeros[i]) # 이전 두 개의 0 출력 횟수를 더함
            ones.append(ones[i-1] + ones[i]) # 이전 두 개의 1 출력 횟수를 더함
    print(f"{zeros[N]} {ones[N]}")

T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)