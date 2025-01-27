from collections import deque

# 테스트 케이스의 수를 받는다
t = int(input())

for _ in range(t):
    # 문서의 개수 n과 순서를 알고자 하는 문서의 인덱스 m을 받는다
    n, m = map(int, input().split())
    
    # 중요도가 적힌 값들을 imp_nums 리스트에 담는다
    imp_nums = deque(map(int, input().split()))
    
    # 문서의 인덱스를 저장하는 큐를 생성
    idx_queue = deque(range(n))
    
    # 인쇄 순서
    doc_ord = 0
    
    while imp_nums:
        # 현재 문서의 중요도와 인덱스를 꺼냄
        current_imp = imp_nums.popleft()
        current_idx = idx_queue.popleft()
        
        # 현재 문서의 중요도가 큐에 남아있는 문서들 중 가장 높은 중요도인지 확인
        if any(current_imp < imp for imp in imp_nums):
            # 가장 높은 중요도가 아니라면 큐의 맨 뒤로 보냄
            imp_nums.append(current_imp)
            idx_queue.append(current_idx)
        else:
            # 가장 높은 중요도라면 인쇄
            doc_ord += 1
            if current_idx == m:
                print(doc_ord)
                break