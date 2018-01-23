import os
import sys
from time import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageGrab


def samples(path):
    # initialises fastfeaturedetector to get initial points of interests
    fast = cv2.FastFeatureDetector_create(threshold=50, nonmaxSuppression=50)

    # initialises Binary Robust Invariant Scalable Keypoints for
    # keypoint descriptor analyze
    br = cv2.BRISK_create()

    # BruteForce matcher to compare matches
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    from src.process import ImageProcess as ip
    from src.templates import make_templates

    # initialize the data of the templates
    ct_models = make_templates('images/templates/CT/', fast, br)

    for file in os.listdir(path):

        image = cv2.imread(path + file)

        process = ip(image, ct_models, fast, br, bf, 'draw')

        image = cv2.cvtColor(process.image, cv2.COLOR_BGR2RGB)

        plt.imshow(image)
        plt.show()


def live_demo():

    # initialises fastfeaturedetector to get initial points of interests
    fast = cv2.FastFeatureDetector_create(threshold=50, nonmaxSuppression=50)

    # initialises Binary Robust Invariant Scalable Keypoints for
    # keypoint descriptor analyze
    br = cv2.BRISK_create()

    # BruteForce matcher to compare matches
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    from src.process import ImageProcess as ip
    from src.templates import make_templates

    # initialize the data of the templates
    ct_models = make_templates('images/templates/CT/', fast, br)
    start = time()
    while True:

        # captures the screen with ImageGrab in RGB.
        screen = np.array(ImageGrab.grab(bbox=(0, 27, 800, 627)))
        # converts it to BGR
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

        process = ip(screen, ct_models, fast, br, bf, 'draw')
        print('Loop took: {:.5} seconds'.format(time()-start))

        cv2.imshow('AimAssistant', process.image)
        start = time()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':

    sys.path.append('.')

    live_demo()