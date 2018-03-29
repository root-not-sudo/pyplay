# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 13:02:51 2018

@author: Brent Markus
"""
import random
import string
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(' ', '')
    count = 0
    if(len(my_word) == len(other_word)):
        for i in range(len(my_word)):
            if(my_word[i] == other_word[i] or (my_word[i] == '_' and other_word[i] not in my_word)):
                count += 1

    return(len(my_word) == count)