import math
import time


#problem 26
##The way I viewed the problem was based on how 'long division' is performed.
##I kept storing the remainders, and as a pattern of remainders had occurred twice,
##you would know that it's stuck in a loop of that pattern.

def getPattern(x):
    rem = 10%7
    for times in range(10): #gets rid of non pattern starts
        rem = (rem * 10)%x

    patternList = str(rem)

    while True:
        rem = (rem * 10)%x
        patternList += str(rem)

        lenList = len(patternList)

        

        if patternList[:(lenList/2)] == patternList[lenList/2:]:
            return patternList[:(lenList/2)]
            break
 #       print patternList

  #      print 'patternlist1 ' + str(patternList[:(lenList/2)])
  #      print 'patternlist2 '+ str(patternList[lenList/2:])


longestPatNum = 0
longestPat = 0

for number in range(1,1000):
    length = len(getPattern(number))

    if length > longestPat:
        longestPatNum = number
        longestPat = length


print longestPatNum
print longestPat



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
