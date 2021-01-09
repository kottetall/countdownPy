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

    # brute force - Onödigt omständigt, går att göra bättre!
    solutions = []
    operand = ["+", "-", "/", "*"]
    for one in range(4):
        exampleOne = str(n1) + str(operand[one]) + str(n2)
        solutions.append(exampleOne)
        print("Går igenom uträkning: " + exampleOne)
        for two in range(4):
            exampleTwo = str(n1) + str(operand[one]) + str(n2) + str(operand[two]) + str(n3)
            solutions.append(exampleTwo)
            print("Går igenom uträkning: " + exampleTwo)
            for three in range(4):
                exampleThree = str(n1) + str(operand[one]) + str(n2) + str(operand[two]) + str(n3) + str(operand[three]) + str(n4)
                solutions.append(exampleThree)
                print("Går igenom uträkning: " + exampleThree)
                for four in range(4):
                    exampleFour = str(n1) + str(operand[one]) + str(n2) + str(operand[two]) + str(n3) + str(operand[three]) + str(n4) + str(operand[four]) + str(n5)
                    solutions.append(exampleFour)
                    print("Går igenom uträkning: " + exampleFour)
                    for five in range(4):
                        #onödigt att lägga detta separat, kan utvärdera direkt
                        exampleFive = str(n1) + str(operand[one]) + str(n2) + str(operand[two]) + str(n3) + str(operand[three]) + str(n4) + str(operand[four]) + str(n5) + str(operand[five]) + str(n6)
                        solutions.append(exampleFive)
                        print("Går igenom uträkning: " + exampleFive)

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

def printSolution(randomNums, target, numOfPossibleCalcs, calcEval):
    print("")

    print("Numren som slumpades fram var: \n" + str(randomNums))
    print("Målet blev: " + str(target) + "\n")
    print("Av " + str(numOfPossibleCalcs) + " möjliga uträkningar, blir svaret:\n")

    if len(calcEval["10p"]) > 0:
        print("finns lösning!")
        for ten in calcEval["10p"]:
            print("\t" + ten)
    elif len(calcEval["7p"]):
        print("Fanns ingen 10p, men någon/några 7p:")
        for seven in calcEval["7p"]:
            print("\t" + seven)
    elif len(calcEval["5p"]):
        print("Fanns ingen 10p eller 7p, men någon/några 5p:")
        for five in calcEval["5p"]:
            print("\t" + five)
    else:
        print("Ingen lösning gick att finna...")


#### MAIN ####
choice = random.randrange(1, 4, 1)
randomNums = randomLarge(choice) + randomSmall(6 - choice)
target = randomTarget()

possibleCalculations = possibleSolutions(randomNums)
calcEval = solve(target, possibleCalculations)

printSolution(randomNums, target, len(possibleCalculations), calcEval)