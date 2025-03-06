import sys
import heapq

input = sys.stdin.readline

def min_heap():
    n = int(input().strip())
    heap = []
    
    for _ in range(n):
        x = int(input().strip())
        if x == 0:
            if heap:
                print(heapq.heappop(heap)) # 최솟값 출력
            else:
                print(0) # 힙이 비어 있으면 0 출력
        else:
            heapq.heappush(heap, x) # x 추가

min_heap()
