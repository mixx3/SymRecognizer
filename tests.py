from recognizer import Recognizer, Morphology, Correlation
import cv2 as cv


if __name__ == "__main__":
    img = cv.imread("static/img_2.png", cv.IMREAD_GRAYSCALE)
    print(Recognizer.recognize(img, Morphology))
    print(Recognizer.recognize(img, Correlation))
