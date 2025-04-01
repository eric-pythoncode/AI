import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test), = tf.keras.datasets.moist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0