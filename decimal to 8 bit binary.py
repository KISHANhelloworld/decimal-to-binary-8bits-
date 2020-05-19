num=int(input())
binary=[]
tem=num
n=1
while n<=8:
    bit=num%2
    num=num//2
    binary.append(bit)
    n+=1
binary.reverse()
print(binary)    
