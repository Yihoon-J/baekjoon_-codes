
# 못풀었다...



#N: 가로등 개수
#M: 초기/현재 위치
#D: 각 가로등 위치
#W: 각 가로등 소모량

N, M= map(int, input().split())
Ds=[]
Ws=[]
for _ in range(N):
    D, W=map(int, input().split())
    Ds.append(W)
    Ws.append(W)
Ds[M-2]=0 #시작 위치 0으로
watt=0

#좌 우 비교
for d in Ds:
    Ds[i]=Ds[i]-M


# lights=[0]*1000
# for k in range(N):
#     D,W= map(int, input().split())
#     if k!=M-1: 
#         lights[D]=W #처음 자기 위치는 바로 0으로 만들고 시작
#     else:
#         M=D #가로등 번호를 위치로 변환
# watt=0 #소모량 카운트

# #왼쪽으로 갈때 오른쪽으로 한칸 이동할때 생기는 전력 비교
# #좌로 간다면 위치가 M번째, M-1번째 가로등만

# while lights!=[0]*1000:
#     sum=0
#     for i in range(len(lights)):
#         sum+=lights[i]*abs(M-i)
#         if (lights[M-2]<lights[M]) or (M<2): #우측으로 이동하는 경우: 오른쪽으로 이동했을 때 더해지는 값이 더 작은 경우 혹은 좌로 이동할 수 없는 경우(1번에 있는 경우)
#             M+=1
#             lights[M]=0
#             sum-=lights[M] #바로 오른쪽 값을 0으로
#             print('right', M)
#         else: #좌측으로 이동하는 경우: 우로 이동하지 않는 경우 혹은 1000번에 있는 경우
#             M-=1
#             lights[M-2]=0
#             sum-=lights[M-2]
#             print('left', M)
#     watt+=sum
    
# print(watt)
    