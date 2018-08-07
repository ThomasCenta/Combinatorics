
# binomial coefficient is n choose r
def generateBinomialCoefficientTable(maxN, maxK, mod):
    table = []
    for i in range(maxN+1):
        table.append([1]*(maxK+1))
    for i in range(maxN+1):
        for j in range(maxK+1):
            table[i][j] = (table[i-1][j-1]+table[i][j-1]) % mod
    return table
