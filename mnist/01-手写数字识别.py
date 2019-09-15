import sys,os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train,t_train),(x_text,t_text) = load_mnist(flatten=True,normalize=False)
# print(x_train.shape)
print("x_train.shape:"+str(x_train.shape[0])+","+str(x_train.shape[1]))
# print(t_train.shape)
print("t_train.shape:"+str(t_train.shape[0])+",")
print("x_text.shape:"+str(x_text.shape[0])+","+str(x_text.shape[1]))
print("t_text.shape:"+str(t_text.shape[0])+",")
# print(t_text.shape) #查看 t_text.shape为1维数组