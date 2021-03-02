# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

print(os.getcwd())
print(__file__)
#img = imread('../dataset/lena.png') # 画像の読み込み
img = imread(os.getcwd()+r'\dataset\lena.png')
plt.imshow(img)

plt.show()