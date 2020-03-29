from tqdm import tqdm

def main():
    # some very basic config
    minSeatCount    = 0
    maxSeatCount    = 9

    for i in range(minSeatCount, maxSeatCount + 1):
        # build table
        table = []
        for j in range(i):
            table.append(j)

        #actual test process
        for j in range(i - 1):
            swp = buildAndTest(j, table, table, [], ([], [], len(table) + 1))
            tqdm.write(f"{i}:{j} --> {swp[2]} : {swp[1]}")


def buildAndTest(startCorrect, table, remaining, current, worst):
    retWorst = (worst[0].copy(), worst[1].copy(), worst[2])
    
    # limit check
    if (0 == len(remaining)):
        # limit function
        if (countMatches(table, current) == startCorrect):
                curMax = getMaxArrangement(table, current)
                if (curMax[2] < retWorst[2]):
                    retWorst = (curMax[0].copy(), curMax[1].copy(), curMax[2])
    else:
        # recursive function
        
        # remaining into current
        for i in tqdm(range(len(remaining)), leave=False):
            curChop = current.copy()
            remChop = remaining.copy()
            curChop.append(remChop.pop(i))

            # pump downwards
            retWorst = buildAndTest(startCorrect, table, remChop, curChop, retWorst)
    return retWorst

def rotBackwards(someList):
    ret = []
    for i in range(1, len(someList)):
        ret.append(someList[i])
    ret.append(someList[0])
    return ret

def rotForwards(someList):
    ret = []
    ret.append(someList[-1])
    for i in range(len(someList)-1):
        ret.append(someList[i])
    return ret

def getMaxArrangement(table, people):
    ret = None
    retArrangement = table.copy()
    retPeople      = people.copy()
    retCount       = countMatches(table, people)

    curPeople = people.copy()

    for i in range(len(table)):
        curPeople = rotForwards(curPeople)
        curCount  = countMatches(table, curPeople)

        if (curCount > retCount):
            retCount  = curCount
            retPeople = curPeople.copy()
        
    ret = (retArrangement, retPeople, retCount)
    return ret

def countMatches(table, people):
    # a running count of matches
    ret = 0
    
    for i in range(len(table)):
        if (table[i] == people[i]):
            ret += 1

    return ret

if __name__ == "__main__":
    main()
