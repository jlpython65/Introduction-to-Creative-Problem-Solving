from itertools import filterfalse
import itertools
import re
from icecream import ic
import statistics
from statistics import mode
 
index_and_occurances = {}

word_list = ["jam","ham","sam","cam","bam","wam","dim","man","men","ain","age","ann","air","dio","edei","die","dei"]
pattern_list = []

def get_most_options(letter):
    print(letter)
    print(word_list)
    # try:
    def filter_for_letter(word):
        return letter not in word
    
    def filter_for_mode(word):
        pattern_list.append(str(word).index(f"{letter}"))
        most_common_pattern = mode(pattern_list)
        ic(pattern_list)
        ic(most_common_pattern)
        return most_common_pattern != str(word).index(f"{letter}")

    words_with_letter = list(itertools.filterfalse(filter_for_letter, word_list))
    ic(words_with_letter)
    most_options = list(itertools.filterfalse(filter_for_mode,words_with_letter))
    ic(most_options)
    pattern_list.clear()
    return most_options

for x in range(2):
    letter = input("Guess a letter!")
    word_list = get_most_options(letter)
    print(word_list)
