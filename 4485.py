n=int(input())
grid=[]
for n in range(n):
    grid.append(list(map(int, input().split())))
visited=[[False]*(n+1)]*(n+1)
        
xpos=0
ypos=0
rupee=grid[ypos][xpos] #열-행 순 인덱싱
visited[xpos][ypos]=True #시작점 방문처리

    
#down as default
def get_min_dir(x, y, grid, visited):
    nx=0
    ny=0
    rupee_min=126
    rupee_temp=grid[y+1][x] if y<n-1 and visited[y+1][x]==False else 126
    if rupee_min>rupee_temp:
        rupee_min=rupee_temp
        nx=x
        ny=y+1
    rupee_temp=grid[y-1][x] if y>0 and visited[y-1][x]==False else 126
    if rupee_min>rupee_temp:
        rupee_min=rupee_temp
        nx=x
        ny=y-1
    rupee_temp=grid[y][x+1] if x<n-1 and visited[y][x+1]==False else 126
    if rupee_min>rupee_temp:
        rupee_min=rupee_temp3
        nx=x+1
        ny=y
    rupee_temp=grid[y][x-1] if x>0 and visited[y][x-1]==False else 126
    if rupee_min>rupee_temp:
        rupee_min=rupee_temp
        nx=x-1
        ny=y
    visited[ny][nx]==True
    return nx, ny, visited, grid[ny][nx]

while xpos<n and ypos<n:
    xpos, ypos, visited, add = get_min_dir(xpos, ypos, visited, grid)
    print(xpos,ypos)
    rupee+=add

print(rupee)