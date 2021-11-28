import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0, 100,(25, 2)).astype(np.float32);
ketqua = np.random.randint(0, 2, (25, 1)).astype(np.float32);
red = trainData[ketqua.ravel()==1]

plt.scatter(red[:,0],red[:,1], 100, 'r', 's')
ptl.show()