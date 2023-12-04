## The following code is written by Fatih Asci

import math
import numpy
truevalueofln10=numpy.log(10)
print(truevalueofln10)
x0=8
x1=9
x2=11
x=10
fx0=ln8=2.0794415
fx1=ln9=2.1972246
fx2=ln11=2.3978953
b0=fx0
b1=(fx1-fx0)/(x1-x0)
b2=(((fx2-fx1)/(x2-x1))-b1)/(x2-x0)
fx3=b0+b1*(x-x0)+b2*(x-x0)*(x-x1)
print(fx3)
b3=(((fx3-fx2)/(x-x2))-b2)/(x-x0)
fx4=b0+b1*(x-x0)+b2*(x-x0)*(x-x1)+b3*(x-x0)*(x-x1)*(x-x2)
print(fx4)
percentrelativeerror=((truevalueofln10-fx4)/truevalueofln10)*100
print("percent relative error of interpolation is:","%",percentrelativeerror)
