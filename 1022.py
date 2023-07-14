a,x,b,y=map(int,input().split())
U=[] #전체 출력될 박스

for i in range(a,b+1):
    u=[]
    U+=[u]
    
    for j in range(x,y+1):
        k=2*max(-i,i,-j,j)
        u+=[1+k*k+(-1)**(i<j)*(i+j+k)]
        print(k)
        print(u)
        
for z in U:
    print(*[f"%{len(str(max(U[0]+u)))}d"%i for i in z])
    

# easy code but out of memory...
# import sys

# def solution():
#     r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     tornado = [[0] * (abs(c2-c1)+1) for _ in range(abs(r2-r1)+1)]
#     x, y = 0, 0
#     dir = 3
#     dcnt, num = 1, 1
#     cnt = 0
#     while tornado[0][0] == 0 or tornado[0][c2-c1] == 0 or tornado[r2-r1][0] == 0 or tornado[r2-r1][c2-c1] == 0:
#         if x - r1 >= 0 and x - r1 <= (r2-r1) and y - c1 >= 0 and y - c1 <= (c2-c1):
#             tornado[x-r1][y-c1] = num
#         num += 1
#         cnt += 1
#         x = x + dx[dir]
#         y = y + dy[dir]
#         if cnt == dcnt:
#             cnt = 0
#             dir = (dir+1) % 4
#             if dir == 3 or dir == 1:
#                 dcnt += 1
#     cnt = len(str(num))
#     for i in range(r2-r1+1):
#         for j in range(c2-c1+1):
#             if j == c2 - c1:
#                 print(f"%{cnt}d"%tornado[i][j], end="\n")
#             else:
#                 print(f"%{cnt}d"%tornado[i][j], end=" ")


# if __name__ == "__main__":
#     solution()