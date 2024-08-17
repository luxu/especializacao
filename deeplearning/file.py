import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#from tensorflow.keras.layers import Dense


# Carregar o dataset
california = fetch_california_housing()

#print(california.keys())

# Criar um DataFrame
df = pd.DataFrame(data=california.data, columns=california.feature_names)

df['median_house_value'] = california.target

print(df.head())

