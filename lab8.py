import sys
import math
import cmath
import random
import numpy as np
import time 

def calcz(z, c, zabsmax):
	
	nit = 0;
	nitmax = 1000
	while abs(z) < zabsmax and nit < nitmax:
		z = z**2 + c; 
		nit += 1;
		ratio = (float(nit) / nitmax) * 255.0
	return ratio
	
	
def julia_loop(im_width, im_height, xwidth, yheight, xmin, ymin, nitmax):

	print("Calculate the 2D plane...")
	
	zabsmax = 10.0;
	c = complex(-0.1, 0.65)
	julia = np.zeros((im_width, im_height))
	for ix in range(im_width):
		for iy in range(im_height):
			nit = 0
			
			z = complex(float(ix) / im_width * xwidth + xmin,
						float(iy) / im_height * yheight + ymin)
						
			julia[ix][iy] = calcz(z,c,zabsmax)
	return julia
	

if __name__ == '__main__':
	if len(sys.argv) > 1:
		file = sys.argv[1]
	else:
		file = 'juliadata.txt'
		
		
	print("Julia set fractal generator\n")
	im_width = 1000;
	im_height = 1000;
	xmin, xmax = -0.5, 0.5;
	xwidth = xmax - xmin;
	ymin, ymax = -0.5, 0.5
	yheight = ymax - ymin;
	nitmax = 1000;
	zabsmax = 10.0;
	title = "Julia set fractal generator"
	julia = julia_loop(im_width, im_height, xwidth, yheight, xmin, ymin, nitmax)
	with open(file, 'w') as f:
		f.write(str(im_width) + '\n');
		f.write(str(im_height) + '\n');
		f.write(str(xmin) + '\n');
		f.write(str(xmax) + '\n');
		f.write(str(xwidth) + '\n');
		f.write(str(ymin) + '\n')
		f.write(str(ymax) + '\n')
		f.write(str(yheight) + '\n')
		#f.write(str(nitmax) + '\n')
		#f.write(str(zabsmax) + '\n')
		for i in julia:
			for j in i:
				f.write(str(j)+'\t')
		f.write('\n')
		
	p = time.perf_counter()
	print(p)