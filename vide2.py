#tập hộp các điểm ảnh x y

import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0, 100,(25, 2)).astype(np.float32);
ketqua = np.random.randint(0, 2, (25, 1)).astype(np.float32);
red = trainData[ketqua.ravel()==1]

print(trainData)
print(ketqua)
print(red)