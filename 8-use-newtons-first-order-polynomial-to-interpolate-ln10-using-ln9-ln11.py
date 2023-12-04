## The following code is written by Fatih Asci

import math
import numpy
truevalueofln10=numpy.log(10)
print(truevalueofln10)
ln9=2.1972246
ln11=2.3978953
interpolatedln10=ln9 + ((ln11-ln9)/(11-9))*(10-9)
print(interpolatedln10)
percentrelativeerror=((truevalueofln10-interpolatedln10)/truevalueofln10)*100
print("percent relative error of interpolation is:","%",percentrelativeerror)
