import math
# Basic Dynamic Model of Cancer's Cells Population with initial state - population: Nzero, proportionality constant: r, bearing capacity: k,  at time: t 
#(Malthus - Logisitc Model)
def N(t,r,k,N_zero):
    if t>0:
        N = k*N_zero/(N_zero + ((k-N_zero)*(math.e**(-(r)*t))))
    else:
        print('Error')
    return N 
        