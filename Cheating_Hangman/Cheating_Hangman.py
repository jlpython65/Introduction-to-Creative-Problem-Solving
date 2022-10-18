#Cheating Hangman
from code import interact
from icecream import ic
import re
# words_file = open("words.txt","r")
# words = words_file.read()
# split = words.split("\n")
# print(split) 

# def correct_letters():

index_and_occurances = {}

print("_ _ _")
letter = input("Guess a letter!")

word_list = ["jam","ham","sam","man","age","ann","air","neda"]
most_options = []

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
        print(word)
        index_of_letter = word.find(f"{letter}") #this line should be working, word = item. Maybe there 
        if index_of_letter == most_common_index:
            most_options.append(word)
    print(most_options)

get_possible_words(letter)



# new = filter(lambda word: word.index(f"{letter}") == 0, word_list)
# ic(new)
# for x in new:
#     print(x)
