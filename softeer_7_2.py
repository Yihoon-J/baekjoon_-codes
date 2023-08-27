from collections import deque

def dfs(x,y, p, q):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
	if x<=-1 or x>=p or y<=-1 or y>=q:
		return False
	if graph[x][y]==0: #해당 위치가 0, 즉 아직 방문하지 않은 경우
		graph[x][y]=1 #해당 노드 방문 처리 - 원래 1인 것이랑 같은 처리 해준다.
		#해당 노드와 상하좌우 인접한 위치들을 재귀 호출
		dfs(x-1,y)
		dfs(x,y-1)
		dfs(x+1,y)
		dfs(x,y+1)
		return True #계속 수행할 수 있도록 True 리턴
	return False#완료 시 종료


n, m= map (int, input().split()) #n,m 입력

#그래프 모양 입력
graph=[]
for i in range(n):
 	graph.append(list(map(int,input()))) #2중 리스트 형태.
  
#방문해야 할 위치 입력
target=[]
for i in range(m):
    target.append(list(map, int,input().split()))
    

#모든 위치에 대해 음료수 채우기
result=0
for i in range(n):
	for j in range(m):
		#현재 위치에서 DFS 수행
		if dfs(i,j)==True:
			result+=1
print(result)













n, m=map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split()))) #인덱싱할 때 행, 열 순.
    
target=[]
for i in range(m):
    target.append(list(map, int,input().split()))

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]  
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
    
    
print(graph)