from recognizer import Recognizer, Morphology
import cv2 as cv


def print_hi():
    img = cv.imread("static/img_1.png", cv.IMREAD_GRAYSCALE)
    s = Recognizer.recognize(img, Morphology)
    print(s)


if __name__ == "__main__":
    print_hi()
