#Cheating Hangman
from code import interact
from os import remove
from icecream import ic
import re
# words_file = open("words.txt","r")
# words = words_file.read()
# split = words.split("\n")
# print(split) 


index_and_occurances = {}

print("_ _ _")
letter = input("Guess a letter!")

word_list = ["jam","ham","sam","cam","bam","wam","dim","man","men","ain","age","ann","air"]
most_common_pattern = []

def get_possible_words(letter):
    occurances = 0
    try:
        for index, word in enumerate(word_list):
            occurances += 1
            index_of_letter = word.index(f"{letter}")
            index_of_letter_of_next_item = word_list[index+1].index(f"{letter}")
            if index_of_letter != index_of_letter_of_next_item:
                index_and_occurances[str(index_of_letter)] = occurances
                most_common_index = max(index_and_occurances,key=index_and_occurances.get)
                occurances = 0
    except:
        print(" ")
    print(index_and_occurances)
    print(f"the most common index is {most_common_index} with {index_and_occurances[most_common_index]} number of occurances")
    
    for index, word in enumerate(word_list): 
        index_of_letter = word.index(f"{letter}") 
        print(index_of_letter)
        if index_of_letter != 2:
            del word_list[index]
            print(word_list)

            
    return most_common_index
blanks = "_ _ _"
blanks_list = blanks.split(" ")

def display_correct_guess(letter,most_common_index):
    print(most_common_index)
    blanks_list[int(most_common_index)] = letter
    result = " ".join(blanks_list)
    print(result)
display_correct_guess(letter,get_possible_words(letter))
print(blanks_list)
print(word_list)



# new = filter(lambda word: word.index(f"{letter}") == 0, word_list)
# ic(new)
# for x in new:
#     print(x)
