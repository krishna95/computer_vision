import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
from scipy.misc import imread

def rgb2grey(image):
    grey =np.floor(np.mean (image,axis = 2))
    return grey

def equalise(image):
	rows,cols,channels = image.shape
	if (channels == 3):
		image = rgb2grey(panda)
	bright_sum = hist = np.zeros(256)
	psum=0
	for i in range(0,rows):
		for j in range(cols):
			bright_sum[image[i][j]]=bright_sum[image[i][j]] + 1
	number_of_pixels=rows*cols
	for i in range(256):
		psum = bright_sum[i] + psum
		hist[i] = np.floor(255*1.0*psum)/number_of_pixels
	new = np.zeros((rows,cols))
	for i in range(rows):
		for j in range(cols):
			new[i][j]=hist[image[i][j]]
	return new

if __name__ == "__main__":
	panda = imread('panda.jpg')
	grey = rgb2grey(panda)
	equal = equalise(panda)
	plt.hist(grey.flatten())
	plt.show()
	plt.hist(equal.flatten())
	plt.show()
