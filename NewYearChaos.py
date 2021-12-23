def minimumBribes(q):
    bribes = 0
    for i in range(len(q), 0, -1):
        # using a sorted array, check that the values at corresponding locations
        # beginning from the last element or rather the length of the passed array.
        # matches, if not check if the last one or two numbers in the unsorted 
        # array matches
        if i != q[i-1]:
            
            if (i-2)>=0 and i == q[i-2]:
                # 1 2 3 5 4 (Unsorted) 1 2 3 4 5  Unsorted[i-2] = 5 hence swap
                temp = q[i-1]
                q[i-1] = q[i-2]
                q[i-2] = temp
                bribes+=1
            
            elif (i-3) >=0 and i == q[i-3]:
                # If the number in the location two indices after the number in considration
                # swap the three numbers adjascent to each other beginning from the out of place number
            
               temp1 = q[i-3]
               q[i-3] = q[i-2]
               q[i-2] = temp1
               temp1 = q[i-1]
               q[i-1] = q[i-2]
               q[i-2]= temp1
               bribes+=2
               
            else:
                # More than two bribes occurred hence brint two chaotic
                print("Too chaotic")
                return
        
            
    print(bribes)