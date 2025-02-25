import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)
h = 0;
while low <= high:
    mid = (low + high) // 2
    cut_tree = sum(tree - mid for tree in trees if tree > mid)
            
    if cut_tree >= m:
        h = mid
        low = mid + 1
    else:
        high = mid - 1
        
print(h)

