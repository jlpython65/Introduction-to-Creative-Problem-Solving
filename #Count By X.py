#Count By X

from audioop import mul
import imp


# array1 = []

# def countby(number,multiple,list):
#     array1.append(number)
#     for m in range(1,multiple):
#         result = number + (m * number)
#         array1.append(result)
#         print(array1)

# countby(1,10,array1)

# https://www.codewars.com/kata/57b6f850a6fdc76523001162
# Hit Count
# I see, the numbers need to be in an array so that the counter can iterate to the final, accurate value




# def counterEffect(string):
#     characters = list(string)
#     lists = [[] for i in range(4)]
#     numberslist = []
#     print(lists)
#     for x in range(len(lists)):
#         for i in characters: #how to append before number to their respective lists?
#             for y in int(i):
#                 lists[x].append(y)
#                 print(lists)

def counter_effect(hit_count):
    a = [range(int(i)+1) for i in hit_count]
    print(a)


counter_effect(str(1250))

# roachspeed = float(input("How fast is it? In km/hr"))

# def convert(roachspeed):
#     result = int(roachspeed * ((1/60)*(1/60)*100000) )
#     print(result)
# convert(roachspeed)

# import re

# string = input("Insert a sentence here and we'll count the vowels")

# a= re.findall(r"a|e|i|o|u",string=string)
# print(len(a))
# print(a)

