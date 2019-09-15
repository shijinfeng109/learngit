import numpy as np

def NAND(x1,x2):
  x = np.array([x1,x2])
  w = np.array([-0.5,-0.5])
  b = 0.7
  tmp = np.sum(x*w)+b
	if tmp <= 0:
    return 0
  else:
    return 1

for i in [(1,1),(1,0),(0,0),(0,1)]:
  result = NAND(i[0],i[1])
  print(str(i)+"-—>"+str(result))