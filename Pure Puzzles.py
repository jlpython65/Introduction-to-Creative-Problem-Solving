
# from tkinter import X


# hash = "#####"
# # for a in range(0,4):
# #     print(hash)

# odds = []
# index = 0
# for x in range(0,6):
#     if x % 2 == 1:
#         print("odd number added")
#         odds.append(x)

#     result = hash[0:x+1]
#     print(result)
#     index += 1
#     if index > 3:
#         result = result[0:]
#         print(result)

input = input("insert 7 digits here")

def doubled_split(digit):
    double = digit*2
    print(double)
    if double > 10:
        split = str(double)
        split2 = int(split[1])
        split1 = int(split[0])
        print(split2)
        return split1, split2
    else: 
        print("added")
        return double


index = 0
result = 0
for digit in input:
    index += 1
    int_digit = int(digit)
    result += int(digit)
    if index % 2 == 0:
        print(f"{index} index")
        print(doubled_split(int_digit))
    print(result)
    


doubled_split(input)