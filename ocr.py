import argparse

# construct the argument parse and parse the arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="path to input image")
arg_parser.add_argument("-p", "--preprocess", default="threshold", type=str, help="type of preprocessing to be done")

args = vars(arg_parser)
