from itertools import filterfalse
import itertools
import re

import statistics
from statistics import mode
 
index_and_occurances = {}

print("_ _ _")
letter = input("Guess a letter!")

word_list = ["jam","ham","sam","cam","bam","wam","dim","man","men","ain","age","ann","air","dio","ede"]
pattern_list = []

def get_possible_words(letter):
    # try:
    def filter_for_letter(word):
        return letter not in word
    
    def filter_for_mode(word):
        pattern_list.append(str(word).index(f"{letter}"))
        most_common_pattern = mode(pattern_list)
        return most_common_pattern != str(word).index(f"{letter}")

    itertools.filterfalse(filter_for_letter,word_list)
    words_with_letter = list(itertools.filterfalse
    (filter_for_letter, word_list))
    most_options = list(itertools.filterfalse(filter_for_mode,words_with_letter))
    return most_options

word_list = get_possible_words(letter)

print(word_list)
