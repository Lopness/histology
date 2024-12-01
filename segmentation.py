from skimage import data
#import numpy as np
import matplotlib.pyplot as plt
from skimage import io
#from scipy import ndimage
from skimage import filters
from skimage.filters import gaussian
from skimage.feature import peak_local_max

img = io.imread('C:/Users/User/Desktop/DAPI_40.tif')
plt.imshow(img)
#plt.show()

def detect_nuclei(img, sigma=4, min_distance=3, threshold_abs=400):
    g = gaussian(img, sigma, preserve_range=True)
    return peak_local_max(g, min_distance, threshold_abs)

centers = detect_nuclei(img)
count_cell = len(centers.tolist())

plt.figure(figsize=(12, 12))
plt.imshow(img, cmap='gray', vmax=4000)
plt.plot(centers[:, 1], centers[:, 0], 'r.')
plt.axis('off')
#plt.show()
print(count_cell)