## The following code is written by Fatih Asci

import numpy as np
import matplotlib.pyplot as plt
import math
def function(h):
    I=math.e**(-2*h)
    return(I)
def forward(x,y):
    I=(function(x+y)-function(x))/(y)
    return(I)
def backward(x,y):
    I=(function(x)-function(x-y))/(y)
    return(I)
def central(x,y):
    I=(function(x+y)-function(x-y))/(2*y)
    return(I)
def truerelativeerror(x,y):   ## where x=true value, y=approximate value
    trueerror=x-y
    I=trueerror/x
    return(I)
def truevalue(x):
    I=-2*(math.e**(-2*x))
    return(I)
errorlistforward=[]
errorlistbackward=[]
errorlistcentral=[]
xaxes=[]
h=2 ##derivative value of whichever the number to calculate
for i in range(1,50):
    y=(float(i))/(100)
    errorlistforward.append(abs(truerelativeerror( truevalue(h),forward(h,y))))
    errorlistbackward.append(abs(truerelativeerror( truevalue(h),backward(h,y))))
    errorlistcentral.append(abs(truerelativeerror( truevalue(h),central(h,y))))
    xaxes.append(y)
    i+=1
plt.plot(xaxes,errorlistforward,label="relative true error of forward difference approximation", color="g")
plt.plot(xaxes,errorlistbackward,label="relative true error of backward difference approximation", color="b")
plt.plot(xaxes,errorlistcentral,label="relative true error of central difference approximation", color="r")
plt.xlabel('dx')
plt.ylabel('relative true error')
plt.title('the graph of relative true error of different methods in calculating derivative of f(x) wrt small x values')
plt.legend()
plt.show()





