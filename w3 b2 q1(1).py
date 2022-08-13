numbers = [1,2,5,3,1]

def compare(number1, number2):
    if number1 != number2:
        return True
    else:
        return False

for x in numbers:
    number1 = x
    for x in range(len(numbers)): #It hasn't occured to me to make another loop. 
        if(compare(number1,numbers[x])):
            print(f"{str(number1)} can't be found in index " + f'{x}')
    
#Why 2 matches? It's because the 2nd number is numbers[0]. It's like you're comparing the same value numbers[0] = numbers[0]