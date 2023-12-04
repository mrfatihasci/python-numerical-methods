## The following code is written by Fatih Asci

number_str = input("Enter a number: ")
val=value=abs(int(number_str))
n=32  
i=0
list=[]
for i in range(0, n):
    while val > 0:
        if (val % 2) == 0:
            list.append(0) # adding the element to the array(corresponding to 'list' in python)
            val=val/2
            i +=1
        else:
            list.append(1) # adding the element to the array(corresponding 'list' in python)
            val -=1
            val=val/2
            i +=1
while len(list)<32:
    list.append(0)
print("")
print("The 32-bit binary representation of given number", value,"is:  ",end="")
for k in reversed(list):
    print( k, end =" ")
print("")
