import sys
n=int(sys.stdin.readline())
words=[]
for i in range(n):
    word=sys.stdin.readline().rstrip()
    if word not in words:
        words.append(word)
for i in range(1,51):
    temp_list=[]
    for j in range(len(words)):
        if len(words[j])==i:
            temp_list.append(words[j])
    sort=sorted(temp_list)
    try:
        for i in range(len(sort)):
            print(sort[i])
    except: continue