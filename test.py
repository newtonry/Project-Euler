import math
import time
import itertools
#import numpy

def getPrimesTo(x):
    numlist = range(3, x+1, 2)
    counter = 0
    backup = 0
    for num in numlist:
        counter = backup
        if num != 0:
            counter += num
            while counter <= len(numlist)-1:
                    numlist[counter] = 0
                    counter += num

        backup += 1
    return [2] + [x for x in numlist if x]

def isPandigital(number):
    strNumber = str(number)
    for digit in range(1, len(strNumber)+1):
        if strNumber.count(str(digit)) != 1:
            return False
    return True

def getFactors(n):    
    factors = reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
    factors.sort()
    return set(factors)




###problem 23
##
##numList = range(28124)
##abundNumbers = []
##
###gets the abundant numbers
##for number in range(1,28124):
##    if sum(getFactors(number)) - number > number:
##        abundNumbers.append(number)
##        
###turns numbers that can be written as the sum of 2 abundant numbers into 0
##while abundNumbers != []:
##    for pos in range(0, len(abundNumbers)-1):
##        if (abundNumbers[0]+abundNumbers[pos]) > 28123:
##            break
##            
##        numList[abundNumbers[0]+abundNumbers[pos]] = 0
##    abundNumbers.pop(0)    
##
##print sum(numList)




###problem 15
##
###creates the grid
##grid = []
##for x in range(21):
##    grid.append([])
##    for y in range(21):
##        grid[x].append([])
##
###calculates the paths to each point as a sum of the # of paths to the prior points
##for x in range(21):
##    for y in range(21):
##        pathsToPoint = 0
##
##        if x > 0:
##            pathsToPoint += grid[x-1][y]
##        if y > 0:
##            pathsToPoint += grid[x][y-1]
##
##        if y == 0 or x == 0:
##            pathsToPoint = 1
##            
##        grid[x][y] = pathsToPoint
##
##print grid[20][20]


###problem 24
##z = range(10)
##z = itertools.permutations(z, 10)
##z = list(z)
##z.sort()
##print z[1000000 - 1]


###problem 39
####ansList = [0]*1001
####
####for p in range (1000):
####    count = 0
####    for a in range(p+1):
####        for b in range(p+1):
####            if math.sqrt(a**2 + b**2) == (p - (a + b)):
####                #print a, b, int(math.sqrt(a**2 + b**2))
####                count +=1
####    ansList[p] = count
####
####highP = 0
####highVal = 0
####
####for p in range(1,1001):
####    if ansList[p] > highVal:
####        highP = p
####        highVal = highVal
####
####print highP
####print highVal
##
####ansList = [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 4, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 6, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 8, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 6, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 8, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 8, 0, 4, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 4, 0, 4, 0, 2, 0, 4, 0, 2, 0, 4, 0, 6, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 10, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 8, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 6, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 4, 0, 2, 0, 8, 0, 2, 0, 2, 0, 4, 0, 6, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 4, 0, 4, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 8, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 4, 0, 4, 0, 4, 0, 2, 0, 2, 0, 2, 0, 10, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 4, 0, 4, 0, 2, 0, 4, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 6, 0, 4, 0, 2, 0, 8, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 4, 0, 4, 0, 12, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 6, 0, 4, 0, 4, 0, 2, 0, 4, 0, 6, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 10, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 4, 0, 4, 0, 2, 0, 2, 0, 2, 0, 2, 0, 10, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 4, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 8, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 8, 0, 2, 0, 4, 0, 6, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 8, 0, 2, 0, 4, 0, 2, 0, 2, 0, 6, 0, 4, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 8, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 6, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 8, 0, 2, 0, 2, 0, 10, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 4, 0, 4, 0, 4, 0, 4, 0, 2, 0, 2, 0, 2, 0, 2, 0, 12, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 10, 0, 2, 0, 2, 0, 2, 0, 6, 0, 2, 0, 6, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 4, 0, 2, 0, 6, 0, 4, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 14, 0, 2, 0, 2, 0, 2, 0, 6, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 4, 0, 2, 0, 2, 0, 10, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 4, 0, 6, 0, 2, 0, 2, 0, 2, 0, 2, 0, 10, 0, 4, 0, 4, 0, 2, 0, 2, 0, 2, 0, 8, 0, 2, 0, 2, 0, 4, 0, 6, 0, 2, 0, 4, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 6, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 6, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 18, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 4, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 8, 0, 2, 0, 2, 0, 6, 0, 2, 0, 4, 0, 4, 0, 2, 0, 8, 0, 4, 0, 4, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 10, 0, 2, 0, 2, 0, 2, 0, 2, 0, 6, 0, 6, 0, 2, 0, 2, 0, 6, 0, 6, 0, 2, 0, 12, 0, 2, 0, 4, 0, 4, 0, 2, 0, 2, 0, 8, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 4, 0, 4, 0, 6, 0, 2, 0, 2, 0, 2, 0, 10, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 4, 0, 2, 0, 2, 0, 2, 0, 4, 0, 2, 0, 4, 0, 4, 0, 4, 0, 10, 0, 4, 0, 2, 0, 4, 0, 2, 0, 0]
####
####
####highP = 0
####highVal = 0
####
####for p in range(1,1001):
####    if ansList[p] > highVal:
####        highP = p
####        highVal = ansList[p]
####
####print highVal
####print highP




###problem 29
##
##ansList = []
##for a in range (2,101):
##    for b in range (2,101):
##        ansList.append(a**b)
##        
##ansList = set(ansList)
##print len(ansList)





###problem 38
##number = 1
##while True:
##    concatStr = ''
##    n = 1
##    
##    while len(concatStr) < 10:
##        concatStr += str(n * number)
##
##        if len(concatStr) == 9:
##            thing = True
##            for digit in concatStr:
##                if concatStr.count(digit) != 1 or digit is '0':
##                    concatStr ='000000000000000000'
##                    thing = False
##                    break
##            if thing is True:                
##                print number
##                print concatStr
##        n += 1
##    number += 1



##
##lines = open('keylog.txt').read().splitlines()
##
##lines = sorted(set(lines))
##
###print lines
##
##for numIndex, number in enumerate(lines):
##    for otherIndex, otherNumber in enumerate(lines):
##        if number is not otherNumber:
##            #checking to see if the last two numbers on are the first of any other number or vice versa
##            if number[:2] in otherNumber[-2:]:
##                lines[numIndex] = otherNumber + number[-1]
##                lines.pop(otherIndex)
##            elif number[-2:] in otherNumber[:2]:
##                lines[numIndex] = number + otherNumber[-1]
##                lines.pop(otherIndex)
##
##
##print lines
##
##for numIndex, number in enumerate(lines):
##    for otherIndex, otherNumber in enumerate(lines):
##        if number is not otherNumber:
##            #checking to see if the last two numbers on are the first of any other number or vice versa
##            if number[0] in otherNumber[-1]:
##                lines[numIndex] = otherNumber + number[1:]
##                lines.pop(otherIndex)
##            elif number[-1] in otherNumber[0]:
##                lines[numIndex] = number + otherNumber[1:]
##                lines.pop(otherIndex)
##
##
##
##
##print ''
##print ''
##ans = ''
##for line in lines:
##    ans +=line
##
##print ans
##print len(ans)
##
##test=0
##for letter in ans:
##    test+=1
            
##z =['1','2','3','4']
##
##for ndx,test in enumerate(z):
##    z[ndx] = test + str(1)
##       
##print z

    #print number[1:3]
   # print number[0:2]

##ways = {}
##
##ways[1] = [1]
##ways[2] = [[1,1],[2]]
##ways[5] = []
##
##for x in range(5/2):
##    ways[5] += [ways[2]]
##
##ways[5] += [ways[5%2]]
##
##optionsArray =[]
##for way in ways[5]:
##    for item in way:
##        print item
##

#print ways[5]

    
##ans=[]
##for each in [2,4,2]:
##    for peach in [3,5,2]:
##        ans.append(str(each) + str(peach))
##
##ans = sorted(set(ans))
##
##print ans


##ans={}
##done = []
##
##for p in range(1,1000):
##    ans[p] = 0
##    for a in range(1,p):
##        for b in range(1,p):
##            if [a,b] not in done and [b,a] not in done:
##                c = math.sqrt(a**2 + b**2)
##                if c == int(c) and (a + b + c == p):
##                    done.append([a,b])
##                    ans[p] += 1
##                elif c != int(c):
##                    done.append([a,b])
##                elif (a + b + c) > p:
##                    break
##
##print ans


##
##
##primes = getPrimesTo(100000000)
##primes.sort()
##print "Primed and ready to go"
##
##
##tot = 1
##totalCorners = 1.0
##primesCount = 0.0
##
##
##
##for x in range (3,100000000, 2):
####    print x**2
####    print (x**2 - (x - 1))
####    print (x**2 - 2*(x-1))
####    print (x**2 - 3*(x-1))
####
##
##
##
##
##    if (x**2 - 3*(x-1)) in primes:
##        primesCount += 1
##    if (x**2 - 2*(x-1)) in primes:
##        primesCount += 1
##    if (x**2 - (x - 1)) in primes:
##        primesCount += 1
##    if x**2 in primes:
##        primesCount += 1
##
##
##    for prime in primes:
##        if prime <= x**2:
##            primes.remove(prime)
##        if prime > x**2:
##            break
##
##    print len(primes)
##    totalCorners += 4.0
##
##
###    print primesCount/totalCorners
##
##    if primesCount/totalCorners < .1 and totalCorners > 10:
##        print 'The answer is: ' + str(x)
##        break
##
##
##print primesCount
##print totalCorners
##
##
##   # tot += 4*(x**2) - 6*(x-1)




##number = 16807
##
##ans = 0
##for number in range(1,10000000):
##    nthRoot = len(str(number))
##    guess = math.sqrt(number) * number
##
##    for z in range(100):
##        guess = ((nthRoot -1)*guess + number/(guess**(nthRoot - 1)))/nthRoot
##        if guess == ((nthRoot -1)*guess + number/(guess**(nthRoot - 1)))/nthRoot:
##            break
##
##    if int(guess) == guess:
##        #print guess
##        ans += 1
##
##print ans


##ans = 0
##
##for x in range(2,10):
##    n = 0
##    going = True
##    while going:
##        n+=1
##        if len(str(x**n)) == n:
##            ans += 1
##            print x**n
##        elif len(str(x**n)) > n:
##            going = False
##
##print ans


##for n in range(1000000):
###    print len(str(2**n))
##    if len(str(2**n)) == n:
##        print n
##
##




###problem 46
##primes = getPrimesTo(100000)
##print 'Primes acquired'
##
##squaresDoubled = []
##
##for x in range(1,1000):
##    squaresDoubled.append( 2 * x * x)
##
##
##for number in range(4,100000):
##    if number not in primes and number%2 != 0:
##        possible = True
##        for subt in squaresDoubled:
##            if number - subt in primes:
##              #  print number
##                possible = False
##                break
##
##        if possible:    
##            print str(number) + " IS THE ANSWER"
##            break



###problem 52
##going = True
##x = 10
##
##while going:
##    x += 1
##    if len(str(x)) != len(str(x*6)):
##        x = int('1' + len(str(x))*'0')
##        
##    xSorted = "".join(sorted(str(x)))
##
##    #I'm sure there's a pretty way to write the line, or do it in a loop, but this got the answer
##    if "".join(sorted(str(x*2))) == xSorted and "".join(sorted(str(x*3))) == xSorted and "".join(sorted(str(x*3))) == xSorted and "".join(sorted(str(x*4))) == xSorted and  "".join(sorted(str(x*5))) == xSorted and "".join(sorted(str(x*6))):
##        going = False    
##print x




##def getPentsTo(x):
##    pents = [1]
##    n = 1
##    while pents[-1] < x:
##        n +=1
##
##        for pent in pents:
##            if (n*(3*n - 1)/2 - pent) in pents and (n*(3*n - 1)/2 + pent) in pents:
##                print n*(3*n - 1)/2 - pent
##                return n*(3*n - 1)/2 - pent
##        pents.append(n*(3*n - 1)/2)
##        
##    return pents


###problem 45
##triNums = []
##pentNums = []
##hexNums = []
##
##for x in range (1,100000):
##    triNums.append(x*(x+1)/2)
##
##
##maxVal = triNums[-1]
##
##
##
##
##
##
##for x in range(1,100000):
##    if x*(3*x - 1)/2 < maxVal:
##        pentNums.append(x*(3*x - 1)/2)
##    if x*(2*x-1) < maxVal:
##        hexNums.append(x*(2*x-1))
##        
###apparently this set() is useful
##print(set(triNums) & set(pentNums) & set(hexNums))
##
##
#####brute force way
####for number in triNums:
####    if number in pentNums and number in hexNums:
####        print number



###problem 67
###same solution as 18 pretty much
##
##f = open('triangle.txt')
##lines = f.readlines()
##f.close()
##
###definitely a better way to grab the content, but this worked
##content = []
##for line in lines:
##    line = line.replace('\n', '').split(" ")
##    content.append(line)
##    for number in line:
##        number = int(number)
##for line in content:
##    for x in range(len(line)):
##        line[x] = int(line[x])
##
##print 'Got the content arranged'
##
##
###ugly to read, but w/e
##for lineNum in range(1,len(content)):
##    for numPos in range(len(content[lineNum])):    
##        #compare content[lineNum -1][numPos] and content[lineNum-1][numPos + 1]
##
##       # print content[lineNum][numPos]
##        if numPos == 0: #for left edge numbers
##            content[lineNum][numPos] += content[lineNum -1][numPos]
##
##        elif numPos == len(content[lineNum]) - 1: # for right edge
##            content[lineNum][numPos] += content[lineNum-1][numPos - 1]
##
##        elif content[lineNum -1][numPos-1] > content[lineNum-1][numPos]:
##            content[lineNum][numPos] += content[lineNum -1][numPos-1]
##
##        elif content[lineNum -1][numPos-1] < content[lineNum-1][numPos]:
##            content[lineNum][numPos] += content[lineNum-1][numPos]
##
##        elif content[lineNum -1][numPos-1] == content[lineNum-1][numPos]:
##            content[lineNum][numPos] += content[lineNum-1][numPos]
##
##
##print max(content[lineNum])







###problem 18
##
##f = open('prob18.txt')
##lines = f.readlines()
##f.close()
##
###definitely a better way to grab the content, but this worked
##content = []
##for line in lines:
##    line = line.replace('\n', '').split(" ")
##    content.append(line)
##    for number in line:
##        number = int(number)
##for line in content:
##    for x in range(len(line)):
##        line[x] = int(line[x])
##
##
###ugly to read, but w/e
##for lineNum in range(1,len(content)):
##    for numPos in range(len(content[lineNum])):    
##        #compare content[lineNum -1][numPos] and content[lineNum-1][numPos + 1]
##
##       # print content[lineNum][numPos]
##        if numPos == 0: #for left edge numbers
##            content[lineNum][numPos] += content[lineNum -1][numPos]
##
##        elif numPos == len(content[lineNum]) - 1: # for right edge
##            content[lineNum][numPos] += content[lineNum-1][numPos - 1]
##
##        elif content[lineNum -1][numPos-1] > content[lineNum-1][numPos]:
##            content[lineNum][numPos] += content[lineNum -1][numPos-1]
##
##        elif content[lineNum -1][numPos-1] < content[lineNum-1][numPos]:
##            content[lineNum][numPos] += content[lineNum-1][numPos]
##
##        elif content[lineNum -1][numPos-1] == content[lineNum-1][numPos]:
##            content[lineNum][numPos] += content[lineNum-1][numPos]
##
##
##    print content[lineNum]


###problem 42
##def getTriangleNumsTo(limit):
##    triangleList = []
##    n = 1
##    triNum = 0
##    while triNum <= limit:
##        triNum = n*(n+1)/2
##        triangleList.append(triNum)
##        n += 1
##    return triangleList
##
##
##triangleList = getTriangleNumsTo(364)
##
##f = open('words.txt')
##words = f.read()
##f.close()
##
##words = words.replace('"', '').split(",")
##letterVal = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
##
##ans = 0
##
##for word in words:
##    letterSum = 0
##    for letter in word:
##        letterSum += letterVal[letter] + 1
##
##    if letterSum in triangleList:
##        ans += 1
##
##
##print ans
##
##
####highLen = 0
####
####for word in words:
####    if len(word) > highLen:
####        highLen = len(word)
####
####print highLen * 26 # highest value is 364



###problem 40
##startPos = 10
##
##ansArray = []
##rightOnes = [10,100,1000,10000,100000,1000000]
##
##number = 9
##string = ''
##going = True
##
##
##while going is True:
##    number +=1 
##    string += str(number)
##
##    for character in str(number):
##        if startPos in rightOnes:
##            ansArray.append(int(character))
##            if startPos == 1000000:
##                going = False
##                break
##        
##        startPos +=1
##print ansArray


##size = 3
##
##
##x = range(size)
##y = range(size)
##
##grid = {}
##
###generates all the nodes
##for count in range (size):
##    for count2 in range(size):
##        grid[str(x[count]) + ',' + str(y[count2])] = 0
##
##
###for each in grid:
###    coordinates = each.rsplit(',')
###    print coordinates[each]
##
##for y in range(size):
##    for x in range (size):
##        pathsTo = 1
##        if x > 0:
##            pathsTo += grid[str(x - 1) + ',' + str(y)]
##        if y > 0:
##            pathsTo += grid[str(x) + ',' + str(y - 1)]
##        
##        grid[str(x) + ',' + str(y)] = pathsTo
##        print str(x) + ',' + str(y) + ': ' + str(pathsTo)
##        
##
##print grid[str(size - 1) + ',' + str(size - 1)]/size


###problem 21
##numberList = {}
##
##for number in range(1,10000):
##    divSum = 0
##    for div in range(2, int(math.sqrt(number))+1):
##        if number%div == 0:
##            divSum += div
##            if number/div != div:
##                divSum += number/div
##    numberList[number] = divSum + 1
##
##
##
##ans = 0
##
##for number in numberList:
##    thisSum = numberList[number]
##    if thisSum < 10000 and thisSum != number:
##        if number == numberList[thisSum]:
##            ans += number
##
##print ans

###problem 14
###soltuion by memorizing what has already been calculated
##hitOffNumbers = {}
##
##def getToOne(number):
##
##    count = 0
##    while number != 1:
##
##        if number in hitOffNumbers:
##            return hitOffNumbers[number] + count
##        
##        elif number%2 == 0:
##            number = number/2            
##        else:
##            number = 3 * number + 1
##    
##        count += 1 
##
##    return count
##
##
##
##highCount = 0
##highNum = 0
##
##
##
##
##for number in range(1,1000000):
##
##
##    count = getToOne(number)
##    hitOffNumbers[number] = count
##
##    if count > highCount:
##        highCount = count
##        highNum = number
##
##print highCount
##print highNum
##




###primes = getPrimesTo(1000000)
###print 'Got Primes'
##
### well this is another solution to 12, which works a lot better, due to the line
###return (sr*sr == n) + 2*sum(n%i == 0 for i in xrange(1,sr))
##
##
##def triangles():
##    term, sum = 1, 0
##    while True:
##        term, sum = term+1, sum+term
##        yield sum
##
##def ndivisors(n):
##    from math import sqrt
##    sr = int(sqrt(n))
##    return (sr*sr == n) + 2*sum(n%i == 0 for i in xrange(1,sr))
##
##
##for t in triangles():
##    if ndivisors(t) > 50:
##        break
##    
##print ndivisors(t), t
##
##
##
##x = 2
##print sum( z%2 == 0 for z in range(1, 11))
##

###problem 12
##divDict = {}
##
##def divisorCount(number):
##
##    if number in divDict:
##        return divDict[number]
##    
##    divList = []
##    for divisor in range(2, number/2 +1):
##        if number % divisor == 0:
##            if divisor not in primes:
##                underDivList = divisorCount(divisor)
##                for each in underDivList:
##                    divList.append(divisor)
##            else:
##                divList.append(divisor)
##
##    divList.append(1)
##    divList.append(number)
##    divList = sorted(set(divList))
##
##    divDict[number] = divList
##    return divList
##
##
##currentNum = 1
##increment = 2
##found = False
##while found is False:
##    currentNum += increment
##    increment += 1
##
##    divCount = divisorCount(currentNum)
##    if len(divCount) > 500:
##        print currentNum
##        found = True
##
##
##



###problem 34
##factorialDict = {}
##
##for x in range(0,10):
##    factorialDict[x] = math.factorial(x)
##
##
##
##for number in range(10000000):
##    total = 0
##    for letter in str(number):
##        total += factorialDict[int(letter)]
##        if total > number:
##            break
##    if total == number:
##        print number
##
##

##
###problem 37
##def getPrimesTo(x):
##    numlist = range(3, x+1, 2)
##    counter = 0
##    backup = 0
##    for num in numlist:
##        counter = backup
##        if num != 0:
##            counter += num
##            while counter <= len(numlist)-1:
##                    numlist[counter] = 0
##                    counter += num
##
##        backup += 1
##    return [2] + [x for x in numlist if x]
##
##
##primes = getPrimesTo(1000000)
##print 'Got Primes'
##
##def testTrunc(prime):
##    primeStr = str(prime)
##    isTrunc = True
##
##    for x in range(1, len(primeStr)):
##        if int(primeStr[:-x]) not in primes or int(primeStr[x:]) not in primes:
##            isTrunc = False
##            break
##
##    return isTrunc
##
##
##
##ansList = []
##
##for prime in primes:
##
##    if testTrunc(prime) is True:
##        if prime > 10:
##            ansList.append(prime)
##
##print ansList
##print sum(ansList)
##
##
##
##



##
###problem 35
##
##def getNumbersCircle(number):
##    numbersCircle = []
##    nextNum = number
##
##    for x in range(len(str(number))):
##        nextNum = int(str(nextNum)[-1] + str(nextNum)[:-1])
##        numbersCircle.append(nextNum)
##    return numbersCircle
##
##
##
##primes = getPrimesTo(1000000)
##
##
##primesSubList = [[],[],[],[],[],[],[]]
##primesSubList[1] = [] #for primes with 1 digits
##primesSubList[2] = [] #for primes with 2 digits
##primesSubList[3] = []
##primesSubList[4] = []
##primesSubList[5] = []
##primesSubList[6] = [] #for primes with 6 digits
##
##
##
##ansList = []
##
##
##for prime in primes:
##    numDigits = len(str(prime))
##    primesSubList[numDigits].append(prime)
##
##
##for numDigits in range(1, 7):
##    for number in primesSubList[numDigits]:
##        numberCircle = getNumbersCircle(number)        
##        circular = True
##        for circle in numberCircle:
##            if circle not in primesSubList[numDigits]:
##                circular = False
##                break
##            
##        if circular is True:
##            ansList.append(number)
##
##print len(ansList)
##



##for numDigits in range(1, 7):
##
##    for x in range(len(primesSubList[numDigits])):
##        arr = []
##        for number in str(primesSubList[numDigits][x]):
##            arr.append(number)
##
##        arr.sort()
##        primesSubList[numDigits][x] = arr
##
##    for prime in primesSubList[numDigits]:
##
##        if len(prime) == 1 and primesSubList[numDigits].count(prime) == 1:
##            ansList.append(prime)
##         #   print prime
##
##        elif len(prime) == 2 and primesSubList[numDigits].count(prime) > 1:
##            ansList.append(prime)
         #   print prime
            
##        elif len(prime) == 3 and primesSubList[numDigits].count(prime) > 2:
##            ansList.append(prime)
##           # print prime
##        elif len(prime) == 4 and primesSubList[numDigits].count(prime) > 3:
##            ansList.append(prime)
##        elif len(prime) == 5 and primesSubList[numDigits].count(prime) > 4:
##            ansList.append(prime)
##        elif len(prime) == 6 and primesSubList[numDigits].count(prime) > 5:
##            ansList.append(prime)
##
##print ansList    
##print len(ansList)    
##
##
##
##
##
##
##print getNumbersCircle(56789)

#print primesSubList[2]
        

##
##test =['a','b', 'c']
##test2 =['a','b', 'c']
##
##test3 = [test, test2]
##
##
##print test3.count(['a','b', 'c'])
##
##








###problem 32
###not the most efficient answer certainly
##productList = []
##
##for num1 in range(1, 1000):
##    for num2 in range(1, 10000):
##        stringNum = str(num1) + str(num2) + str(num1 * num2)
##        if len(stringNum) == 9:
##            doesWork = True
##            for x in range(1,10):
##                if str(x) not in stringNum:
##                    doesWork = False
##                    break
##            if doesWork:
##                #print stringNum
##                print str(num1) + ' x ' + str(num2) + ' = ' + str(num1*num2)
##
##                product = num1*num2
##                if product not in productList:
##                    productList.append(product)
##
##print sum(productList)
##
##
##
##
###problem 28
###I just took a look at how each diagonal differs each row and came up with the following pattern:
##
##tot = 1
##for x in range (3,1002, 2):
##    ##x**2 + (x**2 - (x - 1)) + (x**2 - 2*(x-1)) + (x**2 - 3*(x-1))
##    tot += 4*(x**2) - 6*(x-1)
##print tot



###problem 30
##ans = 0
##
##for x in range(2, 1000000):
##    sum = 0
##    for number in str(x):
##        sum += int(number)**5
##
##    if sum == x:
##        print x
##        ans += x
##
##print ans
##
##
###problem 26
####The way I viewed the problem was based on how 'long division' is performed.
####I kept storing the remainders, and as a pattern of remainders had occurred twice,
####you would know that it's stuck in a loop of that pattern.
##
##def getPattern(x):
##    rem = 10%7
##    for times in range(10): #gets rid of non pattern starts
##        rem = (rem * 10)%x
##
##    patternList = str(rem)
##
##    while True:
##        rem = (rem * 10)%x
##        patternList += str(rem)
##
##        lenList = len(patternList)
##
##        
##
##        if patternList[:(lenList/2)] == patternList[lenList/2:]:
##            return patternList[:(lenList/2)]
##            break
## #       print patternList
##
##  #      print 'patternlist1 ' + str(patternList[:(lenList/2)])
##  #      print 'patternlist2 '+ str(patternList[lenList/2:])

##
##longestPatNum = 0
##longestPat = 0
##
##for number in range(1,1000):
##    length = len(getPattern(number))
##
##    if length > longestPat:
##        longestPatNum = number
##        longestPat = length
##
##
##print longestPatNum
##print longestPat
##


#print 1.6180339887**12 /math.sqrt(5)


#problem 25 using fibonacci formula
#count = 1
#while len(str(int(1.6180339887**count /math.sqrt(5)))) < 1000:
#     count +=1



#print len(1.6180339887**472 /math.sqrt(5))

###problem 25
##val1 = 1
##val2 = 1
##
##termN = 2
##
##while len(str(val2)) < 1000:
##    temp = val1 + val2
##    val1 = val2
##    val2 = temp
##
##    termN +=1
##
##print termN


##start = time.time()
##
##
###problem 12? incomplete
##def getPrimesTo(x):
##    numlist = range(3, x+1, 2)
##    counter = 0
##    backup = 0
##    for num in numlist:
##        counter = backup
##        if num != 0:
##            counter += num
##            while counter <= len(numlist)-1:
##                    numlist[counter] = 0
##                    counter += num
##
##        backup += 1
##    return [2] + [x for x in numlist if x]

#primes = getPrimesTo(1000)

#print primes

#print format(1.0/3.0, '.100f')


##
##def getDivs(number):
##                    
##    divList = range (int(math.sqrt(number)))
##    if 
##
##
##getDivs(10000)
##
##
##
##
##end = time.time()
##print "Time:", end - start
##
####
####def getDivs(number):
####    divList = [1]
####    primes = getPrimesTo(int(math.sqrt(number)) + 1)
####    
####    for prime in primes:
####        if number%prime == 0:
####            div = number/prime
####            if prime not in divList:
####                divList.append(prime)
####        #    if div not in divList:
####      #         divList.append(number/prime)
####            if div not in primes and div not in divList:
####                factors = getDivs(div)
####                for factor in factors:
####                    if factor not in divList:
####                        divList.append(factor)
####                    
####    divList.append(number)
####    return divList
##
###print len(getDivs(40000000000))
##
###ans = getDivs(100)
###ans.sort()
###print ans
###print len(getDivs(100))
##
##
###def removeDuplicates(numbers):
###    for number in number 
##
##
##def getFiveHundred(currentNum, nextIncrement):
##    currentNum += nextIncrement
##
##    numDivs =len(getDivs(currentNum))
##    print str(currentNum) + ' has #divs ' + str(numDivs)
##
##    if  numDivs > 50:
##        print currentNum
##    else:
##        getFiveHundred(currentNum, nextIncrement + 1)
##
#getFiveHundred(1,2)

#print unique(2,3,4)

#getDivCount(20)


##
###problem 10
##
###other way to get primes; works by removing all multiples of primes
###so no comparisons vs them are needed, saving a lot of time
###removes all multiples of whatever counter is by turning them into 0's
##
##def getPrimesToX(x):
##    numlist = range(3, x+1, 2)
##    counter = 0
##    backup = 0
##    for num in numlist:
##        counter = backup
##        if num != 0:
##            counter += num
##            while counter <= len(numlist)-1:
##                    numlist[counter] = 0
##                    counter += num
##
##        backup += 1
##    return [2] + [x for x in numlist if x]
##
##
##
##
##
##
##
##
##


##def getPrimesUpTo(limit):
##    x=5
##    primes = [2,3]
##    while x <= limit:
##        
##        isPrime = True        
##
##        for prime in primes:
##            if x%prime == 0:
##                 isPrime = False
##                 break
##    
##        if isPrime is True:
##            primes.append(x)
##        x += 2
##
##    return primes
##
##
##print sum(getPrimesUpTo(2000000))





##names = ['SAM','BOB','KATHERINES', 'KATHY']
##names.sort()
##
##print names



##
###problem 22
###haha, after completing this, I just read there's a .sort() method >_<.  Mine definitely wasn't the most efficient sort anyways
##
##f = open('names.txt')
##names = f.read()
##f.close()
##
##arrangedNames = ['ZZZZZZZZ']
##
##names = names.replace('"', '').split(",")
##letterVal = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
##
##
###names = ['SAM','BOB','KATHERINES', 'KATHY']
##
##
##for name in names:
##        letPos = 0
##        namePos = 0
##        isSorted = True
##     #   print name
##        while isSorted:
##                if letterVal[name[letPos]] < letterVal[arrangedNames[namePos][letPos]]:
##                        arrangedNames.insert(namePos, name)
##                        isSorted = False
##                        
##                elif letterVal[name[letPos]] > letterVal[arrangedNames[namePos][letPos]]:
##                        namePos += 1
##                        letPos = 0
##
##                else:
##                        letPos +=1
##                        if letPos == len(arrangedNames[namePos]):
##                                namePos +=1
##                                letPos = 0
##                        elif letPos == len(name):
##                                arrangedNames.insert(namePos, name)
##                                isSorted = False
##        
##
##total = 0
##
##for x in range(len(arrangedNames) - 1):
##        letterTotal = 0
##        for letter in arrangedNames[x]:
##                letterTotal += letterVal[letter] + 1
##
##        total += (letterTotal * (x+1))
##
##print total


##test = 0
##
##for letter in arrangedNames[937]:
##        test += letterVal[letter] + 1
##
##print test * 938




#print arrangedNames



##alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".replace(' ', '').upper()
##
##string = ''
##for x in range (26):
##        string += ', "' + alphabet[x] + '":'+ str(x) 
##
##print string

##
##total = 0
##totalTwo = 0
##totalThree = 0
##
##for x in range(0,2000000,3):
##        totalThree += x
##
##
##for x in range(0,2000000,2):
##        totalTwo += x
##
##
##for x in range(20000001):
##        total += x
##
##print totalThree
##print totalTwo
##print total
##
##print total-totalTwo


###problem 20
##totalStr = str(math.factorial(100))
##
##ans = 0
##
##for number in totalStr:
##    ans += int(number)
##        
##print ans






#problem  19


##month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
##dayCounter = 2 #starting with Tuesday Jan 1 1901
##
##sunFirstCount = 0
##
##for year in range(1,101):    
##    for mon in range (1,13):
##        if dayCounter%7 == 0:
##            sunFirstCount += 1
##            
##        dayCounter += month[mon]
##        if year%4 == 0 and mon == 2:
##            dayCounter +=1
##
##            
##print sunFirstCount




##
###problem 17
###print len('threehundredandfortytwo')
##
##numTable = {0:'',1: 'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}
##
##
##def wordConvert(number): #up to 99
##    strNum = str(number)
##
##    if number < 21:##
##        return len(numTable[number])
##    else:
##        return len(numTable[int(number/10) * 10]) + len(numTable[int(strNum[1])])
##
##
##ninetyNineTotal = 0
##
##for x in range(100):
##    ninetyNineTotal += wordConvert(x)
##
##
##ans = 10 * ninetyNineTotal 
##
##for hund in range(1,10): #covers everything between 100-999
##    ans += 100*(wordConvert(hund) + wordConvert(100)) + (99*len('and'))
##
##ans += len('onethousand')
##
##print ans






##
###problem 16
##total = str(2**1000)
##totLen = len(total)
##
##ans = 0
##
##for x in range (totLen):
##    ans += int(total[x])
##
##print ans




###problem 9
##a=1
##b=1
##
##
##for a in range (1,500):
##  for b in range (1,500):
##    if (math.sqrt(a**2 + b**2)%int(math.sqrt(a**2 + b**2)) == 0.0):
##      #print str(a) + ',' + str(b), str(math.sqrt(a**2 + b**2))
##      if (a + b + math.sqrt(a**2 + b**2)) == 1000:
##        print str(a) + ',' + str(b), str(math.sqrt(a**2 + b**2))
##
##    b +=1
##  a +=1
##  
##print 200 * 375 * 425
##





#####problem 13
##f = open('num')
##lines = f.readlines()
##f.close()
##
##length = len(lines)
##
##sumVal = 0
##
##for number in lines:
##  number = int(str(number[:15]))
##  sumVal+= number
##
##print str(sumVal)[0:10]
##
###print len ('5537376230')





##
##def isTriangle(number):
##    subNum = 1
##    while number > 0:
##        number -= subNum
##        subNum +=1
##    if number == 0:
##        return True
##    else:
##        return False
##
##


###problem 12? incomplete
##
##def getDivCount(number):
##    divCount = 0
##    for x in range(1, number/2 + 1):
##        if number%x == 0:
##            divCount +=1
##    return divCount + 1
##
##
##
##
##def getFiveHundred(currentNum, nextIncrement):
##    currentNum += nextIncrement
##
##    if getDivCount(currentNum) > 500:
##        print currentNum
##    else:
##        getFiveHundred(currentNum, nextIncrement + 1)
##
##
##
##print getDivCount(1000000000)
##
##
###getFiveHundred(1, 2)
##
##
###print getDivCount(105)
##
##
##
####triNumArr=[1]
####nextLine = 2
####
####cont = True
####
####while cont:
####    triNumArr.append(triNumArr[-1] + nextLine)
####    nextLine += 1
####
####
####    if nextLine == 40:
####        cont = False
##
###print triNumArr
##
##





    


##
###problem11
####
####inp1 = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'
####inp2 = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'
####inp3 ='81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'
####inp4 ='52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'
####inp5 ='22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'
####inp6 ='24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'
####inp7 ='32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'
####inp8 ='67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'
####inp9 ='24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'
####inp10 ='21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'
####inp11 ='78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'
####inp12 ='16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'
####inp13 ='86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'
####inp14 ='19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'
####inp15 ='04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'
####inp16 ='88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'
####inp17 ='04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'
####inp18 ='20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'
####inp19 ='20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'
####inp20 ='01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
####
##
##
##inp1 = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 00 00 00 00'
##inp2 = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 00 00 00 00'
##inp3 ='81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 00 00 00 00'
##inp4 ='52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 00 00 00 00'
##inp5 ='22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 00 00 00 00'
##inp6 ='24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 00 00 00 00'
##inp7 ='32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 00 00 00 00'
##inp8 ='67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 00 00 00 00'
##inp9 ='24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 00 00 00 00'
##inp10 ='21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 00 00 00 00'
##inp11 ='78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 00 00 00 00'
##inp12 ='16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 00 00 00 00'
##inp13 ='86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 00 00 00 00'
##inp14 ='19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 00 00 00 00'
##inp15 ='04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 00 00 00 00'
##inp16 ='88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 00 00 00 00'
##inp17 ='04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 00 00 00 00'
##inp18 ='20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 00 00 00 00'
##inp19 ='20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 00 00 00 00'
##inp20 ='01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 00 00 00 00'
##inp21 ='00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
##inp22 ='00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
##inp23 ='00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
##inp24 ='00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
##
##
##def convert( inpStr ):
##
##    pos = 0
##    retArr = []
##    for number in range (24):
##       retArr.append(int(inpStr[pos:pos+2]))
##       pos +=3
##
##    return retArr
##
##massArr = []
##massArr.append(convert(inp1))
##massArr.append(convert(inp2))
##massArr.append(convert(inp3))
##massArr.append(convert(inp4))
##massArr.append(convert(inp5))
##massArr.append(convert(inp6))
##massArr.append(convert(inp7))
##massArr.append(convert(inp8))
##massArr.append(convert(inp9))
##massArr.append(convert(inp10))
##massArr.append(convert(inp11))
##massArr.append(convert(inp12))
##massArr.append(convert(inp13))
##massArr.append(convert(inp14))
##massArr.append(convert(inp15))
##massArr.append(convert(inp16))
##massArr.append(convert(inp17))
##massArr.append(convert(inp18))
##massArr.append(convert(inp19))
##massArr.append(convert(inp20))
##massArr.append(convert(inp21))
##massArr.append(convert(inp22))
##massArr.append(convert(inp23))
##massArr.append(convert(inp24))
##
##
##
###horizontally
##maxHoz = 0
##maxVer = 0
##maxR = 0
##maxL = 0
##
##
##for r in range (20):
##    for s in range (20):
##        prod = massArr[r][s] * massArr[r][s+1] * massArr[r][s+2] * massArr[r][s+3]
##        if prod > maxHoz:
##            maxHoz = prod
##            #print massArr[r][s]
##            #print maxHoz
##
##
##for r in range (20):
##    for s in range (20):
##        prod = massArr[s][r] * massArr[s+1][r] * massArr[s+2][r] * massArr[s+3][r]
##        if prod > maxVer:
##            maxVer = prod
##            #print massArr[s][r]
##            #print maxVer
##
##
##
##for r in range (20):
##    for s in range (20):        
##        prod = massArr[s][r] * massArr[s+1][r+1] * massArr[s+2][r+2] * massArr[s+3][r+3]
##        if prod > maxR:
##            maxR = prod
##            #print maxVer
##
##for r in range (20):
##    for s in range (20):        
##        prod = massArr[s][r] * massArr[s-1][r+1] * massArr[s-2][r+2] * massArr[s-3][r+3]
##        if prod > maxL:
##            maxL = prod
##            print massArr[s][r]
##            #print maxVer
##
##
##
##print maxHoz
##print maxVer
##print maxR
##print maxL
##
##
##

##
###problem8
##number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
##
##numberString = str(number)
##
##maxNum = 0
##maxProduct = 0
##
##for pos in range (1000-5):
##    fiveDig = numberString[pos:pos+5]
##
##    currentProduct = 1
##    for x in range (5):
##        currentProduct = currentProduct * int(fiveDig[x])
##
##    if currentProduct > maxProduct:
##        maxProduct = currentProduct
##        maxNum = fiveDig
##        #print maxProduct
##    
##print maxNum
##print maxProduct

#problem7
##number = 20
##
##val = 3
##
##pList =[2,val]
##
##lenList = len(pList)
##
###while val < number:
##while lenList < 10002:
##    lenList = len(pList)
##    
##    val += 2
##
##    isPrime = True
##    sqrtVal = math.sqrt(val)
##
##    for x in pList:
##        
##        if x > sqrtVal:
##            break
##        if val%x is 0:
##            isPrime = False
##            break
##    if isPrime:
##        pList.append(val)
##        #print val
##
##print pList[10000]








###problem 6
##x = 0
##y = 0
##
##for num in range (101):
##    x += num**2
##    y += num
##
##print y**2
##print x
##print y**2 - x




###problem5
##numbersToCheck = range (11, 20)#[19, 17, 16, 15, 14, 13, 12, 11]
##
##val = 20
##
##found = False
##
##while found is False:
##    val += 20
##    found = True
##    for number in numbersToCheck:
##        if val%number != 0:
##            found = False
##            break
##print val





###problem4
##x=999
##y=999
##
##highestVal = 0
##
##for x in reversed(range(999)):
##    for y in reversed(range(999)):
##        num = x*y
##        if num == int(str(num)[::-1]):
##            if num > highestVal:
##                highestVal = num
##                print highestVal
##            break
##
##
##















##
####value1= 1
####value2 = 2
#####print value1
#####print value2
####
####totalSum = 2
####
####for x in range (40):
####    temp = value1 + value2
####    value1 = value2
####    value2 = temp
####
####    if temp > 4000000:
####        break
####
####
####    if temp%2 is 0:
####        totalSum += temp
####print totalSum
##
##
##number = 600851475143
##
##
##sqrtNum = int(math.sqrt(number))
##
###print sqrtNum
##
####for x in range (2, sqrtNum):
####    if number%x is 0:
####        print number/x
####
####print 'Done'
##
##x=3
##
##while x < sqrtNum:
##    if number%x == 0:
##        print x
##    
##
##    x+=2
##
##print 'Done'
##
##
##
##
###val = 3
##
####pList =[2,val]
####
####
####while val < number:
####    val += 2
####
####    isPrime = True
####    sqrtVal = math.sqrt(val)
####
####    for x in pList:
####        
####        if x > sqrtVal:
####            break
####        if val%x is 0:
####            isPrime = False
####            break
####    if isPrime:
####        pList.append(val)
####        print val
####
####
####print pList
