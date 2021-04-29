def parityBits(strLen):
    num=2
    while 2**num-1<strLen+num:
        num+=1
    return num
def hammingEncoder(userInput):
    s=list(userInput)
    k=parityBits(len(s))
    lis=[]
    for i in range(k):
        s.insert(2**i-1,'0')
    for i,val in enumerate(s):
        if val=='1':
            lis.append(i+1)
        elif val!='0':
            return 'Error: Input must be binary!'
    res=0
    for i in lis:
        res^=i
    for i in range(k):
        s[2**i-1]=str(res%2)
        res//=2
    return ''.join(s)


print(hammingEncoder("0110101"))