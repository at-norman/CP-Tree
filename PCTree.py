class PCTree:
    def __init__(self, array):
        self.columns = array
       #print("Input: " + str(self.columns))
        m, n = len(array[0]), len(array)
        
        #The above pulls in an nxm matrix
        
        #initializing nodes to a 2m+1 by m+2 matrix - this is done just to make sure we don't run out of slots. WE MIGHT WANT THIS BIGGER OR SMALLER - I DO NOT KNOW.
        
        #!Current problem takes place in j = 2, is placing the wrong things in places, largest case.
        
        self.nodes = [[None] * (m + 1)] * 2 * n
        self.nodes[0] = [0] * (n+2)
        self.nodes[1] = [0] * (n+2)
        self.nodes[0][0] = 2
        self.nodes[0][1] = (n+11)
        self.nodes[1][0] = 2
        self.nodes[1][1] = (n+10)
        indexlen = [0] * (2 * n + 1)
        k1, k2 = 2, 2
        indexlen[n] = 2
        indexlen[n+1] = 2
        NodeOne = False
        NodeZero = False
        for i in range(n):
            if self.columns[i][0] is 0:
                self.nodes[0][k1] = (i+10)
                k1 += 1
                indexlen[n]+=1
                NodeZero = True
            elif self.columns[i][0] is 1:
                self.nodes[1][k2] = (i+10)
                k2 += 1
                indexlen[n+1]+=1
                NodeOne = True
            else:
                raise ValueError('Invalid input, not a 1 or 0')
    
        #The above is placing all the columns that are 1 on the first row on a node, all the columns that are zero on the first row on another node, and connecting them.
    
        index = [0] * (2 * n + 1)
                        #print(n)
                        #print("0:")
                        #print(self.nodes[0])
                        #print("1:")
                        #print(self.nodes[1])
        for i in range(n):
            index[i] = self.columns[i]
            indexlen[i] = m
                        #print("index")
                        #print(index[i])
        index[n] = self.nodes[0]
        index[n+1] = self.nodes[1]
        isize = n+2
                        #p = 0
                        #for i in range(0,len(index)):
                        #if index[i] != 0:
                        #p+=1
                        #print(p)
                
        #The above just gives me a master list of all columns and nodes. This is incredibly important to how I coded the algorithm

        #Non-base case implementation:
        
                        #print(index)
        for j in range(1, m):
           #print(j)
           #print(index)
            tsize = 0
            trsize = 0
            bsize = 0
            osize = 0
            zsize = 0
            termtag = 0
            ones = [0] * 2 * n
            zeroes = [0] * 2 * n
            terminal = [0] * 2 * n
            self.tried = [0] * 2 * n
            touching = [0] * 2 * n
            both = [0] * n
            bothindex = [0] * n
            indexcheck = [0]*(isize)
            
        #The above is just initializing variables we need to work with
        
        #NOTE: Justin tried to do tsize,trsize = [0]*2 etc with other variables. This DOES NOT WORK. That creates a single object with multiple tags to it, not multiple objects that start out
        #the same. Do not attempt to do this.
        
        #Next we initialize all of our columns into ones or zeroes
            
            for i in range(n):
                        #print(i)
                if self.columns[i][j] == 1:
                    ones[osize] = (i+10)
                        #print("is one")
                        #print(ones[osize])
                    indexcheck[i] = 1
                    osize += 1
                elif self.columns[i][j] == 0:
                    zeroes[zsize] = (i+10)
                        #print("is zero")
                        #print(zeroes[zsize])
                    indexcheck[i] = 2
                    zsize += 1
                else:
                    raise ValueError('Invalid input, not a 1 or 0')
                        #for i in range(zsize):
                        #print("nb")
                        #print(zeroes[i])
                        #print("done")
        
        #Next we initialize "elementary" nodes - ones that are attached to one other node at most and a bunch of columns into One, Zero, or Both
        
        #Initialization of Nodes into One or Zero etc
        
            for i in range(n, isize):
                onestag = False
                zeroestag = False
                nodestag = 0
                        #print("indexlen")
                        #print(indexlen[i])
                        #print(j)
                        #print(i)
                        #print(index[i])
                        #print(indexlen[i])
                        #print(index)
                for k in range(1, indexlen[i]):
                    if index[i][k] in range(10,10+m):
                        #print("i")
                        #print(i)
                        #print("k")
                        #print(k)
                        #print(index[i][k][j])
                        a = index[i][k]
                        if index[a-10][j] is 1:
                            onestag = True
                        if index[a-10][j] is 0:
                            zeroestag = True
                    else:
                        nodestag += 1
                if zeroestag and onestag:
                    both[bsize] = (i+10)
                    indexcheck[i] = 3
                    bsize += 1
                elif zeroestag and nodestag==1:
                    zeroes[zsize] = (i+10)
                    indexcheck[i] = 2
                    zsize += 1
                elif onestag and nodestag==1:
                    ones[osize] = (i+10)
                    indexcheck[i] = 1
                    osize += 1
                        #print("After Step 1")
                        #print(bsize)
                        
        #Okay, that's great. Now it's time to interate our node initialization, specifically the non elementary ones. This procedure is described on the overleaf document.
        
            bothiterate = True
            while(bothiterate):
                #print("index")
                #print(index)
                #print("ones")
                #print(ones)
                #print("zeroes")
                #print(zeroes)
                #print("both")
                #print(both)
                for i in range(n, isize):
                        #print(indexcheck[i])
                    iteratetag = True
                    onestag = False
                    zeroestag = False
                    bothtag = False
                    nodestag = 0
                    if (indexcheck[i] == 1):
                        iteratetag = False
                    if (indexcheck[i] == 2):
                        iteratetag = False
                    if (indexcheck[i] == 3):
                        iteratetag = False
                    if iteratetag:
                        for k in range(1, indexlen[i]):
                        #print(index[i][k])
                            if index[i][k] in ones and index[i][k] != 0:
                                onestag = True
                            elif index[i][k] in zeroes and index[i][k] != 0:
                                zeroestag = True
                            elif index[i][k] in both and index[i][k] != 0:
                                bothtag = True
                            elif index[i][k] != 0:
                                nodestag += 1
                        if zeroestag and onestag:
                            both[bsize] = (i+10)
                            indexcheck[i] = 3
                            bsize += 1
                        elif zeroestag and nodestag<=1:
                            zeroes[zsize] = (i+10)
                            indexcheck[i] = 2
                            zsize += 1
                        elif onestag and nodestag<=1:
                            ones[osize] = (i+10)
                            indexcheck[i] = 1
                            osize += 1
                        elif bothtag and nodestag<=1:
                            both[bsize] = (i+10)
                            indexcheck[i] = 3
                            bsize += 1
                        #for i in range(0,bsize):
                        #print(both[i])
                        #print("b")
                        #print(bsize)
                        #print("o")
                        #print(osize)
                        #print("z")
                        #print(zsize)
                bothiterate = False
                        #print(both)
                        #print(ones)
                        #print(zeroes)
                for i in range(m, isize):
                        #print(indexcheck[i])
                    if ((i+10) not in ones) and ((i+10) not in zeroes) and ((i+10) not in both):
                        bothiterate = True
                        #print(index[i])
                        #print(bothiterate)
                        
        #End iteration

        #The above is 100% solid, this perfectly places our nodes and columns into the categories we need in order to find the terminal path.

        #The next goal is to determine the terminal path.
        
        #To begin with we consider the case if we only have one node to split along. Of course, if we have none we can just ignore it and move to the next row.
        
                        #print(j)
                        #print(both)
            if bsize is not 0:
                        #print(j)
               #print("IF1")
                if bsize is 1:
                    #print(j)
                   #print("IF2")
                    
        #This next case is for if the single node we're splitting along is a p node
        
                    a = (both[0]-10)
                    if index[a][0] is 2:
                        #print(j)
                       #print("IF3")
                        splitp = index[a][:]
                        splitplen = indexlen[a]
                        ocounter = 0
                        zcounter = 0
                        for i in range(1,splitplen):
                            if index[a][i] in ones and index[a][i] != 0:
                                ocounter+=1
                            if index[a][i] in zeroes and index[a][i] != 0:
                                zcounter+=1
                    
        #Why use this zcounter/ocounter thing? Well, if we're splitting along a node and it only has one thing that's in Ones and all else is in Zeroes, it'll end up just being as if we hadn't
        #split at all. Same with vice versa. So we just ignore it if that's the case.
                    
                        if zcounter!=1 and ocounter!=1:
                            for i in range(isize):
                                if not(i in range(n)):
                                    for p in range(indexlen[i]):
                                        if index[i][p] == (a+10):
                                            if (i+10) in ones:
                                                index[i][p] = 4
                                            elif (i+10) in zeroes:
                                                index[i][p] = 5
                        
        #Okay, just now we went through all of our structure, saw where things intersect our node we need to split along, and replaced them pointing to that node with a little tag that I can
        #use to come back to later and stitch our changed node back into our larger structure.
                        
                            index[a] = 0
                            indexlen[a] = 0
                            temparray = [0]*(2*n+1)
                            qrs = 1
                            temparray[0] = 2
                            for i in range(1,splitplen):
                                if splitp[i] in ones and splitp[i] != 0:
                                    temparray[qrs] = splitp[i]
                                    qrs += 1
                            indexlen[a] = qrs+1
                            index[a] = temparray
                            
        #Just now we grabbed all of the connections from our node we're splitting along that are in Ones and attached them to a new node.
                            
                            temparray = [0]*(2*n+1)
                            qrs = 1
                            temparray[0] = 2
                            for i in range(1,splitplen):
                                if splitp[i] in zeroes and splitp[i] != 0:
                                    temparray[qrs] = splitp[i]
                                    qrs += 1
                            index[isize] = temparray
                            index[isize][qrs] = (a+10)
                            indexlen[isize] = qrs+1
                            index[a][indexlen[a]-1] = (isize+10)
                            isize += 1
                            
        #Same as just before, but with zeroes.
        
                            #print(index)
                            for i in range(isize):
                                if not(i in range(n)):
                                    for p in range(indexlen[i]):
                                        if index[i][p] == 4:
                                            index[i][p] = (a+10)
                                        elif index[i][p] ==5:
                                            index[i][p] = (isize+9)
                
        #Okay, then we stitch the two nodes to each other and then stitch them back into our larger structure
                
        #Alright, that ends the p node stuff. Now we split along a single c node.
        
                    if index[a][0] is 3:
                        #print(index[6])
                        #print(j)
                       #print("IF4")
                        splitp = index[a][:]
                        splitplen = indexlen[a]
                        ocounter = 0
                        zcounter = 0
                        zr = 0
                        for y in range(1, splitplen-1):
                            if index[a][y] in zeroes and index[a][y+1] in ones and index[a][y] != 0 and index[a][y+1] != 0:
                                zr += 1
                            if index[a][y+1] in zeroes and index[a][y] in ones and index[a][y] != 0:
                                zr += 1
                            if zr >= 3:
                                raise ValueError('There is no possible arrangement.')
                    
        #This is the major change between the p and c nodes, for the c nodes we actually need to look at the structure, that all ones and zeroes we split along are all next to each other
        #in a "circular order" in a sense. The above code just checks for this.
        
        #The second major change with a C node is this, if we're only splitting along a single cnode, and the structure we have works out, we do an order preserving contraction and we're done. Thus no change is made.
        
        #Okay, those were the nice cases, where we only had one node to split along. If we have more than one we have a bit of a nastier task, which first requires us to find multiple nodes to
        #split along, not all of which are "both".
        
        #Next off we initialize some technical junk and send it to our function that finds our terminal path.

                else:
                   #print("ELSE")
                        #print(j)
                        #print(both[0])
                        #print(both[1])
                    a = (both[0]-10)
                    terminal[0] = both[0]
                    tsize += 1
                    temparray = self.traverse(both, terminal, self.tried, tsize, trsize, termtag, a, bsize, n, index, indexlen)
                    terminal = temparray[0]
                    tried = temparray[1]
                    tsize = temparray[2]
                    trsize = temparray[3]
                    termtag = temparray[4]
                   #print("postElse")
                   #print(terminal)
                   #print(both)
                   #print(index)

        #The above is just to get us the terminal path, grabbing it and other relevant tidbits of information.
        
                    terminalsize = [0]*tsize
                    for i in range(tsize):
                        terminalsize[i] = indexlen[terminal[i]-10]
                    splitsize = 0
                    splitsize = tsize+bsize
                    frontcounter = 0
                    backcounter = 0
                    temparray = [0]*((2*n+1)*2)
                    temparray[0] = 3
                    qrs = 1
                    centrallocfor = isize
                    centralloc = isize
                        #print(j)
                        #print("centralloc1")
                        #print(centralloc+10)
                    index[isize] = temparray
                    indexlen[isize] = ((2*n+1)*2)
                    isize += 1
                    temparray = [0]*((2*n+1)*2)
                    temparray[0] = 3
                    centrallocback = 2*n
                    index[2*n] = temparray
                    indexlen[2*n] = ((2*n+1)*2)
                        #print(centralloc+10)
                   #print(terminal)
                    
        #Next up is the above, which initializes some things for the next step in our algorithm.
        
                    for i in range(tsize):
                        #print("for")
                       #print(i)
                       #print(index)
                        temparray = [0]*(2*n+1)
                        qrs = 1
                        #print(terminal)
                        #print(index[4])
                        #print(index[5])
                        if not(terminal[i] in both):
                           #print("if 10")
                            #print(terminal[i])
                            if index[terminal[i]-10][0] == 2:
                                if terminal[i] in ones and terminal[i] != 0:
                                    for k in range(1,indexlen[terminal[i]-10]):
                                        if index[terminal[i]-10][k] in ones and index[terminal[i]-10][k] != 0:
                                            for l in range(1, indexlen[index[terminal[i]-10][k]-10]):
                                                if index[index[terminal[i]-10][k]-10][l] == terminal[i]:
                                                    index[index[terminal[i]-10][k]-10][l] = (centralloc+10)
                                            index[centrallocback][backcounter+1] = index[terminal[i]-10][k]
                                            backcounter += 1
                                elif terminal[i] in zeroes and terminal[i] != 0:
                                    for k in range(1,indexlen[terminal[i]-10]):
                                        if index[terminal[i]-10][k] in zeroes and index[terminal[i]-10][k] != 0:
                                            for l in range(1, indexlen[index[terminal[i]-10][k]-10]):
                                                if index[index[terminal[i]-10][k]-10][l] == terminal[i]:
                                                    index[index[terminal[i]-10][k]-10][l] = (centralloc+10)
                                            index[centrallocfor][frontcounter+1] = index[terminal[i]-10][k]
                                            frontcounter += 1
                            elif index[terminal[i]-10][0] == 3: #Maybe fix this up?
                                checktag = True
                                quickquicktag = 1
                                for k in range(indexlen[terminal[i]-10]):
                                    if index[terminal[i]-10][k] in terminal and checktag:
                                        checktag = False
                                        quickquicktag = k
                                if quickquicktag != 1:
                                    temparray[0] = 3
                                    for k in range(quickquicktag,indexlen[terminal[i]-10]):
                                        temparray[qrs] = index[terminal[i]-10][k]
                                        qrs += 1
                                    for k in range(1, quickquicktag):
                                        temparray[qrs] = index[terminal[i]-10][k]
                                        qrs += 1
                                    index[terminal[i]-10] = temparray
                                        #print(index)
                                if terminal[i] in ones and terminal[i] != 0:
                                    if index[terminal[i]-10][1] == terminal[i-1] or index[terminal[i]-10][1] == centralloc:
                                        for k in range(2, indexlen[terminal[i]-10]-1):
                                            index[centrallocback][backcounter+1] = index[terminal[i]-10][k]
                                            backcounter += 1
                                    elif index[terminal[i]-10][1] == terminal[i+1]:
                                        for l in range(2,indexlen[terminal[i]-10]-1):
                                            k = indexlen[terminal[i]-10]-l
                                            index[centrallocback][backcounter+1] = index[terminal[i]-10][k]
                                            backcounter += 1
                                elif terminal[i] in zeroes and terminal[i] != 0:
                                    #print("hmm")
                                    if index[terminal[i]-10][1] == terminal[i-1] or index[terminal[i]-10][1] == centralloc:
                                        for k in range(2, indexlen[terminal[i]-10]-1):
                                            index[centrallocfor][frontcounter+1] = index[terminal[i]-10][k]
                                            frontcounter += 1
                                    elif index[terminal[i]-10][1] == terminal[i+1]:
                                        for l in range(2,indexlen[terminal[i]-10]-1):
                                            k = indexlen[terminal[i]-10]-l
                                            index[centrallocfor][frontcounter+1] = index[terminal[i]-10][k]
                                            frontcounter += 1
                        #print(index)
                            for k in range(indexlen[terminal[i]-10]):
                                #print("whaddup")
                                #print(index[index[terminal[i]-10][k]-10])
                                if index[index[terminal[i]-10][k]-10] != 0 and index[index[terminal[i]-10][k]-10] != 7:
                                    for l in range(len(index[index[terminal[i]-10][k]-10])):
                                        #print(l)
                                        if index[index[terminal[i]-10][k]-10][l] == terminal[i]:
                                            index[index[terminal[i]-10][k]-10][l] = (centralloc+10)
                                                #print(index)
                            index[terminal[i]-10] = 7
                           #print(index)
                        
                    
        #If we reach something that doesn't need to be split we just push it back onto our new central C node. Above holds forward/back.
        
        #Next we talk about splitting along this more complicated terminal path, if it's a p node.
        
                        elif index[terminal[i]-10][0] == 2:
                            #print("if 11")
                            #print(j)
                            temparray[0] = 2
                            a = terminal[i]-10
                            splitp = index[terminal[i]-10][:]
                            splitplen = indexlen[terminal[i]-10]
                            ocounter = 0
                            zcounter = 0
                            otag = 0
                            ztag = 0
                            #print(i)
                            #print(splitp)
                            for k in range(1,splitplen):
                        #print("for 110")
                                if ((splitp[k] in ones) and not(splitp[k] in terminal)) and splitp[k] != 0:
                                    ocounter+=1
                                    otag = k
                                   #print(k)
                                if ((splitp[k] in zeroes) and not(splitp[k] in terminal)) and splitp[k] != 0:
                                    zcounter+=1
                                    ztag = k
                        #print("tags")
                        #print(otag)
                        #print(ztag)
                            if zcounter == 1 and ocounter == 1:
                               #print("if 111")
                                for k in range(indexlen[splitp[ztag]-10]):
                                    if index[splitp[ztag]-10][k] == terminal[i]:
                                        index[splitp[ztag]-10][k] = (centralloc+10)
                                for k in range(len(index[splitp[otag]-10])):
                                    if index[splitp[otag]-10][k] == terminal[i]:
                                        index[splitp[otag]-10][k] = (centralloc+10)
                                for k in range(tsize): #NOT SURE IF THIS WORKS, THIS IS THE PROPOSED CHANGE - DO I NEED TO DO THIS? NO IDEA. MIGHT BE REDUNDANT.
                                    if index[terminal[k]-10] != 7:
                                        for o in range(indexlen[terminal[k]-10]):
                                            if index[terminal[k]-10][o] == terminal[i]:
                                                index[terminal[k]-10][o] = (centralloc+10)
                                index[centrallocfor][frontcounter+1] = splitp[ztag]
                                frontcounter += 1
                                index[centrallocback][backcounter+1] = splitp[otag]
                                backcounter += 1
                        #print(index[centrallocback])
                        #print(index[centrallocfor])
                                index[a] = 7
                        #print("test")
                               #print(index)
                        
        #The above is concerning a p node where it's got only one 'zero' node attached and one 'one' node attached.
                        
                            elif zcounter == 1:
                               #print("if 112")
                                for k in range(indexlen[splitp[ztag]-10]):
                        #print("for 1121")
                                    if index[splitp[ztag]-10][k] == terminal[i]:
                                        index[splitp[ztag]-10][k] = (centralloc+10)
                                for k in range(tsize): #NOT SURE IF THIS WORKS, THIS IS THE PROPOSED CHANGE.
                                    if index[terminal[k]-10] != 7:
                                        for o in range(indexlen[terminal[k]-10]):
                                            if index[terminal[k]-10][o] == terminal[i]:
                                                index[terminal[k]-10][o] = (centralloc+10)
                                index[centrallocfor][frontcounter+1] = splitp[ztag]
                                frontcounter += 1
                        #print("test")
                        #print(index[centrallocfor])
                        #print(index[5])
                                for k in range(indexlen[terminal[i]-10]):
                        #print("for 1122")
                                    if (splitp[k] in ones) and not (splitp[k] in terminal) and splitp[k] != 0 and splitp[k] != (centralloc+10):
                                        temparray[qrs] = splitp[k]
                                        qrs += 1
                                    elif (splitp[k] in zeroes) and not (splitp[k] in terminal) and splitp[k] != 0 and splitp[k] != (centralloc+10):
                                        temparray[qrs] = (centralloc+10)
                                        qrs += 1
                                indexlen[a] = qrs+1
                                index[a] = temparray
                                index[centrallocback][backcounter+1] = (a+10)
                                backcounter += 1
                        #print(index)
                        #print("test")
                        #print(index[centrallocback])
                        
        #That's if just one that's a 'zero' node, we stitch that back onto our new central node, then modify our node to remove that and all connections to terminal path nodes, then stitch that on as well.
                        
                            elif ocounter == 1:
                        #print(j)
                               #print("if 113")
                        #print(index)
                        #print(terminal[i])
                        #print(index[splitp[otag]-10])
                                for k in range(len(index[splitp[otag]-10])):
                                    if index[splitp[otag]-10][k] == terminal[i]:
                                        index[splitp[otag]-10][k] = (centralloc+10)
                                for k in range(tsize): #NOT SURE IF THIS WORKS, THIS IS THE PROPOSED CHANGE.
                                    if index[terminal[k]-10] != 7:
                                        for o in range(indexlen[terminal[k]-10]):
                                            if index[terminal[k]-10][o] == terminal[i]:
                                                index[terminal[k]-10][o] = (centralloc+10)
                                index[centrallocback][backcounter+1] = splitp[otag]
                                backcounter += 1
                        #print(centralloc+10)
                                for k in range(indexlen[terminal[i]-10]):
                                    if (splitp[k] in zeroes) and not (splitp[k] in terminal) and splitp[k] != 0 and splitp[k] != (centralloc+10):
                                        temparray[qrs] = splitp[k]
                                        qrs += 1
                                    elif (splitp[k] in ones) and not (splitp[k] in terminal) and splitp[k] != 0 and splitp[k] != (centralloc+10):
                                        temparray[qrs] = (centralloc+10)
                                        qrs += 1
                                indexlen[a] = qrs+1
                                index[a] = temparray
                                index[centrallocfor][frontcounter+1] = (a+10)
                                frontcounter += 1
                        #print("index2")
                               #print(index)
                        
        #The above for if there's one 'one' node.
                        
        #And, of course, if we're just splitting along a generic pnode that isn't a general case we do the above.
                            
        #Next, we work on if there's more than just one in each category, we generate a new node as well and stitch them both on to our new central node.
                            
                            else:
                               #print("if 114")
                        #print(index[5])
                        #print(index)
                        #print(terminal[i])
                                for k in range(indexlen[terminal[i]-10]):
                        #print("for 115")
                                    if (splitp[k] in zeroes) and not (splitp[k] in terminal) and splitp[k] != 0:
                                        temparray[qrs] = splitp[k]
                                        qrs += 1
                                index[isize] = temparray
                                indexlen[isize] = qrs+1
                                index[isize][qrs] = (centralloc+10)
                                index[centrallocfor][frontcounter+1] = (isize+10)
                                isize += 1
                                frontcounter += 1
                                temparray = [0]*(2*n+1)
                                qrs = 1
                                temparray[0] = 2
                               #print(index)
                                for k in range(indexlen[terminal[i]-10]):
                        #print("for 116")
                                    if (splitp[k] in ones) and not (splitp[k] in terminal) and splitp[k] != 0:
                                        temparray[qrs] = splitp[k]
                                        qrs += 1
                                index[a] = temparray
                                indexlen[a] = qrs+1
                                index[a][qrs] = (centralloc+10)
                                index[centrallocback][backcounter+1] = (a+10)
                                backcounter += 1
                                    #print(j)
                                    #print(index)
                                    #print(i)
                        #print(index[centralloc])
                        #print(index[terminal[i]-10])
                           #print(index)
        #Next we consider if we're splitting along a C node.
                            
                        elif index[terminal[i]-10][0] == 3:
                        #print(j)
                        #print(index)
                           #print("if 12")
                        #print(index[5])
                            temparray[0] = 3
                            a = terminal[i]-10
                            splitp = index[terminal[i]-10][:]
                            splitplen = terminalsize[i]
                            ocounter = 0
                            zcounter = 0
                            otag = 0
                            ztag = 0
                            traverseCounter = 0
                            structureCheck = True
                            splitChecker = 0
                            onesCheck = False
                            zeroesCheck = False
                            for k in range(1,splitplen):
                                if splitp[k] in terminal or splitp[k] == (centralloc+10):
                                    traverseCounter += 1
                           #print(centralloc+10)
                            if traverseCounter == 2:
                                for k in range(1,splitplen):
                                    #print(k)
                                    #print(splitChecker)
                                    #print(splitp[k])
                                    if (splitChecker == 0) and (splitp[k] in terminal or splitp[k] == (centralloc+10) or index[splitp[k]-10] == 7) and splitp[k] != 0:
                                        splitChecker += 1
                                    elif (splitChecker == 1) and (splitp[k] in terminal or splitp[k] == (centralloc+10) or index[splitp[k]-10] == 7) and splitp[k] != 0:
                                        splitChecker += 2
                                    elif (splitChecker == 1) and (splitp[k] in ones) and splitp[k] != 0:
                                        splitChecker += 1
                                        onesCheck = True
                                    elif (splitChecker == 1) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        splitChecker += 1
                                        zeroesCheck = True
                                    elif (splitChecker == 2) and (splitp[k] in terminal or splitp[k] == (centralloc+10) or index[splitp[k]-10] == 7) and splitp[k] != 0:
                                        splitChecker += 1
                                    elif (splitChecker == 2) and onesCheck:
                                        if splitp[k] in zeroes:
                                            structureCheck = False
                                    elif (splitChecker == 2) and zeroesCheck:
                                        if splitp[k] in ones and splitp[k] != 0:
                                            structureCheck = False
                                splitChecker = 0
                                #print(structureCheck)
                                onesCheck = False
                                zeroesCheck = False
                                for k in range(1,splitplen):
                                    if (splitChecker == 0) and (splitp[k] in terminal or splitp[k] == (centralloc+10) or index[splitp[k]-10] == 7) and splitp[k] != 0:
                                        splitChecker += 2
                                    elif (splitChecker == 0) and (splitp[k] in ones) and splitp[k] != 0:
                                        splitChecker += 1
                                        onesCheck = True
                                    elif (splitChecker == 0) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        splitChecker += 1
                                        zeroesCheck = True
                                    elif (splitChecker == 1) and (splitp[k] in terminal or splitp[k] == (centralloc+10) or index[splitp[k]-10] == 7) and splitp[k] != 0:
                                        splitChecker += 1
                                    elif (splitChecker == 1) and onesCheck:
                                        if splitp[k] in zeroes and splitp[k] != 0:
                                            structureCheck = False
                                    elif (splitChecker == 1) and zeroesCheck:
                                        if splitp[k] in ones and splitp[k] != 0:
                                            structureCheck = False
                                    elif (splitChecker == 3) and onesCheck:
                                        if splitp[k] in zeroes and splitp[k] != 0:
                                            structureCheck = False
                                    elif (splitChecker == 3) and zeroesCheck:
                                        if splitp[k] in ones and splitp[k] != 0:
                                            structureCheck = False
                                    elif (splitChecker == 3) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        zeroesCheck = True
                                    elif (splitChecker == 3) and (splitp[k] in ones) and splitp[k] != 0:
                                        onesCheck = True
                                    elif (splitChecker == 1) and (splitp[k] in terminal or splitp[k] == (centralloc+10) or index[splitp[k]-10] == 7) and splitp[k] != 0:
                                        splitChecker += 1
                                    elif (splitChecker == 2) and (splitp[k] in terminal or splitp[k] == (centralloc+10) or index[splitp[k]-10] == 7) and splitp[k] != 0:
                                        splitChecker += 1
                            #print(index)
        #Above is checking for structural integrity along a node in the middle of our terminal path
            
                            else:
                        #print(index)
                               #print("else")
                                for k in range(1,splitplen):
                                    if (splitChecker == 0) and (splitp[k] in terminal or splitp[k] == (centralloc+10)) and splitp[k] != 0:
                                        splitChecker += 2
                                    elif (splitChecker == 0) and (splitp[k] in ones) and splitp[k] != 0:
                                        splitChecker += 1
                                        onesCheck = True
                                    elif (splitChecker == 0) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        splitChecker += 1
                                        zeroesCheck = True
                                    elif (splitChecker == 1) and (splitp[k] in ones) and splitp[k] != 0:
                                        if zeroesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 1) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if onesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 1) and (splitp[k] in terminal or splitp[k] == (centralloc+10)) and splitp[k] != 0:
                                        splitChecker += 6
                                    elif (splitChecker == 2) and (splitp[k] in ones) and splitp[k] != 0:
                                        splitChecker += 2
                                        onesCheck = True
                                    elif (splitChecker == 2) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        splitChecker += 2
                                        zeroesCheck = True
                                    elif (splitChecker == 3) and (splitp[k] in ones) and splitp[k] != 0:
                                        if onesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 3) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if zeroesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 3) and (splitp[k] in terminal or splitp[k] == (centralloc+10)) and splitp[k] != 0:
                                        splitChecker += 5
                                    elif (splitChecker == 4) and (splitp[k] in ones) and splitp[k] != 0:
                                        if zeroesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 4) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if onesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 5) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if onesCheck:
                                            structureCheck = False
                                    elif (splitChecker == 5) and (splitp[k] in ones) and splitp[k] != 0:
                                        if zeroesCheck:
                                            structureCheck = False
                                    elif (splitChecker == 6) and (splitp[k] in ones) and splitp[k] != 0:
                                        if onesCheck:
                                            structureCheck = False
                                    elif (splitChecker == 6) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if zeroesCheck:
                                            structureCheck = False
                                    elif (splitChecker == 7) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if onesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 7) and (splitp[k] in ones) and splitp[k] != 0:
                                        if zeroesCheck:
                                            splitChecker +=2
                                    elif (splitChecker == 8) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if onesCheck:
                                            structureCheck = False
                                        elif zeroesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 8) and (splitp[k] in ones) and splitp[k] != 0:
                                        if zeroesCheck:
                                            structureCheck = False
                                        elif onesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 9) and (splitp[k] in ones) and splitp[k] != 0:
                                        if onesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 9) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if zeroesCheck:
                                            splitChecker += 2
                                    elif (splitChecker == 10) and (splitp[k] in ones) and splitp[k] != 0:
                                        if zeroesCheck:
                                            structureCheck = False
                                    elif (splitChecker == 10) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if onesCheck:
                                            structureCheck = False
                                    elif (splitChecker == 11) and (splitp[k] in ones) and splitp[k] != 0:
                                        if zeroesCheck:
                                            structureCheck = False
                                    elif (splitChecker == 11) and (splitp[k] in zeroes) and splitp[k] != 0:
                                        if onesCheck:
                                            structureCheck = False
                                            
        #Above is checking for structural integrity along a node on the edge of our terminal path
                        
        #To make sure that the structure of the cnode we're splitting on isn't problematic we do the above.

        #Next we consider splitting along an edge node of ours. Currently the directionality is broken, need to fix that.

                            tagtag = True
                            starttag = 0
                            stoptag = 0
                            #print(structureCheck)
                            if structureCheck and traverseCounter == 1:
                               #print("yeah, we got here1")
                        #print(j)
                        #print(index)
                        #print(splitp)
                                if i == 0:
                        #print("ifffff1")
                                    for k in range(1, splitplen):
                                        if (splitp[k] in terminal or splitp[k] == (centralloc+10)) and splitp[k] != 0:
                                            otag = k
                        #print(splitp)
                        #print(terminal)
                        #print(otag)
                        #print(ones)
                        #print(zeroes)
                                    for k in range(1,splitplen):
                                        for l in range(indexlen[splitp[k]-10]):
                                            if index[splitp[k]-10][l] == (a+10):
                                                index[splitp[k]-10][l] = (centralloc+10)
                                    if splitp[1] in ones and splitp[1] != 0 and splitp[otag-1] in zeroes and splitp[otag-1] != 0:
                        #print("if1")
                                        for k in range(1,otag):
                                            if splitp[k] in zeroes and splitp[k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[k]
                                                frontcounter += 1
                                        for k in range(1,otag):
                                            if splitp[otag-k] in ones and splitp[otag-k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[otag-k]
                                                backcounter += 1
                                        for k in range(otag+1,splitplen):
                                            if splitp[splitplen+otag-k] in ones and splitp[splitplen+otag-k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[splitplen+otag-k]
                                                backcounter += 1
                                    elif splitp[1] in zeroes and splitp[1] != 0 and splitp[otag-1] in ones and splitp[otag-1] != 0:
                        #print("if2")
                        #print(index)
                                        for k in range(1,otag):
                                            if splitp[k] in ones and splitp[k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[k]
                                                backcounter += 1
                                        for k in range(1,otag):
                                            if splitp[otag-k] in zeroes and splitp[otag-k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[otag-k]
                                                frontcounter += 1
                                               #print(zeroes)
                                        for k in range(otag+1,splitplen):
                                            if splitp[splitplen+otag-k] in zeroes and splitp[splitplen+otag-k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[splitplen+otag-k]
                                                frontcounter += 1
                        #print(index)
                                    elif splitp[1] in ones and splitp[1] != 0 and splitp[otag+1] in zeroes and splitp[otag+1] != 0:
                        #print("if3")
                                        for k in range(otag+1,splitplen):
                                            if splitp[splitplen+otag-k] in zeroes and splitp[splitplen+otag-k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[splitplen+otag-k]
                                                frontcounter += 1
                                        for k in range(1,otag):
                                            if splitp[k] in ones and splitp[k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[k]
                                                backcounter += 1
                                        for k in range(otag+1,splitplen):
                                            if splitp[k] in ones and splitp[k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[k]
                                                backcounter += 1
                                    elif splitp[1] in zeroes and splitp[1] != 0 and splitp[otag+1] in ones and splitp[otag+1] != 0:
                        #print("if4")
                                        for k in range(otag+1,splitplen):
                                            if splitp[splitplen+otag-k] in ones and splitp[splitplen+otag-k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[splitplen+otag-k]
                                                backcounter += 1
                                        for k in range(1,otag):
                                            if splitp[k] in zeroes and splitp[k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[k]
                                                frontcounter += 1
                                        for k in range(otag+1,splitplen):
                                            if splitp[k] in zeroes and splitp[k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[k]
                                                frontcounter += 1
                                    elif otag == 1 and splitp[otag+1] in ones and splitp[otag+1] != 0:
                                        for k in range(2,splitplen):
                                            if [splitplen+1-k] in ones and [splitplen+1-k] != 0:
                                                #print("here oneone")
                                                index[centrallocback][backcounter+1] = [splitplen+1-k]
                                                backcounter += 1
                                        for k in range(2,splitplen):
                                            if splitp[k] in zeroes and splitp[k] != 0:
                                                #print("here onetwo")
                                                index[centrallocfor][frontcounter+1] = splitp[k]
                                                frontcounter += 1
                                    elif otag == 1 and splitp[otag+1] in zeroes and splitp[otag+1] != 0:
                        #print("here two")
                                        for k in range(2,splitplen):
                                            if splitp[splitplen+1-k] in zeroes and splitp[splitplen+1-k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[splitplen+1-k]
                                                frontcounter += 1
                                        for k in range(2,splitplen):
                                            if splitp[k] in ones and splitp[k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[k]
                                                backcounter += 1
                                
                                        index[a] = 7
                                    #!Might have to add in another 'clean' effect? idk.
                                else: #!Might have to change this back? idk
                                    #print("ifffff2")
                                    for k in range(1, splitplen):
                                        if (splitp[k] in terminal or splitp[k] == (centralloc+10)) and splitp[k] != 0:
                                            otag = k
                        #print("otag")
                        #print(k)
                        #print(splitp)
                        #print(j)
                                    if splitp[1] in ones and splitp[1] != 0 and splitp[otag-1] in zeroes and splitp[otag-1] != 0:
                                        for k in range(1,otag):
                                            if splitp[otag-k] in zeroes and splitp[otag-k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[otag-k]
                                                frontcounter += 1
                                        for k in range(otag,splitplen):
                                            if splitp[k] in ones and splitp[k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[k]
                                                backcounter += 1
                                        for k in range(1,otag):
                                            if splitp[k] in ones and splitp[k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[k]
                                                backcounter += 1
                                    elif splitp[1] in zeroes and splitp[1] != 0 and splitp[otag-1] in ones and splitp[otag-1] != 0:
                                        for k in range(1,otag):
                                            if splitp[otag-k] in ones and splitp[otag-k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[otag-k]
                                                backcounter += 1
                                        for k in range(otag,splitplen):
                                            if splitp[k] in zeroes and splitp[k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[k]
                                                frontcounter += 1
                                        for k in range(1,otag):
                                            if splitp[k] in zeroes and splitp[k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[k]
                                                frontcounter += 1
                                    elif splitp[1] in ones and splitp[1] != 0 and splitp[otag+1] in zeroes and splitp[otag+1] != 0:
                                        for k in range(otag,splitplen):
                                            if splitp[k] in zeroes and splitp[k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[k]
                                                frontcounter += 1
                                        for k in range(1,otag):
                                            if splitp[otag-k] in ones and splitp[otag-k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[otag-k]
                                                backcounter += 1
                                        for k in range(otag+1,splitplen):
                                            if splitp[splitplen+otag-k] in ones and splitp[splitplen+otag-k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[splitplen+otag-k]
                                                backcounter += 1
                                    elif splitp[1] in zeroes and splitp[1] != 0 and splitp[otag+1] in ones and splitp[otag+1] != 0:
                                        for k in range(otag,splitplen):
                                            if splitp[k] in ones and splitp[k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[k]
                                                backcounter += 1
                                        for k in range(1,otag):
                                            if splitp[otag-k] in zeroes and splitp[otag-k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[otag-k]
                                                frontcounter += 1
                                        for k in range(otag+1,splitplen):
                                            if splitp[splitplen+otag-k] in zeroes and splitp[splitplen+otag-k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[splitplen+otag-k]
                                                frontcounter += 1
                                    elif otag == 1 and splitp[otag+1] in ones and splitp[otag+1] != 0:
                        #print(j)
                        #print(index)
                        #print("here one")
                                        for k in range(2,splitplen):
                                            if splitp[k] in ones and splitp[k] != 0:
                        #print("here oneone")
                                                index[centrallocback][backcounter+1] = splitp[k]
                                                backcounter += 1
                                        for k in range(2,splitplen):
                                            if splitp[splitplen+1-k] in zeroes and splitp[splitplen+1-k] != 0:
                        #print("here onetwo")
                                                index[centrallocfor][frontcounter+1] = splitp[splitplen+1-k]
                                                frontcounter += 1
                                    elif otag == 1 and splitp[otag+1] in zeroes and splitp[otag+1] != 0:
                        #print("here two")
                                        for k in range(2,splitplen):
                                            if splitp[k] in zeroes and splitp[k] != 0:
                                                index[centrallocfor][frontcounter+1] = splitp[k]
                                                frontcounter += 1
                                        for k in range(2,splitplen):
                                            if splitp[splitplen+1-k] in ones and splitp[splitplen+1-k] != 0:
                                                index[centrallocback][backcounter+1] = splitp[splitplen+1-k]
                                                backcounter += 1
                        #print(index)
                                for k in range(indexlen[a]): #NOT SURE IF THIS WORKS, THIS IS THE PROPOSED CHANGE.
                                    for o in range(indexlen[index[a][k]-10]):
                                        if index[index[a][k]-10] != 7:
                                            if index[index[a][k]-10][o] == (a+10):
                                                index[index[a][k]-10][o] = (centralloc+10)
                                index[a] = 7
                        #print["index @"]
                        #print(index)
                        
                        
        #Above is for splitting along a C node that's on the edge of our terminal path. Next we split along a terminal path node in the center.
        
                            elif structureCheck:
                                #print("yeah we got here2")
                                tagtag = 0
                                for k in range(1,splitplen):
                                    if (splitp[k] in terminal or splitp[k] == (centralloc+10)) and (tagtag == 0):
                                        tagtag += 1
                                        starttag = k
                                    elif (splitp[k] in terminal or splitp[k] == (centralloc+10)) and (tagtag == 1):
                                        stoptag = k
                               #print(starttag)
                               #print(stoptag)
                               #print(ones)
                               #print(zeroes)
                                if splitp[starttag+1] in zeroes and splitp[starttag+1] != 0:
                                    if terminal[i-1] == splitp[starttag] or splitp[starttag] == (centralloc+10):
                                       #print("hmm")
                                        for k in range(starttag+1,stoptag):
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocfor][frontcounter+1] = splitp[k]
                                            frontcounter += 1
                                        for o in range(1,starttag):
                                            k = (starttag-o)
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocback][backcounter+1] = splitp[k]
                                            backcounter += 1
                                        for o in range(1,splitplen-stoptag):
                                            k = splitplen-o
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocback][backcounter+1] = splitp[k]
                                            backcounter += 1
                                    elif terminal[i-1] == splitp[stoptag] or splitp[stoptag] == (centralloc+10): #Do I even need this? Not sure.
                                        for o in range(starttag+1,stoptag):
                                            k = (stoptag+starttag-o)
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocfor][frontcounter+1] = splitp[k]
                                            frontcounter += 1
                                        for o in range(1,splitplen-stoptag):
                                            k = stoptag+o
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocback][backcounter+1] = splitp[k]
                                            backcounter += 1
                                        for k in range(1,starttag):
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocback][backcounter+1] = splitp[k]
                                            backcounter += 1
                                elif splitp[starttag+1] in ones and splitp[starttag+1] != 0:
                                    if terminal[i-1] == splitp[starttag] or splitp[starttag] == (centralloc+10):
                                        for k in range(starttag+1,stoptag):
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocback][backcounter+1] = splitp[k]
                                            backcounter += 1
                                        for o in range(1,starttag):
                                            k = (starttag-o)
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocfor][frontcounter+1] = splitp[k]
                                            frontcounter += 1
                                        for o in range(1,splitplen-stoptag):
                                            k = splitplen-o
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocfor][frontcounter+1] = splitp[k]
                                            frontcounter += 1
                                    elif terminal[i-1] == splitp[stoptag] or splitp[stoptag] == (centralloc+10): #Do I even need this? Not sure.
                                        for o in range(starttag+1,stoptag):
                                            k = (stoptag+starttag-o)
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocback][backcounter+1] = splitp[k]
                                            backcounter += 1
                                        for o in range(1,splitplen-stoptag):
                                            k = stoptag+o
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocfor][frontcounter+1] = splitp[k]
                                            frontcounter += 1
                                        for k in range(1,starttag):
                                            for l in range(indexlen[splitp[k]-10]):
                                                if index[splitp[k]-10][l] == (a+10):
                                                    index[splitp[k]-10][l] = (centralloc+10)
                                            index[centrallocfor][frontcounter+1] = splitp[k]
                                            frontcounter += 1

                                index[a] = 7
                               #print(index)
                            else: raise ValueError('There is no possible arrangement.')
                    #print("test")
                    #print(index[centrallocback])
                    #print(index)
                    temparray = [0]*(2*n+1)
                    temparray[0] = 3
                    tempcounter = 1
                    for i in range(frontcounter):
                        temparray[tempcounter] = index[centrallocfor][i+1]
                        tempcounter += 1
                    for i in range(backcounter):
                        temparray[tempcounter] = index[centrallocback][backcounter-i]
                        tempcounter += 1
                    index[centralloc] = temparray
                    indexlen[centralloc] = (frontcounter+backcounter+1)
                    index[centrallocback] = 0
                    reSortTag = False
                    quicktag = True
                    reSortPos = 0
                    #print(index)
                   #print("collapse")
                    for i in range(isize):
                        if index[i] == 7:
                            reSortTag = True
                    while reSortTag:
                        for i in range(isize):
                            if index[i] == 7 and quicktag:
                                quicktag = False
                                reSortPos = i
                        for i in range(reSortPos,isize):
                            index[i] = index[i+1]
                        isize -= 1
                        for i in range(isize):
                            if index[i] != 7 and index[i] != 0:
                                for k in range(len(index[i])):
                    #print(i)
                    #print(k)
                                    if index[i][k] >= (reSortPos+10):
                                        index[i][k] -= 1
                        reSortTag = False
                        for i in range(isize):
                            if index[i] == 7 and not reSortTag:
                                reSortTag = True
                                reSortPos = i
                       #print(index)
                    for i in range(n,2*n+1):
                        qrs = 0
                        if index[i] != 0:
                            for k in range(len(index[i])):
                                if index[i][k] != 0:
                                    qrs += 1
                        indexlen[i] = qrs
                   #print("wait what")
                   #print(index)
        #The above just splits our terminal path nodes that are C nodes, and does cleanup on the minor placeholder work we did in our algorithm.
        
        #The below is the display function. The idea is that we grab the first column in our set, then search all nodes to see what node touches that column, then stick on all columns from that node onto our display array, if it's a p node, then choose a node adjacent and move along that, etc etc, similar to traverse.

        displayArray = [0]*n
                    #print("display")
        displayArray[0] = 0
        displaySize = 1
        displaySet = [0]*(isize-n+2)
                    #print((isize-n))
        displayTry = [0]*isize
        trsize = 0
        lastDone = 0
        for i in range(n,isize):
            for j in range(len(index[i])):
                if index[i][j] == 10:
                   #print(index[i])
                   #print(i)
                    displaySet[0] = (i+10)
        displaySetSize = 1
        p = 0
        forwardBackCheck = 0
        while displaySize < n:
                    #print(displaySize)
            p += 1
                    #print(p)
            posMarker = -2
            progressTag = True
            otherTag = True
            nextSlot = 0
            prevSlot = 0
                    #print(displaySet[displaySetSize-1])
                    #print(displayArray)
                    #print(index)
                    #print(displaySet[displaySetSize-1]-10)
                    #print(index[displaySet[displaySetSize-1]-10])
            if index[displaySet[displaySetSize-1]-10][0] == 2:
                    #print("hmm3")
                    #print(n)
                lastDone = displaySet[displaySetSize-1]
                    #print("ifDis1")
                    #print(index[displaySet[displaySetSize-1]-10])
                    #print(indexlen[displaySet[displaySetSize-1]-10])
                for i in range(1,indexlen[displaySet[displaySetSize-1]-10]):
                    if displaySize == n:
                        otherTag = False
                    #print(index[displaySet[displaySetSize-1]-10][i])
                    #print(index[displaySet[displaySetSize-1]-10][i] < (n+10))
                    #print(index[displaySet[displaySetSize-1]-10][i] > 9)
                    if (index[displaySet[displaySetSize-1]-10][i] < (n+10)) and (index[displaySet[displaySetSize-1]-10][i] > 9) and not((index[displaySet[displaySetSize-1]-10][i]-10) in displayArray):
                    #print("Yep")
                        displayArray[displaySize] = (index[displaySet[displaySetSize-1]-10][i]-10)
                        displaySize += 1
                if displaySize < n:
                    quicktagtag = True
                    for i in range(1,indexlen[displaySet[displaySetSize-1]-10]):
                        if displaySize == n:
                            otherTag = False
                        if index[displaySet[displaySetSize-1]-10][i] >= (n+10) and ((index[displaySet[displaySetSize-1]-10][i]) not in displaySet) and ((index[displaySet[displaySetSize-1]-10][i]) not in displayTry) and index[displaySet[displaySetSize-1]-10][i] != 0 and quicktagtag:
                            progressTag = False
                    #print("display")
                    #print(displaySet)
                    #print(displaySetSize)
                            displaySet[displaySetSize] = (index[displaySet[displaySetSize-1]-10][i])
                            displaySetSize += 1
                            forwardBackCheck = 1
                            quicktagtag = False
                    if progressTag:
                        displayTry[trsize] = displaySet[displaySetSize-1]
                        displaySet[displaySetSize-1] = 0
                        forwardBackCheck = 2
                        displaySetSize -= 1
                        trsize += 1
            elif index[displaySet[displaySetSize-1]-10][0] == 3: #
                if (displaySetSize+trsize) != 1:
                    if forwardBackCheck == 1:
                        lastDone = displaySet[displaySetSize-2]
                    elif forwardBackCheck == 2:
                        lastDone = displayTry[trsize-1]
                    #print(displayArray)
                    #print("ifDis2")
                    for i in range (1,indexlen[displaySet[displaySetSize-1]-10]):
                        if index[displaySet[displaySetSize-1]-10][i] == lastDone:
                            posMarker = i
                    if posMarker == (indexlen[displaySet[displaySetSize-1]-10]-1):
                        nextSlot = 1
                    else:
                        nextSlot = posMarker + 1
                    if posMarker == 1:
                        prevSlot = (indexlen[displaySet[displaySetSize-1]-10]-1)
                    else:
                        prevSlot = posMarker - 1
                    if ((index[displaySet[displaySetSize-1]-10][nextSlot] in displayTry) or (index[displaySet[displaySetSize-1]-10][nextSlot] in displaySet)) and (index[displaySet[displaySetSize-1]-10][nextSlot] != 0):
                        if nextSlot == 1:
                            posMarker2 = posMarker - 1
                        else:
                            posMarker2 = posMarker
                        for i in range(1,posMarker2):
                            if displaySize == n:
                                otherTag = False
                            j = posMarker - i
                            if index[displaySet[displaySetSize-1]-10][j] < (n+10) and index[displaySet[displaySetSize-1]-10][j] > 9 and otherTag:
                                displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][j]-10
                                displaySize += 1
                            elif index[displaySet[displaySetSize-1]-10][j] >= (n+10) and otherTag:
                                otherTag = False
                                displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][j]
                                displaySetSize += 1
                                forwardBackCheck = 1
                        if displaySize == n:
                            otherTag = False
                        if otherTag:
                            for i in range(posMarker,indexlen[displaySet[displaySetSize-1]-10]-1):
                                if displaySize == n:
                                    otherTag = False
                                j = indexlen[displaySet[displaySetSize-1]-10]+posMarker-1-i
                                if index[displaySet[displaySetSize-1]-10][j] < (n+10) and index[displaySet[displaySetSize-1]-10][j] > 9 and otherTag:
                                    displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][j]-10
                                    displaySize += 1
                                elif index[displaySet[displaySetSize-1]-10][j] >= (n+10) and otherTag:
                                    otherTag = False
                                    #print(posMarker)
                                    displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][j]
                                    displaySetSize += 1
                                    forwardBackCheck = 1
                        if displaySize == n:
                            otherTag = False
                        if otherTag:
                            displayTry[trsize] = displaySet[displaySetSize-1]
                            displaySet[displaySetSize-1] = 0
                            forwardBackCheck = 2
                            displaySetSize -= 1
                            trsize += 1
                    elif ((index[displaySet[displaySetSize-1]-10][prevSlot] in displayTry) or (index[displaySet[displaySetSize-1]-10][prevSlot] in displaySet)) and (index[displaySet[displaySetSize-1]-10][prevSlot] != 0):
                    #print("ifDis3")
                        for i in range(posMarker+1,indexlen[displaySet[displaySetSize-1]-10]):
                            if displaySize == n:
                                otherTag = False
                            if index[displaySet[displaySetSize-1]-10][i] < (n+10) and index[displaySet[displaySetSize-1]-10][j] > 9 and otherTag:
                                displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][i]-10
                                displaySize += 1
                            elif index[displaySet[displaySetSize-1]-10][i] >= (n+10) and otherTag:
                                otherTag = False
                                displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][i]
                                displaySetSize += 1
                                forwardBackCheck = 1
                        if displaySize == n:
                            otherTag = False
                        if otherTag and posMarker != 1:
                            for j in range(1,posMarker):
                                if displaySize == n:
                                    otherTag = False
                    #print(posMarker)
                    #print(index[displaySet[displaySetSize-1]-10])
                                if index[displaySet[displaySetSize-1]-10][j] < (n+10) and index[displaySet[displaySetSize-1]-10][j] > 9 and otherTag:
                                    displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][j]-10
                                    displaySize += 1
                                elif index[displaySet[displaySetSize-1]-10][j] >= (n+10) and otherTag:
                                    otherTag = False
                                    displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][j]
                                    displaySetSize += 1
                                    forwardBackCheck = 1
                        if displaySize == n:
                            otherTag = False
                        if otherTag:
                            displayTry[trsize] = displaySet[displaySetSize-1]
                            displaySet[displaySetSize-1] = 0
                            forwardBackCheck = 2
                            displaySetSize -= 1
                            trsize += 1
                    else:
                    #print("ifDis4")
                        for i in range (1,indexlen[displaySet[displaySetSize-1]-10]):
                            if index[displaySet[displaySetSize-1]-10][i] == lastDone:
                                posMarker = i
                        for j in range(posMarker+1,indexlen[displaySet[displaySetSize-1]-10]):
                            if displaySize == n:
                                otherTag = False
                            if index[displaySet[displaySetSize-1]-10][j] < (n+10) and index[displaySet[displaySetSize-1]-10][j] > 9 and otherTag:
                                displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][j]-10
                                displaySize += 1
                            elif index[displaySet[displaySetSize-1]-10][j] >= (n+10) and otherTag:
                                otherTag = False
                                #print(index)
                                displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][j]
                                displaySetSize += 1
                                forwardBackCheck = 1
                        if displaySize == n:
                            otherTag = False
                        if otherTag:
                            for j in range(1,posMarker):
                                if displaySize == n:
                                    otherTag = False
                                if index[displaySet[displaySetSize-1]-10][j] < (n+10) and otherTag:
                                    displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][j]-10
                                    displaySize += 1
                                elif index[displaySet[displaySetSize-1]-10][j] >= (n+10) and otherTag:
                                    otherTag = False
                                    displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][j]
                                    displaySetSize += 1
                                    forwardBackCheck = 1
                        if displaySize == n:
                            otherTag = False
                        if otherTag:
                            displayTry[trsize] = displaySet[displaySetSize-1]
                            displaySet[displaySetSize-1] = 0
                            forwardBackCheck = 2
                            displaySetSize -= 1
                            trsize += 1
                else:
                    for i in range (1,indexlen[displaySet[displaySetSize-1]-10]):
                        if index[displaySet[displaySetSize-1]-10][i] == 10:
                            posMarker = i
                    #print(posMarker)
                    #print(indexlen[displaySet[displaySetSize-1]-10])
                    if posMarker != indexlen[displaySet[displaySetSize-1]-10]-1:
                        for j in range(posMarker,indexlen[displaySet[displaySetSize-1]-10]):
                    #print(displayArray)
                    #print(index[displaySet[displaySetSize-1]-10][j+1])
                    #print(n)
                            if otherTag:
                    #print("hmm2")
                    #print(j)
                                if displaySize == n:
                                    otherTag = False
                                if index[displaySet[displaySetSize-1]-10][j+1] < (n+10) and index[displaySet[displaySetSize-1]-10][j+1] > 9 and otherTag:
                    #print(index[displaySet[displaySetSize-1]-10])
                                    displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][j+1]-10
                                    displaySize += 1
                                elif index[displaySet[displaySetSize-1]-10][j+1] >= (n+10) and otherTag:
                    #print("hmm")
                                    otherTag = False
                                    displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][j+1]
                                    displaySetSize += 1
                                    forwardBackCheck = 1
                    #print(displaySet)
                        if otherTag:
                            if displaySize == n:
                                otherTag = False
                            for j in range(1,posMarker):
                                if index[displaySet[displaySetSize-1]-10][j] < (n+10) and otherTag:
                                    displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][j]-10
                                    displaySize += 1
                                elif index[displaySet[displaySetSize-1]-10][j] >= (n+10) and otherTag:
                                    otherTag = False
                                    displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][j]
                                    displaySetSize += 1
                                    forwardBackCheck = 1
                    #print(displayArray)
                    else:
                        for j in range(1,posMarker):
                            if displaySize == n:
                                otherTag = False
                            if index[displaySet[displaySetSize-1]-10][j] < (n+10) and otherTag:
                    #print(displaySet[displaySetSize-1])
                    #print(displaySet)
                                displayArray[displaySize] = index[displaySet[displaySetSize-1]-10][j]-10
                                displaySize += 1
                            elif index[displaySet[displaySetSize-1]-10][j] >= (n+10) and otherTag:
                                otherTag = False
                                displaySet[displaySetSize] = index[displaySet[displaySetSize-1]-10][j]
                                displaySetSize += 1
                                forwardBackCheck = 1


       #print("display")
        print(displayArray)
                    #Above is display

    def traverse(self, both, terminal, tried, tsize, trsize, termtag, counter, bsize, n, index, indexlen):
                    #print("TRAVERSE")
                    #print("both")
                    #print(both)
                    #print("index")
                    #print(index)
        array = index[counter]
        pathcheck = True
        testvar = 0
        #print(terminal)
        pathcheck = self.checkPath(both,terminal,pathcheck,bsize,tsize)
        tempcounter = 0
                    #print(pathcheck)
                    #print("terminal")
                    #print(terminal)
                    #print("tried")
                    #print(tried)
        if pathcheck:
            quicktag = False
            secondTag = True
            pathcheck = True
            if (counter+10) in both:
                quicktag = True
                    #print(array)
            for i in range(1, indexlen[counter]):
                if ((not((array[i]-10) in range(n))) and (not(array[i] in terminal)) and (not(array[i] in self.tried))): #should work now - where I stopped
                    pathcheck = self.checkPath(both,terminal,pathcheck,bsize,tsize)
                    if pathcheck:
                        secondTag = False
                    #print("if 1")
                        terminal[tsize] = array[i]
                        tsize += 1
                        temparray = [0]*5
                        temparray = self.traverse(both, terminal, tried, tsize, trsize, termtag, (array[i]-10), bsize, n, index, indexlen)
                        terminal = temparray[0]
                        tried = temparray[1]
                        tsize = temparray[2]
                        trsize = temparray[3]
                        termtag = temparray[4]
            pathcheck = self.checkPath(both,terminal,pathcheck,bsize,tsize)
            if pathcheck:
                if termtag is 0 and quicktag and secondTag:
                    #print("if 2")
                    temp = 0
                    temp = terminal[tsize]
                    termtag = 1
                    terminal = [0] * 2 * n
                    tried = [0] * 2 * n
                    tsize = 1
                    trsize = 0
                    terminal[0] = (temp+10)
                    temparray = self.traverse(both, terminal, tried, tsize, trsize, termtag, (array[i]-10), bsize, n, index, indexlen)
                    terminal = temparray[0]
                    tried = temparray[1]
                    tsize = temparray[2]
                    trsize = temparray[3]
                    termtag = temparray[4]
                elif (termtag is 1 and quicktag and (not secondTag)) or (len(terminal) is 1):
                    raise ValueError('There is no possible arrangement.')
                else:
                    #print("if 3")
                    #print(tried)
                    #print(terminal)
                    #print(trsize)
                    #print(tsize)
                    tried[trsize] = terminal[tsize-1]
                    trsize += 1
                    terminal[tsize-1] = 0
                    tsize -= 1
                    temparray = self.traverse(both, terminal, tried, tsize, trsize, termtag, (terminal[tsize-1]-10), bsize, n, index, indexlen)
                    terminal = temparray[0]
                    tried = temparray[1]
                    tsize = temparray[2]
                    trsize = temparray[3]
                    termtag = temparray[4]
                    #print("returned at")
                    #print(counter)
                    #print(terminal)
        returnarray = [terminal,tried,tsize,trsize,termtag]
        return returnarray


    def checkPath(self,both,terminal,pathcheck,bsize,tsize):
                    #print("checkPath")
        tuv = 0
        #print("check")
        #print(both)
        #print(terminal)
        for i in range(bsize):
            if both[i] in terminal:
                tuv += 1
                    #for k in range(tsize):
                    #print("i")
                    #print(i)
                    #print("k")
                    #print(k)
                    #     if terminal[k] == both[i]: #This is problematic. For some reason this is breaking python's limited recursion capabilities.
                    #     tuv += 1
                    #print(bsize)
                    #print(tuv)
        if tuv == bsize:
            pathcheck = False
        #print(pathcheck)
        return pathcheck







