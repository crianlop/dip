import numpy as np
import cv2
import random

def gaussNoise(img):
    if(len(img.shape)!= 2):
        img = img[:,:,0]
    mean = 0
    var = 1000
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, (img.shape[0],img.shape[1])) 
    noisy_image = np.zeros(img.shape, np.float32)
    noisy_image = img + gaussian
    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image

def gaussNoiseFilter(img):
    kernel = np.ones((3,3),np.float32)/9
    processed_image = cv2.filter2D(img,-1,kernel)
    return processed_image

def saltPepperFilter(img):
    processed_image = cv2.medianBlur(image, 3)
    return processed_image
def saltPepper(img):
    if(len(img.shape)!= 2):
        img = img[:,:,0]
    row , col = img.shape
    noisy_img = np.copy(img)
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        img[y_coord][x_coord] = 0
    return noisy_img