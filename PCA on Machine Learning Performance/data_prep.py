import numpy as np
import os
import cv2

# data initialization
w = 250
h = 250

def pic_loader(folder, txt_file, label):
    f = open(txt_file, 'r')
    data = f.readlines()  # read the text file line by line 
    images = np.zeros([len(data), w * h])
    for i in range(len(data)):
        s = data[i]
        ns = s.replace('\n','')
        path = os.path.join(folder, ns)
        print(path)
        image = cv2.imread(path)
        imagenew = image[:,:,0]  # only need 1 channel (total: 3 channels)
        down = (w, h)
        resizeimage = cv2.resize(imagenew, down, interpolation=cv2.INTER_LINEAR)
        sd = resizeimage.reshape(resizeimage.shape[0] * resizeimage.shape[1], 1)
        images[i, :] = sd[:, 0]
    return images