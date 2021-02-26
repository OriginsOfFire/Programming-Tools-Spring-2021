import numpy as np
import random as rnd
def main():
  size = rnd.randint(3, 7)
  a = [[size], [size]]
  b = [[size], [size]]
  
  for i in range(0, size):
    for j in range(0, size):
      a[i][j] = rnd.randint(0, 10)
      b[i][j] = rnd.randint(0, 10)
      
  A = np.array(a)
  A = np.array(b)
  
  
  
  res = A.dot(B)
  print(res)

if __name__ == "__main__":
  main()
