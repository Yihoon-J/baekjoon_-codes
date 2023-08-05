n=int(input())

zero_list=[0]*n
one_list=[0]*n

zero_list[0]=0
one_list[0]=1

for i in range(1,n):
    #0개수: 이전 0에서 나오는 것 + 1에서 나오는 거
    zero_list[i] = zero_list[i-1] + one_list[i-1]
    #1개수: 이전 0에서 나오는 것만 있음
    one_list[i] = zero_list[i-1]
 
print(one_list[-1]+zero_list[-1])