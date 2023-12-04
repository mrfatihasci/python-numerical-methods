## The following code is written by Fatih Asci

import matplotlib.pyplot as plt
F=[0,10,28,46,63,82,110,130]
x=[0,0.05,0.10,0.15,0.20,0.25,0.30,0.35]
## the area under the curve gives the work done by stretching
## which can be found by the trapezodial rule, 1/3 rule, or 3/8 rule
## the area can be calculated by 1 trapezodial rule + 2 3/8 simpsons rule.
## from x=0 to x=0.05 we'll use trapezodial rule
## from x=0.05 to 0.20 we'll have 3/8 simpson'S rule
## from 0.20 to 0.35 one another 3/8 simpson's rule
def trapezodial(x0,x1,fx0,fx1):
    I=(x1-x0)*(fx0+fx1)*(1/2)
    return(I)
def threeOverEightSimpsons (x0,x1,x2,x3,fx0,fx1,fx2,fx3):
    L=(x3-x0)*(1/8)*(fx0+3*fx1+3*fx2+fx3)
    return(L)
Area=0
print(Area)
Area+= trapezodial(x[0],x[1],F[0],F[1])
print(Area)
Area+= threeOverEightSimpsons(x[1],x[2],x[3],x[4],F[1],F[2],F[3],F[4])
print(Area)
Area+= threeOverEightSimpsons(x[4],x[5],x[6],x[7],F[4],F[5],F[6],F[7])
print('the work done by stretching from x=0 m to x=0.35 m is', Area,"Joule(N.m)")
plt.plot(x,F)
plt.xlabel('x')
plt.ylabel('F')
plt.title('the graph of Force applied versus displacement of spring')
plt.show()
