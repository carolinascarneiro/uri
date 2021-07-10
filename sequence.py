def sequence():
    #declaring variables
    ilist = [3, 3, 3]
    lj = [7, 9, 12, 15]
    jlist = []
    
    #solving the i list 
    for w in range(9):
            ilist.append(ilist[w]+3)
    ilist = [1, 1, 1] + ilist

    #solving the j list
    for a in lj:    
        jlist.append(a), jlist.append(a - 1), jlist.append(a - 2)

    for i in range(12): print("I=", ilist[i], "J=", jlist[i])

sequence()







