
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

    
        


