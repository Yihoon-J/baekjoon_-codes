import heapq

n=int(input())
cards=[]
for i in range(n):
    heapq.heappush(cards, int(input()))

result = 0

if len(cards)==1:
    print(result)

else:
    for i in range(n-1):
        # print(cards)
        previous = heapq.heappop(cards)
        current = heapq.heappop(cards)
        result += previous + current
        heapq.heappush(cards,previous + current)   
    print(result)


# for i in range(n):
#     ncards.append(int(input()))

# ncards.sort()
# if len(ncards)==1:
#     print(ncards[0])
# else:
#     counts=[0]
#     for i in range(len(ncards)):
#         counts.append(counts[i]+ncards[i])
#     print(counts)
#     result=0
#     for i in range(2, len(counts)):
#         result+=counts[i]
#     print(result)