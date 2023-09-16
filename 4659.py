while True:
    case=str(input())
    if case=='end':
        break
    else:
        code=''
        for chr in case:
            if chr in ['a','e','i','o','u']:
                code+='v'
            else:
                code+='c'
        if 'v' not in code: #모음이 없는 경우
            check=False
        elif 'vvv' in code or 'ccc' in code: #3개 연속인 경우: iii, eee는 여기서 처리됨
            check=False
        else: #모음도 있고, 3개 연속도 없어
            if len(case)==1:
                check=True
            else:
                eeoo=False
                double=False
                for i in range(len(case)-1):
                    if case[i]==case[i+1]:
                        if case[i]=='e' or case[i]=='o':
                            eeoo=True
                        else:
                            double=True
                if eeoo==True:
                    check=True
                elif double==True:
                    check=False
                else:
                    check=True
                    
    if check==True:
        print(f"<{case}> is acceptable.")
    else:
        print(f"<{case}> is not acceptable.")