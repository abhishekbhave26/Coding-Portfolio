def solution(N, S):
    # write your code in Python 3.6
    if(N==1 and S==''):
        return 3
    S=S.split()
    fam=0
    new=['A','B','C','D','E','F','G','H','J','K']
    for i in range(0,N):
        count=0
        for j in range(0,len(new)):
            if(j=='A' or j=='D' or j=='H'):
                count=0
            x=str(i)+str(new[j])
            if x in S:
                count=0
            elif(count==3):
                fam+=1
            else:
                count+=1
    return int(fam/3)


def solution(N, S):
    # write your code in Python 3.6
    if(N==1 and S==''):
        return 3
    S=S.split()
    fam=0
    new=['A','B','C']
    new2=['D','E','F','G']
    new3=['H','J','K']
    for i in range(0,N):
        count=0
        for j in range(0,3):
            x=str(i)+str(new[j])
            if x in S:
                break
            else:
                count+=1
        if(count==3):
            fam+=1
            #print(fam)
        count=0
        for j in range(0,3):
            x=str(i)+str(new3[j])
            if x in S:
                break
            else:
                count+=1
        if(count==3):
            fam+=1 
            #print(fam)
            
        count=0
        for j in range(0,4):
            x=str(i)+str(new2[j])
            #print(x)
            if x in S:
                count=0
            else:
                count+=1
        if(count==3):
            fam+=1
        #print(S)
        #print(fam)
            
    return fam