n=int(input())
m=int(input())

friendlist=[]
for i in range(m):
    a,b=map(int, input().split())
    friendlist.append([a,b])

def find_friend(friends, pointer):
    fr=[]#바로 친구
    for rel in friends:
        if pointer == rel[0]:
            fr.append(rel[1])
        elif pointer == rel[1]:
            fr.append(rel[0])
        else: continue
    return fr #친구 리스트

fr1=find_friend(friends=friendlist, pointer=1)

fr2=[]
for fr in fr1:
    frt=find_friend(friends=friendlist, pointer=fr)
    for frfrt in frt:
        if (frfrt not in fr2) and (frfrt not in fr1) and (frfrt !=1):
            fr2.append(frfrt)

print(len(fr1)+len(fr2))
