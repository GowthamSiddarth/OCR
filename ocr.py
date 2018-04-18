import argparse
import cv2
import os

# construct the argument parse and parse the arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="path to input image")
arg_parser.add_argument("-p", "--preprocess", default="threshold", type=str, help="type of preprocessing to be done")

args = vars(arg_parser)

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if "threshold" == args["preprocess"]:
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif "blur" == args["preprocess"]:
    gray = cv2.medianBlur(gray, 3)

filename = "{}.png".format(os.getpgid())
cv2.imwrite(filename=filename, img=gray)
