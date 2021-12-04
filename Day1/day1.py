def twoSum(hashTable):
    for x in hashTable.keys():
        try:
            hashTable[2020-x] == hashTable[x]
            return (2020-x)*x
        except KeyError:
            next
    return "not found"

def threeSum(data):
    for x in range(0,len(data)):
        holderset = set()
        currentSum = 2020 - data[x]
        for y in  data[x+1:]:
            if (currentSum - y) in holderset:
                return(data[x]*y*(currentSum-y))
            holderset.add(y)
    return "not found"

if __name__ == '__main__':
    data = [int(x) for x in open('input','r')]
    hashTable = dict(zip(data, range(0,len(data))))
    print(twoSum(hashTable))
    print(threeSum(data))