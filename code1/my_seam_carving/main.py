from SeamCarving import SeamCarving
import numpy as np
import cv2


import os


def main():
    input_dir = "input_image"
    output_dir = "output_image"

    input_path = os.path.join(input_dir, "input2.jpg")
    output_path = os.path.join(output_dir, "output2.jpg")

    image = cv2.imread(input_path)
    seam_carver = SeamCarving(image, 0.5)
    output = seam_carver.seam_carving()
    cv2.imwrite(output_path, output)


if __name__ == "__main__":
    main()
