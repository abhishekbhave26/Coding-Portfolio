# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:26:10 2019

@author: abhis
"""

def compare(word1, word2):
    #this should return True if value 1 is alphabetically before value 2, false otherwise
    letter_index = 0
    while letter_index < len(word1):
        letter_index += 1
        letter1 = word1[letter_index]
        letter2 = word2[letter_index]
        if letter1 > letter2:
            return True
        elif letter2 > letter1:
            return False
    #if they’re the same word, we’ll exit the loop and it doesn’t matter what we return
    return True

#x=compare('fgh','fghi')
#print(x)


def compute_number_score(number):
    s=str(number)
    score=0
    c3=0
    n=0
    for i in range(0,len(s)):
        if(int(s[i])%2==1):
            score+=1
        if(s[i]=='5'):
            score+=2
        if(s[i]=='3'):
            if(c3==0):
                c3+=1
            elif(c3==1):
                c3+=1
                score+=4
            else:
                score+=4
        else:
            c3=0
        if(i!=0):
            if(int(s[i-1])<int(s[i])):
                n+=1
            else:
                score+=n*n
                n=0
                
        else:
            score+=1

    if(number%5==0):
        score+=6
    return score

#print(compute_number_score(101275345))
#print(compute_number_score(141333852))
    

x=['ACQUIRE 123','ACQUIRE 364','ACQUIRE 84','RELEASE 84','RELEASE 364','ACQUIRE 456']

def check_log_history(events):
    release={}
    acquire={}
    st=[]
    for i,v in enumerate(events):
        action,iD=v.split()
        if(action=='RELEASE'):
            if(iD in acquire):
                del acquire[iD]
                if(st[-1]!=iD):
                    return i+1
                st.pop()
            else:
                return iD
        else:
            if(iD in acquire):
                return iD
            else:
                st.append(iD)
                acquire[iD]=i
    
    return 0

print(check_log_history(x))




