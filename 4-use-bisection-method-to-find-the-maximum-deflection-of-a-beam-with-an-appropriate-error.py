## The following code is written by Fatih Asci

L=6.0
x=0.0000001
inc=0.001
result=True
secondResult=False
def Function(x):
    Derivative= (((-5.0)*(x**4))+6*(L**2)*(x**2)-(6**4))
    return(Derivative)
i=0.0
if (Function(i+inc)*(Function(i))>0.0):
    result=True
else:
    result=False
while i<=6.0:
    if(Function(i+inc)*Function(i)>0.0):
        secondResult=False
    else:
        secondResult=True
    if (secondResult== result):
        i-=inc
        inc*=0.1
    if(inc<0.000000000000001):
        print("")
        print("dy/dx at the detected point of max deflection is close to 0,")
        print("And this dy/dx corresponds to:",Function(i+inc)*Function(i))
        print("Max declection is at x=",(i+inc),"m")
        break
    i+=inc
