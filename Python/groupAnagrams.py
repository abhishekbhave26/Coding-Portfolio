# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:23:06 2019

@author: abhis
"""
#leetcode 49

import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        print(groups.keys())
        for s in strs:
            groups["".join(sorted(s))].append(s)
        return list(groups.values())
    
    def groupAnagrams2(self,strs):
        groups = collections.defaultdict(list)
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            groups[tuple(char_count)].append(s)
        return list(groups.values())


x=["eat", "tea", "tan", "ate", "nat", "bat"]
s=Solution()
print(s.groupAnagrams2(x))


