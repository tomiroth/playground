import sys
import math
import time 

primeNumbers = [2,3,5,7,11,13,17]

def work_out_multiplys(number):
    for prime in primeNumbers:
        division = number/prime
        if division.is_integer():
            return prime, division

def get_multiplys_until_they_are_all_prime(multipliers):
    allPrime = True
    newMultipliers = []

    for multiplier in multipliers:
        if multiplier in primeNumbers:
            newMultipliers.append(int(multiplier))
            continue
        else:
            allPrime = False
            newNumbers = work_out_multiplys(multiplier)
            newMultipliers.append(int(newNumbers[0]))
            newMultipliers.append(int(newNumbers[1]))

    if allPrime == True:
        return multipliers
    else:
        return get_multiplys_until_they_are_all_prime(newMultipliers)
    

# If we have pairs they go out side of the square root
def sort_in_to_pairs(multipliers):
    sortedPairs = {}
    for multiplier in multipliers:
        if multiplier not in sortedPairs.keys():
            sortedPairs[multiplier] = [multiplier]
        else:
            sortedPairs[multiplier].append(multiplier)

    insideSqr = 1;
    outsideSqr = 1;
    for numbers in sortedPairs.values():
        if math.fmod(len(numbers), 2) == 0:
            outsideSqr = outsideSqr * multiply_list(numbers[0:int(len(numbers)/2)])
        else:
            if len(numbers) > 1:
                del numbers[-1]
                outsideSqr = outsideSqr * multiply_list(numburs[0:int(len(numbers)/2)])
            insideSqr = insideSqr * numbers[0]

    return outsideSqr, insideSqr
                

def multiply_list(list):
    val = 1;
    for cVal in list:
        val = val * cVal
    return val;

 

def simplify(number):
    print(u"\u221a",number)
    multipliers = get_multiplys_until_they_are_all_prime([number])
    print("=",' x '.join(map(str,multipliers)))
    sSqr = sort_in_to_pairs(multipliers)
    print("=",sSqr[0],u"\u221a",sSqr[1])
    print("=",sSqr[0] * math.sqrt(sSqr[1]))





# https://www.youtube.com/watch?v=rjSCMUOuy_Y&ab_channel=TammyGrigsby
if len(sys.argv)< 2:
    print("Please specifiy a number to simplify")
else:
    simplify(int(sys.argv[1]))
    
