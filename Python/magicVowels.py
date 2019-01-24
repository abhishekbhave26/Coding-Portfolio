# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:47:19 2019

@author: abhis
"""

def checkMagicVowel(s):
    
	 
	count = 0	
	if ('a' in s) and ('e' in s) and ('i' in s) and ('o' in s) and ('u' in s):
        
		v = 'aeiou'
		a = ''

		for letter in s:
			if letter in 'aeiou':
				a+= letter
		
        
		index = 0
		current = v[index]
		
		i = 0
		for current_char in a:
			
			if current_char == current:
				count+=1

			if (i < len(a)-1):
				next_char = a[i+1]

				if(index != 4):
					next_vowel = v[index+1]
				else:
					next_vowel = v[index]

				#next character should be the next new vowel only to count++
				if (current_char != next_char and next_char == next_vowel):
						if(index != 4):
							index += 1
						current = v[index]

			i +=1
        return count
        
        
        
		
	else:
		return 0
    
    


print(checkMagicVowel('aeiaaioooaauuaeiou'))