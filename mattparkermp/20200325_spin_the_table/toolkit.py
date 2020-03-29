def main():
    foo = [1, 2, 3, 4, 5, 6]

    print(f"start:     {foo}")
    print(f"forwards:  {rotForwards(foo)}")
    print(f"backwards: {rotBackwards(foo)}")

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

if __name__ == "__main__":
    main()
