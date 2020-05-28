import numpy as np
import matplotlib.pyplot as plt

def entropy_mono(img):
    mask=int(input("Entry size of square mask (for example 7): "))
    img_out=np.zeros_like(img)
    width=img.shape[0]
    height=img.shape[1]
    max_value=0
    min_value=255
    res_array=[]
    for i in range(height):
        for j in range(width):
            count_of_squares=0
            ix=j-((mask-1)/2)
            iy=i-((mask-1)/2)
            histogram=np.zeros(256)
            for ii in range(mask):
                for jj in range(mask):
                    if ix+ii >= 0 and ix+ii <width and iy+jj>=0 and iy+jj<height:
                        #print(ix+ii, iy+jj)
                        count_of_squares +=1
                        histogram[img[int(ix+ii),int(iy+jj)]] += 1

            histogram = histogram / count_of_squares
            histogram = list(filter(lambda px: px > 0, histogram))
            res=-np.sum(np.multiply(np.log2(histogram), histogram))
            if res>max_value:
                max_value=res
            if res<min_value:
                min_value=res
            res_array.append(res)

    #print(res_array)
    ix=0
    for i in range(height):
        for j in range(width):
            img_out[j,i]=(res_array[ix] - min_value)/(max_value - min_value)*255
            ix +=1

    return img_out





def entropy_color(img):
    mask=int(input("Entry size of square mask (for example 7): "))
    img_out=np.zeros_like(img)
    width=img.shape[0]
    height=img.shape[1]
    max_value=0
    min_value=255  
    res_array=[]
    for i in range(height):
        for j in range(width):
            count_of_squares=0
            ix=j-((mask-1)/2)
            iy=i-((mask-1)/2)
            histR=np.zeros(256)
            histG=np.zeros(256)
            histB=np.zeros(256)
            for ii in range(mask):
                for jj in range(mask):
                    if ix+ii >= 0 and ix+ii <width and iy+jj>=0 and iy+jj<height:
                       # print(ix+ii, iy+jj)
                        count_of_squares +=1
                        histR[img[int(ix+ii),int(iy+jj),0]] += 1
                        histG[img[int(ix+ii),int(iy+jj),1]] += 1
                        histB[img[int(ix+ii),int(iy+jj),2]] += 1
            if count_of_squares == 0:
                print(i,j)
            histR = histR / count_of_squares
            #print(histR)
            histG = histG / count_of_squares
            histB = histB / count_of_squares
            histR = list(filter(lambda px: px > 0, histR))
            histG = list(filter(lambda px: px > 0, histG))
            histB = list(filter(lambda px: px > 0, histB))

            hist=histR+histG+histB

            res=-np.sum(np.multiply(np.log2(hist), hist))
            if res>max_value:
                max_value=res
            if res<min_value:
                min_value=res
            res_array.append(res)

    #print(res_array)
    ix=0
    for i in range(height):
        for j in range(width):
            img_out[j,i]=(res_array[ix] - min_value)/(max_value - min_value)*255
            ix +=1

    return img_out
