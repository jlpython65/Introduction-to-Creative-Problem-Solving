from itertools import filterfalse
import itertools
from operator import le
import re
from icecream import ic
import statistics
from statistics import mode


index_and_occurances = {}

word_list = ["jam","ham","sam","cam","bam","wam","dim","man","men","ain","age","ann","air","dio","edei","die","dei"]
pattern_list = []
index_for_blank = []
def get_most_options(letter):
    print(letter)
    print(word_list)
    # try:
    def filter_for_letter(word):
        return letter not in word
    
    def filter_for_mode(word):
        pattern_list.append(str(word).index(f"{letter}"))
        most_common_pattern = mode(pattern_list)

        return most_common_pattern != str(word).index(f"{letter}")

    words_with_letter = list(itertools.filterfalse(filter_for_letter, word_list))
    most_options = list(itertools.filterfalse(filter_for_mode,words_with_letter))
    index_for_blank.append(mode(pattern_list))
    pattern_list.clear()
    return most_options
    
blanks = "_ _ _"
blanks_list = blanks.split(" ")

def display_correct_guess(letter,most_common_index):
    print(most_common_index)
    blanks_list[int(most_common_index)] = letter
    result = " ".join(blanks_list)
    print(result)

length = int(input("How long should the word be?"))

for x in range(length):
    letter = input("Guess a letter!")
    word_list = get_most_options(letter)
    display_correct_guess(letter,index_for_blank[x])
    print(word_list)
