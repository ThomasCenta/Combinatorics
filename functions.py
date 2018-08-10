import helperFunctions as hf
import math

# binomial coefficient is n choose r
def generateBinomialCoefficientTable(maxN, maxK, mod):
    table = []
    for i in range(maxN+1):
        table.append([1]*(maxK+1))
    for i in range(maxN+1):
        for j in range(maxK+1):
            table[i][j] = (table[i-1][j-1]+table[i][j-1]) % mod
    return table

# n choose k, factorials is the list of factorials with size > max(n, k), all % mod
def calculateBinomialCoefficient(n, k, factorials, mod):
    temp = hf.modDivide(factorials[n], factorials[n-k], mod)
    temp = hf.modDivide(temp, factorials[k], mod)
    return temp


def generateFactorials(maxN, mod):
    factorials = [1]*(maxN+1)
    for i in range(1, maxN+1):
        factorials[i] = (factorials[i-1] * i) % mod
    return factorials

# P(n, r) is the number of r permutations of a set of size n (each element unique)
def numPermutations(n, r, factorials, mod):
    if r > n:
        return 0
    return hf.modDivide(factorials(n), factorials(n-r), mod)

def numCircularPermutations(n, r, factorials, mod):
    return hf.modDivide(factorials(n), factorials(n-r)*r, mod)

def numSubsets(n, r, factorials, mod):
    if r > n:
        return 0
    return hf.modDivide(factorials(n), factorials(r)*factorials(n-r) % mod, mod)

def numPermutationsInfiniteMultiset(numUniqueElements, r, mod):
    return pow(numUniqueElements, r, mod)

def numPermutationsFiniteMultiset(n, elementCounts, factorials, mod):
    divisor = 1
    for i in elementCounts:
        divisor = divisor*factorials(i) % mod
    return hf.modDivide(n, divisor, mod)

def numPartitionsOfFiniteMultisetIntoLabelledBoxes(n, elementCounts, factorials, mod):
    divisor = 1
    for i in elementCounts:
        divisor = divisor*factorials(i) % mod
    return hf.modDivide(n, divisor, mod)

def numPartitionsOfFiniteMultisetIntoUnlabelledBoxes(n, elementCounts, factorials, mod):
    divisor = factorials(len(elementCounts))
    for i in elementCounts:
        divisor = divisor*factorials(i) % mod
    return hf.modDivide(n, divisor, mod)

# Stirlings formula. This thing sucks so hard for mods so Im not including it
def approximateFactorial(n):
    return math.sqrt(2*math.pi*n)*pow(n/math.e, n)



def main():
    factorial = 1

main()