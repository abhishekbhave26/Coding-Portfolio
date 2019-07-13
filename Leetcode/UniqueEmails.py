# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 01:33:12 2019

@author: abhis
"""
#leetcode 929


class Solution:
    def numUniqueEmails2(self):
        emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        dict={}
        for i in emails:
            email=''
            flag=0
            for j in range(0,len(i)):
                if(i[j]=='@'):
                    email+=i[j:]
                    if(email in dict):
                        dict[email]+=1
                    else:
                        dict[email]=1
                    break
                if(i[j]=='.'):
                    pass
                if(i[j]=='+'):
                    flag=1
                if(i[j] not in ['@','.','+'] and flag==0):
                    email+=i[j]
        return len(dict)
    
    def numUniqueEmails(self):
        emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)
                    
s=Solution()
print(s.numUniqueEmails())
                
        