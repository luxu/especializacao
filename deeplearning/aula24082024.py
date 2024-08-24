import tensorflow as tf
from keras import datasets, layers, models
import matplotlib as plt
import numpy as np

# Carregar o dataset 
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalizar os dados para valores entre 0 e 1
train_image, test_image = train_images / 255.0, test_images / 255.0

print(test_image)
