n, k= map(int, input().split())
st=list(map(int, input().split()))

#차이를 구해서, n-k개만큼 작은 값부터 추출
diff=[]
for i in range(1,n):
    diff.append(st[i]-st[i-1])
diff.sort()
sum=0
for i in range(n-k):
    sum+=diff[i]
print(sum)