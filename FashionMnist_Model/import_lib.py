from __future__ import division, print_function
import sys
import os
import glob
import re
import sys
import numpy as np
import cv2
import tensorflow as tf 
from tensorflow.keras import layers
from tensorflow import keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model,  Sequential
from keras.preprocessing import image
from keras.layers import Dense, Activation, BatchNormalization, Dropout, Flatten, Conv2D, MaxPooling2D, Input
from keras.optimizers import SGD
from keras.utils import to_categorical
from keras.api._v2.keras import callbacks

import numpy as np
import kerastuner
import matplotlib.pyplot as plt
from keras.api._v2.keras import callbacks
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevant.pywsgi import WSGIServer
