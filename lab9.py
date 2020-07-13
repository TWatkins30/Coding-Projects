import matplotlib.pyplot as plt
import math
import time
def plot(mymap):
	fig = plt.figure()
	im = plt.imshow(mymap,cmap=plt.get_cmap('jet'), vmin=0, vmax=255)
	plt.show()
def calc(x,y):
	z = 0.0
	for i in range(1,11):
		z += math.sin(math.pow(x,1./i)) * math.cos(math.pow(y,1./i))
	return z
if __name__ == '__main__':
	output=[]
	start = time.time()
	for x in range(1000):
		line=[]
		for y in range(1000):
			nx = x/100.
			ny = y/100.
			z = calc(x,y) * 255
			line.append(z)
		output.append(line)
	end = time.time()
	print ("Time elapsed",end-start)
	plot(output)