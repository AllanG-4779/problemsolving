def minimumBribes(q):
    bribes = 0
    for i in range(len(q), 0, -1):
        if i != q[i-1]:
            if (i-2)>=0 and i == q[i-2]:
                temp = q[i-1]
                q[i-1] = q[i-2]
                q[i-2] = temp
                bribes+=1
            
            elif (i-3) >=0 and i == q[i-3]:
               temp1 = q[i-3]
               q[i-3] = q[i-2]
               q[i-2] = temp1
               temp1 = q[i-1]
               q[i-1] = q[i-2]
               q[i-2]= temp1
               bribes+=2
               
            else:
                print("Too chaotic")
                return
        
            
    print(bribes)