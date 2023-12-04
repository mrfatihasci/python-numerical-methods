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
interpolatedln10=b0+b1*(x-x0)+b2*(x-x0)*(x-x1)
print(interpolatedln10)
percentrelativeerror=((truevalueofln10-interpolatedln10)/truevalueofln10)*100
print("percent relative error of interpolation is:","%",percentrelativeerror)
