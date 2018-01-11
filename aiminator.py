import os
import sys
import tarfile
import zipfile
from time import time

import cv2
import numpy as np
import tensorflow as tf
from PIL import ImageGrab
import six.moves.urllib as urllib

# Tensorflow object_detection imports
import object_detection.utils.label_map_util as label_map_util
import object_detection.utils.visualization_utils as vis_util

from process import ImageProcess as ip
from templates import make_templates
from judge import Judge

NUM_CLASSES = 90


def setup():
    # Model to download.
    MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
    MODEL_FILE = MODEL_NAME + '.tar.gz'
    DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

    # Path to frozen detection graph. This is the actual model that is used for the object detection.
    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

    # List of the strings that is used to add correct label for each box.
    PATH_TO_LABELS = os.path.join('object_detection', 'data', 'mscoco_label_map.pbtxt')
    
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    if not os.path.exists(MODEL_FILE):
        print("Downloading the model...")
        opener = urllib.request.URLopener()
        opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
        tar_file = tarfile.open(MODEL_FILE)
        for file in tar_file.getmembers():
            file_name = os.path.basename(file.name)
            if 'frozen_inference_graph.pb' in file_name:
                tar_file.extract(file, os.getcwd())
        print("Completed\n")

    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    
    return detection_graph, category_index


def main():
    """
    Main function of the aiminator.py - captures the screen of the size 800x600 in
    the top-left corner of the screen and feeds a new window to display with detected
    models
    """
    # initialises fastfeaturedetector to get initial points of interests
    fast = cv2.FastFeatureDetector_create(threshold=50, nonmaxSuppression=50)

    # initialises Binary Robust Invariant Scalable Keypoints for
    # keypoint descriptor analyze
    br = cv2.BRISK_create()

    # BruteForce matcher to compare matches
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # initialize the data of the templates
    ct_models = make_templates('images/templates/CT/', fast, br)

    detection_graph, category_index = setup()

    j = Judge(detection_graph, category_index)
    j.analyse_screen(800, 600)

if __name__ == '__main__':
    main()
