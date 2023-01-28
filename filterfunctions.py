import numpy as np
import cv2
import random

def gaussNoise(img):
    noisy_img = img.copy()
    row,col,ch= noisy_img.shape
    mean = 0
    var = 50
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = noisy_img + gauss
    return noisy
    

def gaussNoiseFilter(img):
    kernel = np.ones((3,3),np.float32)/9
    processed_image = cv2.filter2D(img,-1,kernel)
    return processed_image

def saltPepperFilter(img):
    processed_image = cv2.medianBlur(img, 3)
    processed_image = cv2.medianBlur(processed_image, 3)
    return processed_image
    
def saltPepper(img):
    noisy_img = img.copy()
    if(len(noisy_img.shape)!= 2):
        img = noisy_img[:,:,0]
    row , col = img.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        noisy_img[y_coord][x_coord] = 255
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0, row - 1)
        x_coord=random.randint(0, col - 1)
        noisy_img[y_coord][x_coord] = 0
    return noisy_img