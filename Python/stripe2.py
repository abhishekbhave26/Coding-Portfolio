# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:08:05 2019

@author: abhis
"""
#5/12 testcases passed
def calculate_total_owed2(actions):
    create={}
    finalized={}
    paid={}
    sumOwed=0
    for i in actions:
        x=(i.split())
        method=x[0][:-1]
        rest=x[1].split('&')
        print(rest)
        if(method=='CREATE'):
            pass
        elif(method=='FINALIZE'):
            pass
        else:
            pass
    return sumOwed


def calculate_total_owed(actions):
    create={}
    finalized={}
    paid={}
    sumOwed=0
    for i in actions:
        x=(i.split())
        method=x[0][:-1]
        rest=x[1].split('&')
        if(len(rest)==3):
            iD,amount,curr=rest[0].split('='),rest[1].split('='),rest[2].split('=')
            iD,amount,curr=iD[1],int(amount[1]),curr[1]
            if(curr!="USD"):
                continue
            if(method=='CREATE'):
                if(iD in finalized or iD in paid):
                    continue
                create[iD]=int(amount)
            else:
                #FINALIZE
                if(iD in paid):
                    continue
                if(iD in create):
                    del create[iD]
                    finalized[iD]=int(amount)
                else:
                    continue
        else:
            #PAY
            iD=rest[0].split('=')
            iD=str(iD[1])
            if(iD in create or iD in finalized):
                if(iD in finalized):
                    paid[iD]=1
                    if(iD in create):
                        del create[iD]
                    if(iD in finalized):
                        del finalized[iD]
                else:
                    continue
            else:
                continue
    
    for i in create.values():
        sumOwed+=i
    for i in finalized.values():
        sumOwed+=i
    return sumOwed




actions=['CREATE: id=14&amount=1000&currency=USD','FINALIZE: id=14&amount=100&currency=USD',
         'CREATE: id=15&amount=1000&currency=US','FINALIZE: id=16&amount=100&currency=USD',
         'CREATE: id=16&amount=1&currency=USD']
result = calculate_total_owed(actions)
print(result)

#I would add more edge cases. I think I have missed out one edge case because of which my code does not pass one remaining test case. I would also try and clean up the code a bit for better understanding. One more thought about the challenge was that it was interesting and relevant to the real world unlike other online assessments. 

