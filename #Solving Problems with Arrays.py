#Solving Problems with Arrays
# array = [4, 7, 3, 8, 9, 7, 3, 9, 9, 3, 3, 10]


# max = 4

# for index, value in enumerate(array):
#     if index+1 == len(array): #That's peculiar, index+1 is = len(array) 12 = 12
#         break
#     if max < array[index+1]:
#         max = array[index+1]
#         print(max)
#     else:
#         print(f"{array[index+1]} is smaller than {max}")

# #What about mode?
from array import array
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic

# , 9, 9, 8, 3, 3, 3, 3, 10
array = [4, 7, 7, 9, 9, 9, 8, 3, 3, 3, 3, 10]
frequency_dict = {}
mode = 0
highest_frequency = 0
frequency = 0

try:
    for index, value in enumerate(array):
        frequency += 1
        if value == array[abs(index+1)]: #this line is stopping my code at index 2
            mode = value
            if frequency > highest_frequency: 
                highest_frequency = frequency
            frequency = 1

        ic(index)
        print("--------")
        ic(mode)
        ic(frequency)
        ic(highest_frequency)
        print("--------")
except:
    print(f"the mode is the number {mode} with {highest_frequency} occurances")


# frequency_list = frequency_dict.items()
# print(frequency_list)

# for index, value in enumerate(frequency_list):
#     if index+1 == len(frequency_list): #That's peculiar, index+1 is = len(frequency_list) 12 = 12
#         break
#     if max < frequency_list[index+1]:
#         max = frequency_list[index+1]
#         print(max)
#     else:
#         print(f"{frequency_list[index+1]} is smaller than {max}")


# # Quick sort in Python

# # # function to find the partition position
# def partition(array, first_index, end_index):

#   # choose the rightmost element as pivot
#   pivot = array[end_index]

#   # swap_pointer for greater element
#   swap_pointer = first_index - 1

#   # traverse through all elements
#   # compare each element with pivot
#   for item in range(first_index, end_index):
#     if array[item] >= pivot:
#       # if element smaller than pivot is found
#       # swap it with the greater element pointed by swap_pointer
#       swap_pointer = swap_pointer + 1

#       # swapping element at swap_pointer with element at item
#       (array[swap_pointer], array[item]) = (array[item], array[swap_pointer])

#   # swap the pivot element with the greater element specified by swap_pointer
#   (array[swap_pointer + 1], array[end_index]) = (array[end_index], array[swap_pointer + 1])

#   # return the position from where partition is done
#   return swap_pointer + 1 #index of where the switch was made

# # function to perform quicksort
# def quickSort(array, first_index, end_index):
#   if first_index < end_index:

#     # find pivot element such that
#     # element smaller than pivot are on the left
#     # element greater than pivot are on the right
#     pivot = partition(array, first_index, end_index)

#     # recursive call on the left of pivot
#     quickSort(array, first_index, pivot - 1)

#     # recursive call on the right of pivot
#     quickSort(array, pivot + 1, end_index)


# data = [8, 7, 2, 1, 0, 9, 6]
# print("Unsorted Array")
# print(data)

# size = len(data)

# quickSort(data, 0, size - 1) #size - 1 = end index

# print('Sorted Array in Descending Order:')
# print(data)




