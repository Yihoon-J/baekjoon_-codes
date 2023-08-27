n, q= map(int, input().split())
cars=sorted(list(map(int, input().split())))
exp=[]
for i in range(q):
    exp.append(int(input()))

for i in range(q):
    if exp[i] not in cars :
        result=0 #기대값이 연비 목록에 없으면 무조건 0
    else: #있다면,
        a=0 #중앙값 해당 차가 몇 대인지
        left=-1 #왼쪽에 올 수 있는 차 수
        right=-1 #오른쪽에 올 수 있는 차 수
        for j in cars:
            if j==exp[i]:
                a+=1
            if j<=exp[i]:
                left+=1
            if j>=exp[i]:
                right+=1
        if left==0 or right==0:
            result=0
        else:
            result=a*(left*right-a+1)
    print(result)
        
#중앙값에 해당하는 차의 개수를 먼저 카운트: a대가 있다 치고, a를 곱해주자.
    #일단 그 차가 없는 리스트에서,
    #왼쪽에는 그보다 연비 낮은 차 or 같은 연비의 차 중 나머지 하나를 고르고 - 작거나 같은 수 몇개?
    #오른쪽에는 그보다 연비 높은 차 or 같은 연비의 차 중 나머지 하나를 고름 - 크거나 같은 수 몇개?
    #여기서, 좌측과 우측 모두 같은 차를 고르는 경우만 빼면 된다. - (a-1)가지가 있겠다