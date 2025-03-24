from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end = ' ')
    
    for next_node in sorted(graph[start]):
        if not visited[next_node]:
            dfs(graph, next_node, visited)
            
def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        print(node, end= ' ')
        
        for next_node in sorted(graph[node]):
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                

def main():
    # 입력 처리 (정점의 개수, 간선의 개수, 시작 정점)
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)
        
    # DFS와 BFS 수행
    visited_dfs = [False] * (N + 1)
    dfs(graph, V, visited_dfs)
    print() # 줄바꿈
    
    bfs(graph, V)

if __name__ == '__main__':
    main()