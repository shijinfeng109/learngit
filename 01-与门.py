import numpy as np

# x = np.array([1,2,4])
#y = np.array([2,3,4])
#dot = np.dot(x,y)
#z = x*y
#print(dot,z)


def AND (x1,x2):
  x = np.array([x1,x2])
  w = np.array([0.5,0.5])
  b = -0.7
  result = np.sum(x*w)+b
  if result <= 0:
    return 0
  else:
    return 1

if __name__ == "__main__":
	for i in [(1,1),(1,0),(0,0),(0,1)]:
  	  y = AND(i[1],i[0])

  	  print (str(i)+"-—>"+str(y))


