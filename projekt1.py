import argparse
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import cv2

def get_arguments():
    parser=argparse.ArgumentParser(prog='projekt1', usage='%(prog)s [options]')
    parser.add_argument("-x", "--xxx", help="dupajas", action="store_true")
    parser.add_argument("-y", "--yyy", help="dupas", action="store_true")
    parser.add_argument("-z", "--zzz", help="dup", action="store_true")
    parser.add_argument("-p", "--path", help="path to input png", required="True")
    results = vars(parser.parse_args())
    return results

def validate_arguments(args):
    count_true=sum(str(i) == "True" for i in args.values())
    return count_true

def validate_count_parameters(count):
    if count > 1:
        print("You used "+str(count)+ " parameters! You can use only one parameter of -x -y -z etc.")
        exit(1)
    elif count == 0:
        print("You must use one of -x -y -z parameters!")
        exit(1)

def read_image(path):
    img=cv2.imread(str(path),cv2.IMREAD_UNCHANGED)
    #img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def convert_to_rgb(img):
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def view_mono_images(input_img, output_img):
    view, (ax1, ax2) = plt.subplots(1,2)
    view.suptitle("Before and after transformation")
    ax1.imshow(input_img, cmap='gray', vmin=0, vmax=255)
    ax2.imshow(output_img, cmap='gray', vmin=0, vmax=255)
    plt.show()

def view_color_images(input_img, output_img):
    view, (ax1, ax2) = plt.subplots(1,2)
    view.suptitle("Before and after transformation")
    ax1.imshow(input_img, vmin=0, vmax=255)
    ax2.imshow(output_img, vmin=0, vmax=255)
    plt.show()

def show_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transform_x(img):
    print("XXX")

def transform_y(img):
    print("YYY")

def chose_transform(options, img):
    if str(options["xxx"]) == "True":
        transform_x(img)
    elif str(options["yyy"]) == "True":
        transform_y(img)

def binary_mono(image, width, height):
    img_out=np.zeros_like(image)
    for i in range(width):
        for j in range(height):
            if image[i][j]<150:
                img_out[i][j]=0
            else:
                img_out[i][j]=255
    return img_out

def binary_color(image, width, height):
    img_out=np.zeros_like(image)
    for i in range(width):
        for j in range(height):
            for k in range(3):
                img_out[i,j,k]=img[i,j,k]-20


##            if image[i,j,0]<150 and image[i,j,1]<100 and image[i,j,2]<40:
##                img_out[i,j,0]=0
##                img_out[i,j,1]=0
##                img_out[i,j,2]=0
##            else:
##                img_out[i,j,0]=255
##                img_out[i,j,1]=255
##                img_out[i,j,2]=255
                
    return img_out
            
def mono_image(img):
    width=img.shape[0]
    height=img.shape[1]
    img_out=binary_mono(img, width, height)
    chose_transform(options, img)
    view_mono_images(img,img_out)


def color_image(img):
    width=img.shape[0]
    height=img.shape[1]
    img_out=binary_color(img, width, height) ##
    
    view_color_images(img, img_out)


options=get_arguments()
count_given_parameters = validate_arguments(options)
validate_count_parameters(count_given_parameters)
img = read_image(options["path"])
try:
    if img.shape[2]:
        img = convert_to_rgb(img)
        color_image(img)
        
except:
    #print("mono")
    mono_image(img)


#img_out = read_image("./Test_card.png")
#img_out = convert_to_rgb(img_out)

#show_image(img)
#show_image(img_out)


