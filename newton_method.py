#! /usr/bin/env python
def f(x):
	return x**3 - 1 

def nwtn_meth(f,x_0,i):
	"""nwtn_meth(f,x_0,i) Finds one of the roots of formula f, using newton's method
	starting at point x_0 and iterating over i iterations"""
	import num_diff

	grad = num_diff.num_diff(f, x_0, 0.0001)
	x_j = x_0
	for j in range(i):
		x_j_new = x_j - f(x_j)/grad
		grad = num_diff.num_diff(f, x_j_new, 0.0001)
		x_j = x_j_new

	return x_j_new
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as img
import sys


numberOfPoints = int(sys.argv[1])
print sys.argv[1]
#numberOfPoints = 100

result_array = numpy.zeros((2*numberOfPoints,2*numberOfPoints,3), dtype="uint8")
numberOfRoots = 0
resultList = []


for i in range(-numberOfPoints,numberOfPoints,1):
	print i
	for k in range(-numberOfPoints,numberOfPoints,1):
		result = (nwtn_meth(f, i+(k*1j), 1000))

		# if the result is a root to the function
		fResult = f(result)
		if (fResult.real**2 + fResult.imag**2 < 0.01) & (fResult.real**2 + fResult.imag**2 > -0.01):
			# insert thing to find distinct roots here
			if len(resultList) == 0:
				resultList.append(result)

			distinctResult=True
			for l in range(len(resultList)):
				# for each previously found result, if the currently found result is very similar then the current result is not a distinct root
				if (result.real - resultList[l].real < 0.01) & (result.real - resultList[l].real > -0.01) & (result.imag - resultList[l].imag < 0.01) & (result.imag - resultList[l].imag > -0.01):
					distinctResult=False
					rootNumber=l
			if distinctResult==True:
				resultList.append(result)
				rootNumber = len(resultList)
					
		# if (result.real >= 0.99) & (result.real <= 1.01) & (result.imag <=0.01) & (result.imag >= -0.01):
		if(rootNumber == 0):
			result_array[k+numberOfPoints][i+numberOfPoints] = (255,0,0)
		# elif (result.real >= -0.51) & (result.real <= -0.49) & (result.imag >= 0.865) & (result.imag <= 0.867):
		if(rootNumber == 1):
			result_array[k+numberOfPoints][i+numberOfPoints] = (0,255,0)
		# elif (result.real >= -0.51) & (result.real <= -0.49) & (result.imag <= -0.865) & (result.imag >= -0.867):
		if(rootNumber == 2):
			result_array[k+numberOfPoints][i+numberOfPoints] = (0,0,255)
		if(rootNumber == 3):
			result_array[k+numberOfPoints][i+numberOfPoints] = (0,125,125)

image = plt.imshow(result_array)
numberOfRoots = len(resultList)
print "There are %d roots: " % (numberOfRoots) 
for l in range(len(resultList)):
	print "%f + %fj" % (resultList[l].real, resultList[l].imag)
plt.show()
