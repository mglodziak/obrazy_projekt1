import numpy as np
import matplotlib.pyplot as plt

def test_print(img):
    print ("dupaaa")

def calculate_count_pixels(img):
    width=img.shape[0]
    height=img.shape[1]

    data=np.zeros(256)
    for i in range(height):
        for j in range(width):
            data[img[i,j]] +=1
            #print(img[i,j])
    print(data)
    return data

def make_histogram(data):
    plt.bar(range(256),data)
    plt.show()
    


def normalize_3_points_mono(img):
    in1=input("Enter value in1: ")
    out1=input("Enter value out1: ")
    in2=input("Enter value in2: ")
    out2=input("Enter value out2: ")
    in3=input("Enter value in3: ")
    out3=input("Enter value out3: ")
    img_out=np.zeros_like(img)
    width=img.shape[0]
    height=img.shape[1]
    i1=int(in1)
    i2=int(in2)
    i3=int(in3)
    o1=int(out1)
    o2=int(out2)
    o3=int(out3)
    for i in range(width):
        for j in range(height):
            if int(img[i,j])<=i1:
                img_out[i,j]=((0-o1)/(0-i1) * int(img[i,j]) - 0) + 0
            elif int(img[i,j])>i1 and int(img[i,j])<=i2:
                img_out[i,j]=((o1+1-o2)/(i1+1-i2) * int(img[i,j]) - i1) + o1
            elif int(img[i,j])>int(in2) and int(img[i,j])<=int(in3):
                img_out[i,j]=((o2+1-o3)/(i2+1-i3) * int(img[i,j]) - i2) + o2
            else:
                img_out[i,j]=((o3+1-255)/(i3+1-255) * int(img[i,j]) - i3) + o3
    return img_out




def normalize_3_points_color(img):
    in1=input("Enter value in1: ")
    out1=input("Enter value out1: ")
    in2=input("Enter value in2: ")
    out2=input("Enter value out2: ")
    in3=input("Enter value in3: ")
    out3=input("Enter value out3: ")
    img_out=np.zeros_like(img)
    width=img.shape[0]
    height=img.shape[1]
    i1=int(in1)
    i2=int(in2)
    i3=int(in3)
    o1=int(out1)
    o2=int(out2)
    o3=int(out3)
    for i in range(width):
        for j in range(height):
            for k in range(3):
                if int(img[i,j,k])<=i1:
                    img_out[i,j,k]=((0-o1)/(0-i1) * int(img[i,j,k]) - 0) + 0
                elif int(img[i,j,k])>i1 and int(img[i,j,k])<=i2:
                    img_out[i,j,k]=((o1+1-o2)/(i1+1-i2) * int(img[i,j,k]) - i1) + o1
                elif int(img[i,j,k])>int(in2) and int(img[i,j,k])<=int(in3):
                    img_out[i,j,k]=((o2+1-o3)/(i2+1-i3) * int(img[i,j,k]) - i2) + o2
                else:
                    img_out[i,j,k]=((o3+1-255)/(i3+1-255) * int(img[i,j,k]) - i3) + o3
    return img_out
