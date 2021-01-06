# https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round - regler

import random


#### FUNKTIONER ####

def randomLarge(choice=0):
    largeNums = [25, 50, 75, 100] # 0-4 nummer väljs, antalet + smånumren ska bli totalt 6 st
    randomNums = []
    for x in range(choice):
        randomNums.append(largeNums.pop(random.randrange(0, len(largeNums), 1)))

    return randomNums

def randomSmall(limit=6):
    smallNums = []
    for x in range(10):
        smallNums.append(x + 1)
        smallNums.append(x + 1)
    
    randomNums = []

    for y in range(limit):
        randomNums.append(smallNums.pop(random.randrange(0, len(smallNums), 1)))

    return randomNums

def randomTarget():
    # Ger inga siffror under 100, ex 045 etc
    return random.randrange(100, 999, 1)

def possibleSolutions(numbers):
    n1, n2, n3, n4, n5, n6 = numbers

    # brute force
    solutions = []
    operand = ["+", "-", "/", "*"]
    for one in range(4):
        for two in range(4):
            for three in range(4):
                for four in range(4):
                    for five in range(4):
                        #onödigt att lägga detta separat, kan utvärdera direkt
                        example = str(n1) + str(operand[one]) + str(n2) + str(operand[two]) + str(n3) + str(operand[three]) + str(n4) + str(operand[four]) + str(n5) + str(operand[five]) + str(n6)
                        solutions.append(example)
                        print("Går igenom uträkning: " + example)

    return solutions

def solve(target, numbers):
    evauationOfCalculations = {
        "10p": [],
        "7p": [],
        "5p": []
    }

    sevenLow = target - 5
    sevenHigh = target + 5
    fiveLow = target - 10
    fiveHigh = target + 10


    for calculation in numbers:
        answer = eval(calculation)
        if answer == target:
            print(calculation + " ger svaret " + str(target))
            evauationOfCalculations["10p"].append(calculation)
        elif answer >= sevenLow and answer <= sevenHigh:
            print(calculation + " är 5 eller mindre ifrån " + str(target))
            evauationOfCalculations["7p"].append(calculation)
        elif answer >= fiveLow and answer <= fiveHigh:
            print(calculation + " är 10 eller mindre ifrån " + str(target))
            evauationOfCalculations["5p"].append(calculation)

    return evauationOfCalculations


#### MAIN ####
choice = 1
randomNums = randomLarge(choice) + randomSmall(6 - choice)
target = randomTarget()
possibleCalculations = possibleSolutions(randomNums)
#solve(target, possibleCalculations)

print(solve(target, possibleCalculations))


print(target)
print(randomNums)