# 57 74 65 61 | 37 58 89 145 42 20 4 16 | 37 58 89...
a, p = map(int, input().split())

def get_next(num, p):
    nv=0
    for s in str(num):
        nv+=int(s)**p
    return nv

if a==1: #1이 들어가면 반복값 없으므로 0을 리턴해줘야 한다
    answer=0
    
else:
    nums=[a]
    while True:
        nv=get_next(nums[-1],p)
        if nv not in nums:
            nums.append(nv)
        else:
            keynum=nv
            answer=nums.index(keynum)
            break
print(answer)
