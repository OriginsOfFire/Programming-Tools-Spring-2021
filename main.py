import numpy as np
import random as rnd
def main():
  size = rnd.randint(3, 7)
  a = np.array(size, size)
  b = np.array(size, size)
  
  for i in range(0, size):
    for j in range(0, size):
      a[i][j] = rnd.randint(0, 10)
      b[i][j] = rnd.randint(0, 10)
  
  res = a.dot(b)
  print(res)

if __name__ == "__main__":
  main()
