
def hammingEncode(input):
    contains_binary = False 
    for char in input:
        if char == "0" or char == "1":
            contains_binary = True
        else:
            #Any char is not 0 or 1 can jump out loop
            break
    if contains_binary:
        result = []
        parityBit = dict()
        power = 0
        i = 1 
        idx = 1
        while i < len(input) +1:
        # for i in range (1, len(input) + 1):
            if (idx == 2**power):
                # print("?")
                result.append(0)
                power+=1  
                print(idx)
                parityBit[idx] = 0
            else:
                # print(i)
                result.append(int(input[i-1]))
                i+=1
                
            idx+=1
        print(result)
        print(parityBit)
        calculateParityBit(result,parityBit)

    else:
        return "Error: Input must be binary!"


#['', '', '0', '', '1', '1', '0', '', '1', '0', '1']

# idx = 1 
# 1,3,5,7,9
# idx = 2 
# 2,3 ,4,5 ,7,8 ,10,11

def calculateParityBit(result,parityBit):
    # print(result[0::2])
    # print(result[0::3])
    # i = 1
    # while i < len(result)+1:
    #     # print("idx",i)
    #     if i %2 !=0:
    #         print(result[i-1])
    #     i+=1
    i = 2
    while i < len(result) +1:
        #start from index 2
        print(result[i-1])
        print(result[i-1+1])
        i+=2

    # for i in parityBit:
    #     sum = 0 
    #     # print(i)
    #     # if i == 1:
        #     for j in range (i-1,len(result),2):
        #         print(result[j])
    #     #     # sum += result[j]
    #     #     # print(sum)
    #     # if i == 2:
    #     print(result[::2])
    #     for i in range(1, len(result), 2):
    #         print(result[i])

        
    #     break
            
    # for i in range (1, len(result)+1):
    #     if i in parityBit:
    #         print("hey")
    #     else:
    #         print(i)
            


# print(hammingEncode("1100"))
#0111100
print(hammingEncode("0110101"))
#10001100101
# print(hammingEncode("COMP30650"))
#Error: Input must be binary!

