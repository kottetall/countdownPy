# https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round - regler

import random




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


def solve(target, numbers, solution):
    if len(numbers) == 0:
        print("ingen lösning")
        return



choice = 1
randomNums = randomLarge(choice) + randomSmall(6 - choice)
target = randomTarget()

print(target)
print(randomNums)

solve(target, randomNums, "")