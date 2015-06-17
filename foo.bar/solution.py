import random
import sys
sys.setrecursionlimit(5000)

i = 0
randNums = []
randSize = random.randrange(2, 5000)

def newRand(i):
    nr = random.randrange(0, randSize)
#    print("old = " + str(i) + " new = " + str(nr))
    if i == nr:
        nr = newRand(i)
    return nr

for i in range(0, randSize):
    curRand = random.randrange(0, randSize)
#    print("i = " + str(i) + " and curRand = " + str(curRand))
    if i == curRand:
#        print(str(i) + " == " + str(curRand))
        nr = newRand(curRand)
#        print("new rand = " + str(nr))
        randNums.append(nr)
    else:
        randNums.append(curRand)

"""
def getNext(p, s, numbers):
    np = numbers[p]
    print("pirate = " + str(p) + " says go to pirate = " + str(np))
    if np in s:
        s.add(p)
        print ("stop -----> " + str(s))
#        return len(s) 
    else:
        s.add(p)
        print ("do again -----> " + str(s))
        getNext(np, s, numbers)
        return len(s)
"""

def getNext(p,s,numbers):
    s.append(p)
    np = numbers[p]
    print(s)
    if np in s:
        return 
    getNext(np,s,numbers)
    return len(s)


def answer(numbers):
    return getNext(numbers[0], [], numbers)

#       [0,1,2,3]
#nums = [1,3,0,1]   
#nums = [1,0]
#nums = [1,2,1]
#nums = [1,3,1]
#nums = [6,0,0,5,0,1,4]  #3
#nums = [5000,18,3,4,5]
#nums = [1,2,3,4,0]
#nums = [1,2,2,2]
#nums = [6,8,5,0,0,4,5,1,2]
nums = [9,0,0,0,0,0,0,0,0,0]
#nums = [4,3,0,2,1]

#pirate 4999 is @ 5000
# list of size 5000
#   [4999, .... ,0]

#print("randSize = " + str(randSize))
#print(randNums)
#print(answer(randNums))
print(nums)
print(answer(nums))


