import numpy as np

# first test, list all the generator's degrees in an octave (octave reduced):
gen = 4/3 #generator: generating interval of the scale
I = 2 # interval we want to divide (2 is the octave)

sc0 = [] #array where the scale ratio are stored

# This algo fills an array with the consecutive ratios of the scale
for i in range(0,7):
    itemp = np.power(gen, i)
    if itemp < I:
        sc0.append(itemp)
    else:
        j = 1
        while itemp > I:
            itemp = itemp / I
        sc0.append(itemp)
        
print("MOS ratios : ", sc0)

sc0s = sorted(sc0) + [2]
print("MOS ratios sorted :", sc0s)

intervals = [sc0s[i+1]/sc0s[i] for i in range(len(sc0s) - 1)]
print("Succesive ratios of the MOS scale :", intervals)
