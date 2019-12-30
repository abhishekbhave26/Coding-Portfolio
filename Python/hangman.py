# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:11:02 2019

@author: abhis
"""
hidden_word='apple'

def main():
    start_string='?'*len(hidden_word)
    wrong_answers=0
    while(True):
        processed_input=process_user_input()
        
        start_string,wrong_answers=guess_character(processed_input,start_string,wrong_answers)
        if(display(start_string)):
            break
        if(wrong_answers==3):
            print('You have entered 3 wrong answers')
            print('Please try again')
            break
    

def guess_character(u_char,start_string,wrong_answers):
    if(u_char in hidden_word):
        for i,v in enumerate(hidden_word):
            if(v==u_char):
                start_string= start_string[:i] + u_char + start_string[i + 1:]
    else:
        print('You have guessed incorrectly')
        wrong_answers+=1
        
    return start_string,wrong_answers


def display(user_string):
    print("Word is:",end=" ")
    for i in user_string:
        print(i,end=" ")
    if('?' not in user_string):
        print("You have guessed the word correctly")
        return True
    return False


def process_user_input():
    while(True):
        user_input=input('Please enter a character:')
        if(user_input.isalpha() and len(user_input)==1):
            return user_input.lower()
        
main()


        
    
    