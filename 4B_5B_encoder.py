


AB_5B = {
    "0000":"11110",
    "0001":"01001",
    "0010":"10100",
    "0011":"10101",
    "0100":"01010",
    "0101":"01011",
    "0110":"01110",
    "0111":"01111",
    "1000":"10010",
    "1001":"10011",
    "1010":"10110",
    "1011":"10111",
    "1100":"11010",
    "1101":"11011",
    "1110":"11100",
    "1111":"11101"
}

# print(AB_5B.get("0000"))
def modulateInputs(input):
    #input checking 
    contains_digit = False
    for char in input:
        if char == "0" or char == "1":
            contains_digit = True
    #check user input is 4 bit and is int char
    if contains_digit and len(input) % 4 == 0:
        result=list()
        n = 4
        input = [input[i:i+n] for i in range(0, len(input), n)]
        # print(input)
        for item in input:
            result.append(AB_5B[str(item)])
            ans = "".join(result)
        return ans
    else:
        return "Error: Input must be in 4 bit binary "

# print(modulateInputs("11110000"))
#1110111110

# print(modulateInputs("COMP30650"))
# print(len("1100") % 4 == 0)
print(modulateInputs(""))
	
#Error: Input must be in 4 bit binary