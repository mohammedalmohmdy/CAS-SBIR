
import cv2, numpy as np

def extract_features(img):
    fft = np.fft.fft2(img)
    mag = np.abs(fft)
    prob = mag/(mag.sum()+1e-8)
    entropy = -np.sum(prob*np.log(prob+1e-8))
    return np.array([np.mean(img>0), entropy],dtype=np.float32)
