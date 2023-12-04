## The following code is written by Fatih Asci

value=int(input("Enter a number:  "))
number=abs(value)
list=[]
Exponent=[]
RoundedError=[]
exponentBits =int(input("Enter a bit number for exponent:  "))
mantissaBits =int(input("Enter a bit number for mantissa:  "))
while number > 0:
    if (number % 2) == 0:
        list.append(0)
        number=number/2   
    else:
        list.append(1)
        number -=1
        number=number/2
del list[-1]   #here we delete the last value, which is going to be 1, from the list. new list is gonna be mantissa, its length is gonna give us exponent 
exponentDecimal=len(list)+(2**(exponentBits-1)-1)  #length of mantissa means the power of 2 in 2^(E-127)
while exponentDecimal > 0:
    if (exponentDecimal % 2) == 0:     
        Exponent.append(0) # adding the element to the array
        exponentDecimal=exponentDecimal/2
    else:
        Exponent.append(1) # adding the element to the array
        exponentDecimal -=1
        exponentDecimal=exponentDecimal/2   
while len(Exponent)<exponentBits:
    Exponent.append(0)   #here we add zeros to the exponent is 10011, it will be 10011000(3 zeros added but this is the reverse order of exponent)
while len(list)>mantissaBits:
    RoundedError.append(list[0])
    del list[0]
while len(list)<mantissaBits:
    list.insert(0,0)
if len(RoundedError)==0:
    RoundedError.append(0)
def printThemAll(sign,exponent,mantissa,roundingError):
    print("")
    print(exponentBits+mantissaBits+1, "bits binary representation of ", value,":  ",end="")
    if (sign>0):
        print(0, end="")   
        print("|",end="")
    else:
        print(1, end="")  
        print("|",end="")
    for k in reversed(exponent):
        print( k, end ="")
    print("|",end="")
    for d in reversed(mantissa):             
        print(d, end="")
    print("|")
    print("Rounding error in binary:  ", end="")
    for c in reversed(roundingError):
        print(c,end="")
    print(""),print("")



printThemAll(value, Exponent, list, RoundedError)