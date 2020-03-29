def main():
    startCorrect = 15
    seatCount    = 20
    
    # build table:
    table = []
    for i in range(seatCount):
        table.append(i)

    print(f"start table:  {table}")
    print("")
    swp = buildAndTestTake2(startCorrect, table, table, [], ([], [], len(table) + 1))
    # swp = buildAndTestSeatArrangements(startCorrect, table, table, [], [], len(table) + 1, "")
    print(f"{swp}")


def buildAndTestTake2(startCorrect, table, remaining, current, worst):
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
        for i in range(len(remaining)):
            curChop = current.copy()
            remChop = remaining.copy()
            curChop.append(remChop.pop(i))

            # pump downwards
            retWorst = buildAndTestTake2(startCorrect, table, remChop, curChop, retWorst)
    return retWorst


def buildAndTestSeatArrangements(startCorrect, table, remaining, current, worst, worstCount, prefix):
    print(f"{prefix}- START -")
    print(f"{prefix}INPUT: startCorrect: {startCorrect}")
    print(f"{prefix}INPUT: table: {table}")
    print(f"{prefix}INPUT: remaining: {remaining}")
    print(f"{prefix}INPUT: current: {current}")
    print(f"{prefix}INPUT: worst: {worst}")
    print(f"{prefix}INPUT: worstCount: {worstCount}")
    retWorst      = worst
    retWorstCount = worstCount

    print(f"{prefix}DEBUG: LIMIT CHECK FORK")
    if (len(remaining) == 0):
        print(f"{prefix}DEBUG: LIMIT")
        # limit step
        # make sure we have the correct number of starting matches
        if (countMatches(table, current) == startCorrect):
            # see if we've gotten a worse arrangement
            curMax = getMaxArrangement(table, current)
            mCount = curMax[2]

            if (mCount < retWorstCount):
                print(f"{prefix}INFO :found worse!")
                retWorstCount = mCount
                retWorst = (curMax[0], curMax[1])
                print(f"{prefix}INF0 : m    : {mCount}")
                print(f"{prefix}INFO : r    : {retWorstCount}")
                print(f"{prefix}INFO : cMax : {curMax}")
                print(f"{prefix}INFO : ret  : {retWorst}")
    else:
        # recursive step
        print(f"{prefix}DEBUG: RECURSIVE")
        for i in range(len(remaining)):
            remSwp     = remaining.copy()
            curSwp     = current.copy()
            curSwp.append(remSwp.pop(i))
            retWorst, retWorstCount = buildAndTestSeatArrangements(startCorrect, table, remSwp, curSwp, worst, worstCount, (prefix + "    "))
        print(f" INFO: return planned: {retWorstCount} {retWorst}")
    print(f"INFO: returning: {retWorstCount} {retWorst}")
    print(f"{prefix}- RETURN -")
    return retWorst, retWorstCount
    

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
