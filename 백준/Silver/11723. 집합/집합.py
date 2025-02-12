import sys
input = sys.stdin.readline

def fun(s, arr):
    if s.startswith("all"):
        return set(range(1, 21))
    elif s.startswith("empty"):
        return set()
    else:
        a, b = s.split()
        n = int(b)
        if s.startswith("add"):
            arr.add(n)
        elif s.startswith("remove"):
            arr.discard(n) # 없는 원소 삭제 시 에러 방지
        elif s.startswith("check"):
            print(1 if n in arr else 0)
        elif s.startswith("toggle"):
            if n in arr:
                arr.remove(n)    
            else: 
                arr.add(n)
    return arr
            
# 수행해야 하는 연산의 수 M
m = int(input())
x_set = set() # 리스트 보다 `set`이 시간복잡도가 더 효율적이다

for _ in range(m):
    x_set = fun(input(), x_set)
            