import math

def period(L, g):
    try:
        if isinstance(L, str) or isinstance(g, str):
            raise TypeError
        if (g <= 0) or (L<0):
            raise ValueError
        T = (2*math.pi)*(math.sqrt(L/g))
        return T
    except: 
        print("error")
    
    
        
    
