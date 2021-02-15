"""Helper functions

Reference: https://www.tensorflow.org/api_docs/python/tf/keras/Model
"""
import tensorflow as tf


class MNISTdataset: 
    """Class for holding dataset"""
    def __init__(self):
        self.MNIST = tf.keras.datasets.mnist
        self.TRAIN_DS = None
        self.VAL_DS = None
        self.TEST_DS = None
        self.load_MNIST_dataset()


    def load_MNIST_dataset(self): 
        """Load mnist dataset"""

        (x_train, y_train), (x_test, y_test) = self.MNIST.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        self.TRAIN_DS = [x_train[10000:], y_train[10000:]]
        self.VAL_DS = [x_train[:10000], y_train[:10000]]
        self.TEST_DS = [x_test, y_test]