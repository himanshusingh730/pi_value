from __future__ import division
import numpy as np
import math
a=1000000
x=0
i=1
for i in np.arange(1,a):
	if i is 0:
		continue
	else:
		x=x+(1/(i*i))
x=6*x
x=math.sqrt(x)
print (x)
