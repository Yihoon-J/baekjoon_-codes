#idea: 데이터가 최대 10만개인 반면 범위는 1만에 불과 --> 계수정렬 활용
#입력 시 메모리 최소화하기 위해 input 대신 sys.readline 사용
#이때 실제 리스트 저장하는 대신 바로 계수정렬 진행
import sys
n=int(sys.stdin.readline())
sort_list=[0]*10001

for i in range(n):
    num=int(sys.stdin.readline().rstrip())
    sort_list[num]+=1

for i in range(len(sort_list)):
    for j in range(sort_list[i]):
        print(i)