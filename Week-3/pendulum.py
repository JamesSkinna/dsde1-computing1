import math

def period(L, g):
        if isinstance(L, str) or isinstance(g, str):
            raise TypeError
        if (g <= 0) or (L<0):
            raise ValueError
        T = (2*math.pi)*(math.sqrt(L/g))
        return T

#def main():
   # Test = period(6, 0)
  #  print(Test)        

#if __name__ == "__main__":
 #   main() 
