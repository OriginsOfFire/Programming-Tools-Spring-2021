import numpy as np
import random as rnd

def main():
  size = rnd.randint(3, 7)
  a = [[rnd.randint(0, 10) for i in range(size)] for j in range(size)] 
  b = [[rnd.randint(0, 10) for i in range(size)] for j in range(size)] 
  
  A = np.array(a)
  B = np.array(b)
  
  res = A.dot(B)
  print(res)

if __name__ == "__main__":
  main()
