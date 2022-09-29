#Cheating Hangman
from code import interact
from icecream import ic
import re
# words_file = open("words.txt","r")
# words = words_file.read()
# split = words.split("\n")
# print(split) 

# def correct_letters():


letter = "a"
word_list = ["jam","ham","sam","age","ann","air","man"]
index_0 = []
index_1 = []


count = 0

#Find words with a in them and the position of a in that word. 
#group the number of words depending on where a is. if a is the 2nd letter
#group up words that fulfill that condition. Count how many items are there
#with a as its 2nd number
new = filter(lambda word: word.index("a") == 0, word_list)
ic(new)
for x in new:
    print(x)