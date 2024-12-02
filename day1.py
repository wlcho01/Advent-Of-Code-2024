with open("input1.txt") as file:
    total = 0
    leftlist = []
    rightlist = []
    for line in file:
        lst = line.split()
        leftlist.append(lst[0])
        rightlist.append(lst[1])
    leftlist.sort()
    rightlist.sort()
    
    #for i in range(len(leftlist)):
    #    total += abs(int(leftlist[i]) - int(rightlist[i])) #2166959
    #print(total)

    for num in leftlist:
        
        total += int(num) * rightlist.count(num)
    print(total)
