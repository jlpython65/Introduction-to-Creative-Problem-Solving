
# from tkinter import X


# hash = "#####"
# # for a in range(0,4):
# #     print(hash)

# odds = []
# index = 0
# for x in range(0,6):
#     result = hash[4 - abs(4 - x)]
#     print(result)
#     index += 1
#     if index > 3:
#         result = result[0:]
#         print(result)

#1.
# hash = "########"
# odds = []
# index = 0
# for row in range(0,4):
#     result = hash[0:8-index].center(14)
#     print(result)
#     index += 2

#2. 
# from re import X


# hash = "##########"
# odds = []
# index = 0
# row = 0
# print(hash[0:2])
# for row in range(0,7):
#     expression = (8-abs(2*row-4))
#     result = hash[0:expression].center(14)
#     if row == 2:
#         result = hash[0:8-abs(2*2-4)].center(14)
#         print(result)
#     print(result)

#ok instead of thinking about keeping the hashes in the middle, just focus on getting the number of hashes

# hashes = 8
# for row in range(4):
#     print(hashes)
#     hashes -= 2

#3. 

# from string import whitespace
# import math

# hash = "##########"
# odds = []
# index = 0
# row = 0

# # list = ["#", " ", " ", " ", " ","#"]
# # list.insert(0," ")
# # list.append(" ") # I used append instead of insert because these commands are distinct
# # print("".join(list))


# for row in range(0,4):

#     whitespace = " " * int(-4*row+12)
#     expression = (8-abs(2*row-6))
#     result = hash[0:expression]
#     result_split = [*result]
#     middleIndex = len(result_split)//2
#     result_split.insert(middleIndex,whitespace)

#     result_split.insert(0," "*row)


#     joined = "".join(result_split)
#     print(joined)


# for row in reversed(range(0,4)):

#     whitespace = " " * int(-4*row+12)
#     expression = (8-abs(2*row-6))
#     result = hash[0:expression]
#     result_split = [*result]
#     middleIndex = len(result_split)//2
#     result_split.insert(middleIndex,whitespace)

#     result_split.insert(0," "*row)


#     joined = "".join(result_split)
#     print(joined)

# def two_digit_number(doubled_number):
#    digits = [int(i) for i in str(doubled_number)]
#    result = digits[0] + digits[1]
#    return result


# input= str(3241523)
# index = 0
# total = 0
# for digit in input:
#     index += 1
#     digit = int(digit)
#     if index %2 == 0:
#         doubled_number = digit * 2
#         if doubled_number > 10:
#             total += two_digit_number(doubled_number)
#             print(total)
#     total += digit
#     print(total)
# if total % 10 == 0:
#     print("verified")
    




# input = input("insert 7 digits here")

# def doubled_split(digit):
#     double = digit*2
#     print(double)
#     if double > 10:
#         split = str(double)
#         split2 = int(split[1])
#         split1 = int(split[0])
#         result = split1 +split2
#         print(result)
#         return result
#     else: 
#         print("added")
#         return double


# index = 0
# result = 0
# for digit in input:
#     index += 1
#     int_digit = int(digit)
#     if index % 2 == 0:
#         print(f"{index} index")
#         doubled = doubled_split(int_digit)
#         result += doubled
#     else:
#         print(f"{digit} is the digit")
#         result += int(digit)
#         print(result)
#         if result % 10 == 0:
#             print("verified")

# #Decode a Message
# from operator import index
# from string import punctuation


from functools import partial


input_list = [18,12312,171,763,98423,1208,216,11,500,18,241,0,32,20620,27,10]
punctuation_list = ["fill","!","?",",","."," ",";",'"',"'"]
continue_from_index = []
#index left off? What is the name of this variable?

# def uppercase_mode():
#     for input in input_list:
#         character_index = input % 27
#         letter = chr(ord('@')+character_index)

#         if character_index == 0:
#             print("Switching to lowercase mode")
#             del input_list[0:input_list.index(input)+1]
#             break
#         print(letter)

# def lowercase_mode():
#     for input in input_list:
#         character_index = input %27
#         letter = chr(ord('`')+character_index)
#         if character_index == 0:
#             print("Switching to punctuation mode")
#             del input_list[0:input_list.index(input)+1]
#             break
#         print(letter)



def modes(mode,foo):
    if foo == "foo":
        print("foo")

    if mode == "upper":
        modulus_value = "27"
        letter_case = "@"
        next_mode = "lower"
        print("upper")

    if mode == "lower":
        modulus_value = "27"
        letter_case = "`"
        next_mode = "punctuation"
        print("lower")

    if mode == "punctuation":
        modulus_value = "9"
        letter_case = 


    for input in input_list:
        character_index = input % int(f"{modulus_value}")
        letter = chr(ord(f'{letter_case}')+character_index)
        print(letter)

        if mode == "punctuation":
            punctuation = punctuation_list[character_index]
            print(punctuation)

        if character_index == 0:
            print(f"Switching to {next_mode} mode")
            del input_list[0:input_list.index(input)+1]
            break
        

# def punctuation_mode():
#     for input in input_list:
#         punctuation_index = input %9
#         punctuation = punctuation_list[punctuation_index]
#         if punctuation_index == 0:
#             print("Switching to uppercase mode")
#             del input_list[0:input_list.index(input)+1]
#             break
#         print(punctuation)

lower_mode = partial(modes,foo = "foo")

upper_mode = lower_mode

punctuation_mode = lower_mode
for x in range(1):
    upper_mode("upper")
    lower_mode("lower")
    punctuation_mode("punctuation")


#4. Soul Gem
         #
        #
         #
      #
     #
    #
   #
   #
     #
      ##
     #
     ###

# for row in range(0,3):
#     whitespace_from_vertical = (-abs(row-1)+1)
#     first_half = " "*(9-whitespace_from_vertical) + "#"+ " "*(whitespace_from_vertical*2) +"#"
#     print(first_half)


# for row in range(3,7):
#     whitespace_from_vertical = (-abs(row-6)+5)
#     first_half = " "*(9-whitespace_from_vertical) + "#"+ " "*(whitespace_from_vertical*2) +"#"
#     print(first_half)

    
# for row in reversed(range(3,6)):
#     whitespace_from_vertical = (-abs(row-6)+5)
#     first_half = " "*(9-whitespace_from_vertical) + "#"+ " "*(whitespace_from_vertical*2) +"#"
#     print(first_half)
# print("""       ######
#        #    #
#        ######""")



    