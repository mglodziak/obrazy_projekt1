import numpy as np
import matplotlib.pyplot as plt




def calc_min(img, row, col, r):
    min_value=img[row,col]
    width=img.shape[0]
    height=img.shape[1]   

    for i in range(row-r,row+r+1):
        for j in range(col-r, col+r+1):
            if i >=0 and i<width and j>=0 and j<height:
                if (i-row)*(i-row)+(j-col)*(j-col) <= r*r:
                    if img[i,j] < min_value:
                        min_value=img[i,j]
    return min_value

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

def open_image(img):
    img_out=np.zeros_like(img)
    img_out1=np.zeros_like(img)
   # img_out=img
    width=img.shape[0]
    height=img.shape[1]
    r=int(input("Enter a radius size (for example 6): "))

    ##erozja
    for i in range(height):
        for j in range(width):
            img_out1[i,j]=calc_min(img,i,j,r)

    #dylacja        
    for i in range(height):
        for j in range(width):
            img_out[i,j]=calc_max(img_out1,i,j,r)
    
    return img_out
    
