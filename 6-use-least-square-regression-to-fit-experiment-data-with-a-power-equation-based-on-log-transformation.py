## The following code is written by Fatih Asci

import math
import matplotlib.pyplot as plt   #   pip install matplotlib (we wrote this in command prompt to install the module)
listV=[10,20,30,40,50,60,70,80]
listF=[25,70,380,550,610,1220,830,1450]
n=len(listV);
logV=[]
logF=[]
i=0
for i in range(0, n):
    logV.append(math.log10(listV[i]))
    print(i)
    print(logV[i])
    logF.append(math.log10(listF[i]))
    print(logF[i])
    i+=1  #now, need to fit this data into a straight line, by finding a0 and a1 as we have done in Q1-a
i=0
totallogV=0
totallogF=0
totallogVF=0
totallogV2=0
for i in range(0, n):
    totallogV+=logV[i]
    totallogF+=logF[i]
    totallogVF+=logV[i]*logF[i]
    totallogV2+=logV[i]*logV[i]
    i+=1
meanlogV=totallogV/(n)
meanlogF=totallogF/(n)
a1=(n*totallogVF-totallogV*totallogF)/((n*totallogV2)-(totallogV**2))
a0=meanlogF-a1*meanlogV
print("log(y)=", a0, "+",a1, "log(x)")
logFlinearised=[]   
i=0
for i in range(0, n):
    logFlinearised.append(a0+a1*logV[i])     #inserting values of log(V) into the linearised equation based where the eq is logF=a0 + (a1*logV) and we the slope of it is found as a1
    i+=1
alfa=10**(a0)
beta=a1
print("y=", alfa,"*","x^",beta )
i=0
plotted=[]
for i in range(0,n):
    plotted.append(alfa*(listV[i]**beta))      #inserting values of V into power equation based on log transformation where the eq is F=alfa*(V^beta)
    i+=1 
plt.plot(listV, plotted)
plt.xlabel('V axis')
plt.ylabel('F - axis')
plt.title('The graph of power equation based on F=âlfa*(V^beta) ')
plt.show()





