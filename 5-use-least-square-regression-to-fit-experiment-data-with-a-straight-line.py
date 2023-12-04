## The following code is written by Fatih Asci

import matplotlib.pyplot as plt
listV=[10,20,30,40,50,60,70,80]
listF=[25,70,380,550,610,1220,830,1450]
n=len(listV);
print(n)
totalV=0
totalF=0
totalVF=0
totalV2=0
i=0
for i in range(0, n):
    print(i);
    totalV+=listV[i]
    totalF+=listF[i]
    totalVF+=listV[i] * listF[i]
    totalV2+=listV[i] * listV[i]
    i+=1
print(totalV)
print(totalF)
print(totalVF) 
print(totalV2)
meanV=totalV/(n)
meanF=totalF/(n)
print(meanV)
print(meanF)
a1=(n*totalVF-totalV*totalF)/((n*totalV2)-(totalV**2))
a0=meanF-a1*meanV
print(a1)
print(a0)
print("the line equation equals to y=a0+a1*x which is:", end=" ")
print("y=", a0, "+", a1, "x")
plotted=[]
for i in range(0,n):
    plotted.append(a0+a1*listV[i])
    i+=1
plt.plot(listV, plotted)
# naming the x axis
plt.xlabel('V ')
# naming the y axis
plt.ylabel('F')
# giving a title to my graph
plt.title('The graph')
# function to show the plot
plt.show()
