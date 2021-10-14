import numpy as np

"""
Function for generate MOS scale and non-MOS scale. 'gen' is the generator interval, I is the interval in which the scale spans (2 represents an octave)
n is the degree of the generation process (5 gives a pentatonic cale, 7 an heptatonic,etc).

According to Erv Wilson, only scales in which 2 different ratios appear could be called MOS scale. Purely MOS scale algorithm will be developed further.

This function is an application of the 3 gap theorem: https://en.wikipedia.org/wiki/Three-gap_theorem.

"""

"""
TODO:

-cut the decimal of certain numbers in successive_ratio list (due to the numerical approximation))
"""

def steinhaus_scl(I, gen, n):
    
    generated_ratios = [] #this array will be filled with the successive computed ratios from the generators and wrapped into [1;I]
    
    for i in range(0,n):
        ratio = np.power(gen, i)
        if ratio < I:
            generated_ratios.append(ratio)
        else:
            j = 1
            while ratio > I:
                ratio = ratio / I
            generated_ratios.append(ratio)
    ratios = sorted(generated_ratios) + [2]# here we order the ratio array in order to be easyly sent in a music application
    successive_ratios = [ratios[i+1]/ratios[i] for i in range(len(ratios) - 1)]
    print("ratios of the scale :", ratios)
    print("Successive ratios of the scale :", successive_ratios)

steinhaus_scl(2, 4/3, 7)
