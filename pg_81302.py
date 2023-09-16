           
def solution(places):
    for c in range(5): #각 대기실 번호
        persons=[]
        for j in range(5): #행
            for k in range(5): #열
                if places[c][j][k]=="P" and [j,k] not in persons:
                    persons.append([j,k])
        if len(persons)==0:
            clear=1
        else:
            clear=1
            while clear!=0:
                for i in range(len(persons)):
                    for j in range(len(persons)):
                        x1=persons[i][0]
                        y1=persons[i][1]
                        x2=persons[j][0]
                        y2=persons[j][1]
                        distance=abs(x1-x2)+abs(y1-y2)
                        if distance==1:
                            clear=0
                        if distance==2:
                            if x1==x2: #가로 직선
                                if places[c][(x1+x2)//2][y1]=="O": clear=1
                                else:
                                    print('hor')
                                    clear=0
                            elif y1==y2: #세로 직선
                                if places[c][x1][(y1+y2)//2]=="O": clear=1
                                else:
                                    print('ver')
                                    clear=0
                            else:
                                clear=1
                                # if places[c][x1][y2]=="O": clear=1
                                # else: clear=0
                break
        print(clear)    
        print("=======================")
    # answer = []
    # return answer

solution(places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], #1
                 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], #0
                 ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], #1
                 ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], #1
                 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])#1