import numpy as np

def calcz(z,c,zabsmax):
    '''
    calculates the recursive function z=z^2 + c; and counts how many iterations are needed to
    reach the maximum nitmax or reach the maximum for z (zabsmax). 
    The ratio (iterations/maxiterations) [range 0..1] times 255 is returned; this 
    allows to use these return values as a color scale between 0...255.
    '''
    nit = 0
    nitmax = 1000
    while abs(z) < zabsmax and nit < nitmax:
        z = z**2 + c
        nit += 1
        ratio = (float(nit) / nitmax) #* 255.0
    return ratio
        

def julia_loop(im_width, im_height, xwidth, yheight, xmin, ymin, nitmax):
    '''
    main loop that calculates recursive function for every pixel
    '''
    print("Calculate the 2D plane...")
    zabsmax = 10.0
    c = complex(-0.1,0.65)
    julia = np.zeros((im_width, im_height))
    for ix in range(im_width):
        for iy in range(im_height):
            nit = 0
            # Map pixel position to a point in the complex plane
            z = complex(float(ix) / im_width * xwidth + xmin,
                        float(iy) / im_height * yheight + ymin)
            # Do the iterations
            julia[ix][iy] = calcz(z,c,zabsmax)
    return julia