total = 0
def searchSortedLists(lsts):
    global total
    for b in lsts:
        # if list is in ascending order, return all lists with gradual increase
        if sorted(b) == b:
                index = 0
                while index < (len(b) - 1):
                    if b[index + 1] - b[index] == 0 or b[index + 1] - b[index] > 3:
                        break
                    index += 1
                
                if index == len(b) - 1:  # The loop ended at the second-to-last index
                    print(b)
                    total += 1
                    break

        # if list is in descending order, return all lists with gradual decrease
        elif sorted(b, reverse = True) == b:
                index = 0
                while index < (len(b) - 1):
                    if b[index] - b[index + 1] == 0 or b[index] - b[index + 1] > 3:
                        break
                    index += 1
                
                if index == len(b) - 1:  # The loop ended at the second-to-last index
                    print(b)
                    total += 1
                    break

def split_list(lst): 
    result = [] 
    for i in range(len(lst)): 
        new_list = lst[:i] + lst[i+1:] 
        result.append(new_list)
    result.append(lst)
    return result

    

with open("input2.txt") as file:
    for line in file:
        lst = line.split()
        b = [int(item) for item in lst]
        #searchSortedLists(b) #part 1 (ans = 479)

        lists = split_list(b)
        searchSortedLists(lists)
            
        

        
    print(total) 
            


   