# PyAiminator

PyAiminator is a practice project and a demo for Tampere University of Technology
course ASE-7410.

I approached the object detection as a concept by trying to detect character models
in a classic game of Counter-Strike 1.6. Most of the image processing is done with 
OpenCV.


### Detection Strategy:
* Filtering and thresholding
* Analysing contours
* Matching features
* Matching color space


### Evaluation:

*NOTE* This repo does not include all the files necessary for evaluation process

The detection process is compared and evaluated using Tensorflow object detection API [link](https://github.com/tensorflow/models/tree/master/research/object_detection). Already trained model can detect a variety of different objects but I only used it to evaluate how many humans or different objects associated with Counter-Strike models can I detect.

Accepted objects:
- Human
- Backpack

Tensorflow threshold: 0.4


### Requirements

Basic usage for collecting and using Brute Force detection:
- Python 3.6.4
- Git

(Optional)
- Python 64-bit
- Tensorflow [object_detection](https://github.com/tensorflow/models/tree/master/research/object_detection) for judge.
- [RPNplus](https://github.com/huangshiyu13/RPNplus)


### Installation

Installing the repo:
```
$ git clone https://github.com/EemeliSaari/PyAiminator
$ cd PyAiminator
$ pip3 install -r requirements.txt
```

Using Tensorflow object_detection:

1. Clone/download Tensorflow [object_detection](https://github.com/tensorflow/models/tree/master/research/object_detection) folder to repository root
2. Follow protoc installation guide found:  [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)


### Examples

Example usage:

1. List of all available commands
```
$ python aiminator.py -h
```

2. Run a live demo
```
$ python aiminator.py --demo live
```

3. Display ImageProcess steps
```
$ python aiminator.py --demo steps
```

