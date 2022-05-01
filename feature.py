import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
# %matplotlib inline
from skimage.io import imread, imshow

image = imread('ImgPIA.jpg', as_gray=True)
imshow(image)