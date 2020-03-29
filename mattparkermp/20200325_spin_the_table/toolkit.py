def main():
    table =  [1, 2, 3, 4, 5, 6]
    people = [6, 5, 4, 3, 2, 1]

    print(f"start table:  {table}")
    print(f"start people: {people}")
    print("")
    swp = getMaxArrangement(table, people)
    print(f"max table:  {swp[0]}")
    print(f"max people: {swp[1]}")
    print(f"max count:  {swp[2]}")

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
    retArrangement = table
    retPeople      = people
    retCount       = countMatches(table, people)

    curPeople = people

    for i in range(len(table)):
        curPeople = rotForwards(curPeople)
        curCount  = countMatches(table, curPeople)

        if (curCount > retCount):
            retCount  = curCount
            retPeople = curPeople
        
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
