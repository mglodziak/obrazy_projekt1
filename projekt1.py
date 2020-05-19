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
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def view_images(input_img, output_img):
    view, (ax1, ax2) = plt.subplots(1,2)
    view.suptitle("Before and after transformation")
    ax1.imshow(input_img)
    ax2.imshow(output_img)
    plt.show()

def transform_x(img):
    print("XXX")

def transform_y(img):
    print("YYY")

def chose_transform(options, img):
    if str(options["xxx"]) == "True":
        transform_x(img)
    elif str(options["yyy"]) == "True":
        transform_y(img)


options=get_arguments()
count_given_parameters = validate_arguments(options)
validate_count_parameters(count_given_parameters)
img = read_image(options["path"])
img_out = read_image("./Test_card.png")
chose_transform(options, img)
view_images(img,img_out)


