import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
  pil_img = Image.fromarray(np.unint8(img))

(x_train,t_train),(x_test,t_test) = load_mnist(flatten=Ture,normalize=False)
img = x_train[0]
label = t_train[0]
print(label)
print(img.shape)
img = img.reshape(28,28) #把图像的形状变成原来的尺寸
img_show(img)