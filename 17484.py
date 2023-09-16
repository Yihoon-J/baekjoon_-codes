# 샘플 케이스는 맞는데 틀린 코드라고 한다...
n, m=map(int, input().split())
space=[list(map(int, input().split())) for _ in range(n)]
inf=1e7
dp=[[[inf]*3 for _ in range(m)] for _ in range(n)]
#0,1,2 각각 (좌측에서 온 경우, 중앙에서 온 경우, 우측에서 온 경우)
for y in range(n):
    if y==0: #첫 행인 경우
        for x in range(m):
            for d in range(3): #세 방향 모두 그냥 원래 연료값 그대로 넣으면 됨
                dp[y][x][d]=space[y][x]
                
    else: #그 뒤로 쭉
        for x in range(m):
            if x==0: #제일 왼쪽이면, 좌측에서 올 수 없다
                dp[y][x][2]=min(dp[y-1][x+1][0], dp[y-1][x+1][1])+space[y][x] #우측에서 온 경우
                dp[y][x][1]=dp[y-1][x][2]+space[y][x] #중앙에서 온 경우
            elif x==m-1: #제일 우측이면, 우측에서 올 수 없다
                dp[y][x][0]=min(dp[y-1][x-1][1], dp[y-1][x-1][2])+space[y][x] #좌측에서 온 경우
                dp[y][x][1]=dp[y-1][x][0]+space[y][x] #중앙에서 온 경우
            else: #나머지 케이스들
                dp[y][x][0]=min(dp[y-1][x-1][1], dp[y-1][x-1][2])+space[y][x]
                dp[y][x][1]=min(dp[y-1][x][0], dp[y-1][x][2])+space[y][x]
                dp[y][x][2]=min(dp[y-1][x+1][0], dp[y-1][x+1][2])+space[y][x]

#결과 출력: 마지막 행의 매 x마다 최솟값을 확인    
answer=inf+1
for x in range(m):
    answer=min(min(dp[n-1][x]),answer)
        
print(answer)