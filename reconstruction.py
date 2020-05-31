import numpy as np
import matplotlib.pyplot as plt
import cv2


def calc_max(img, row, col, r):
    max_value=img[row,col]
    width=img.shape[0]
    height=img.shape[1]   

    for i in range(row-r,row+r+1):
        for j in range(col-r, col+r+1):
            if i >=0 and i<width and j>=0 and j<height:
                if (i-row)*(i-row)+(j-col)*(j-col) <= r*r:
                    if img[i,j] > max_value:
                        max_value=img[i,j]
    return max_value


def negacja(img):
    width=img.shape[0]
    height=img.shape[1]
    neg=np.zeros_like(img)
    for i in range(width):
        for j in range(height):
            if img[i,j]==0:
                neg[i,j]=255
            else:
                neg[i,j]=0
    return neg

def reconstruction(img):
   # matryca=np.zeros_like(img)
    maska=np.zeros_like(img)
    maska_old=np.zeros_like(img)
    
    for i in range(maska.shape[0]):
        for j in range(maska.shape[1]):
            if i==0 or j == 0:
                maska[i,j]=255
                
    neg=np.zeros_like(img)
    width=img.shape[0]
    height=img.shape[1]

    neg=negacja(img)
   # print(neg)
    if_stop = True
    while if_stop is True:
        for i in range(width):
            for j in range(height):
                max_tmp=calc_max(maska_old, i,j,3)
                if max_tmp==255 and neg[i,j]==0:
                    maska[i,j]=max_tmp


        if maska is maska_old:
            if_stop=False

        maska_old=maska

    #img_out=negacja(maska)
    img_out = maska
    
    return img_out
