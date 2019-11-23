# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:59:47 2019

@author: abhis
"""
#leetcode 208

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head={}

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        current=self.head
        for c in word:
            if(c not in current):
                current[c]={}
            current=current[c]
        current['*']=True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        current = self.head
        for character in word:
            if character not in current:
                return False
            current = current[character]
        if '*' in current:
            return True
        return False
	

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.head
        for character in prefix:
            if character not in current:
                return False
            current = current[character]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)