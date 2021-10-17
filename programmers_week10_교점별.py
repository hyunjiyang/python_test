from itertools import combinations as cd
def solution(line):
    meet = []
    new = list(cd(line,2))
    for i in range(len(new)):
        x=0
        y=0
        a = new[i][0][0]
        b = new[i][0][1]
        e = new[i][0][2]
        c = new[i][1][0]
        d = new[i][1][1]
        f = new[i][1][2]
        if a*d-b*c != 0:
            if (b*f-e*d)%(a*d-b*c) == 0 and (e*c-a*f)%(a*d-b*c) ==0:
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                meet.append((x,y))
    meet = list(set(meet))
    width = max(meet)[0]-min(meet)[0]+1
    height = max(meet,key=lambda x:x[1])[1]-min(meet,key=lambda x:x[1])[1]+1
    answer = list("."*int(width) for _ in range(int(height)))
    for i in range(len(meet)):
        a = max(meet)[0]-meet[i][0]
        b = meet[i][1]
        a = int(a)
        b = int(b)
        answer[a].[b]= "*"


    return a
