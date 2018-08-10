def getRightmostCharacterSmallerThanNext(str):
    for i in reversed(range(len(str)-1)):
        if str[i] < str[i+1]:
            return i
    return -1

# insertion sort in range [l, r)
def sort(arr, l, r):
    i = l
    while i < r:
        j = i
        while j > l and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1
        i += 1

# Find the ceil of 'first char' in right of first character.
# Ceil of a character is the smallest character greater than it
def findCeil(str, c, startIndex):
    ceilIndex = startIndex
    for i in range(startIndex, len(str)):
        if str[i] > c and str[i] < str[ceilIndex]:
            ceilIndex = i
    return ceilIndex

# generates all distinct strings of str in alphabetical order
class DistinctPermutationGenerator:
    def __init__(self, str):
        self.current = sorted(str)
        self.n = len(str)
        self.isFinished = False

    def getCurrent(self):
        if self.isFinished:
            return ''
        return self.current

    def getNext(self):
        if self.isFinished:
            return ''
        rmsn = getRightmostCharacterSmallerThanNext(self.current)
        if rmsn == -1:
            self.isFinished = True
            return ''
        ceilIndex = findCeil(self.current, self.current[rmsn], rmsn + 1)
        self.current[rmsn], self.current[ceilIndex] = self.current[ceilIndex], self.current[rmsn]
        sort(self.current, rmsn + 1, len(self.current))
        return self.current

def main():
    str = '2134'
    gen = DistinctPermutationGenerator(str)
    duhNext = gen.getCurrent()
    while(duhNext != ''):
        print(duhNext)
        duhNext = gen.getNext()


if __name__ == '__main__':
    main()