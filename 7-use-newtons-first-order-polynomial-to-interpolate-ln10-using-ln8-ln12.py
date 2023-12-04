## The following code is written by Fatih Asci

import math
import numpy
truevalueofln10=numpy.log(10)
print(truevalueofln10)
ln8=2.0794415
ln12=2.4849066
interpolatedln10=ln8 + ((ln12-ln8)/(12-8))*(10-8)
print(interpolatedln10)
percentrelativeerror=((truevalueofln10-interpolatedln10)/truevalueofln10)*100
print("percent relative error of interpolation is:","%",percentrelativeerror)
