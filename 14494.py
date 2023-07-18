n, m=map(int, input().split())

res=[[0]*(m+1)]*(n+1)
res[1][1]=1

for x in range(1,n+1):
    for y in range(1, m+1):
        if x==1 and y==1:
            continue
        res[x][y]=res[x-1][y]+res[x][y-1]+res[x-1][y-1]

print(res[n][m]%1000000007)