k=int(input())
for c in range(k):
    students=sorted(list(map(int, input().split()))[1:])
    gap=0
    for i in range(len(students)-1):
        ng=students[i]-students[i+1]
        if ng<gap:
            gap=ng
    print(f"Class {c+1}")
    print(f"Max {students[-1]}, Min {students[0]}, Largest gap {gap*-1}")