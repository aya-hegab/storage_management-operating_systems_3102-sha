
def worstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        wstIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if wstIdx == -1:  
                    wstIdx = j  
                elif blockSize[wstIdx] < blockSize[j]:  
                    wstIdx = j
        if wstIdx != -1:  
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i] 
  
    print("Process No. Process Size Block no.") 
    for i in range(n): 
        print(i + 1, "         ",  
              processSize[i], end = "     ")  
        if allocation[i] != -1: 
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated") 


def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        bestIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if bestIdx == -1:  
                    bestIdx = j  
                elif blockSize[bestIdx] > blockSize[j]:  
                    bestIdx = j
        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i] 
  
    print("Process No. Process Size     Block no.") 
    for i in range(n): 
        print(i + 1, "         ", processSize[i],  
                                end = "         ")  
        if allocation[i] != -1:  
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated") 


def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n): 
        for j in range(m): 
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break
  
    print(" Process No. Process Size      Block no.") 
    for i in range(n): 
        print(" ", i + 1, "         ", processSize[i],  
                          "         ", end = " ")  
        if allocation[i] != -1:  
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated") 


if __name__ == '__main__':
    
    blockSize = []
    blockSize_num_of_elements = int(input("Enter number of elements of the block sizes: "))
    for i in range(0, blockSize_num_of_elements):
        ele = int(input(f"enter the element {i+1} : "))
        blockSize.append(ele)
    m = len(blockSize)
    
    processSize = []
    processSize_num_of_elements = int(input("Enter number of elements of the process sizes then enter the elements "))
    for i in range(0, processSize_num_of_elements):
        ele2 = int(input(f"enter the element {i+1} : "))
        processSize.append(ele2)
    n = len(processSize)
    
    choose = 0
    while choose != 4:
        choose = int(input("Now please enter the number of these storage management techniques : (1)Worst Fit (2)Best Fit (3)Next Fit (4)Exit : "))
        if choose == 1:
            worstFit(blockSize, m, processSize, n)
        elif choose == 2:
            bestFit(blockSize, m, processSize, n)
        elif choose == 3:
            firstFit(blockSize, m, processSize, n)
            
