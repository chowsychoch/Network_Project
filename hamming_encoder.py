
def hammingEncode(input):
    contains_binary = False 
    for char in input:
        if char == "0" or char == "1":
            contains_binary = True
        else:
            #Any char is not 0 or 1 can jump out loop
            break
    if contains_binary:
        result = list()
        power = 0
        i = 1 
        idx = 1
        while i < len(input) +1:
        # for i in range (1, len(input) + 1):
            if (idx == 2**power):
                # print(idx)
                power+=1  
                
            else:
                # print("Not a pow")
                i+=1
            idx+=1
    else:
        return "Error: Input must be binary!"



# print(hammingEncode("1100"))
#0111100
print(hammingEncode("0110101"))
# print(hammingEncode("COMP30650"))
#Error: Input must be binary!

