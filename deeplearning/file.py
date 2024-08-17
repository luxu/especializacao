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

# Separar características e alvo
x = df.drop('median_house_value', axis=1)
y = df['median_house_value']

# formalizar características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(x)


# Dividir o dataset
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, )



# Avaliar o modelo
# loss = model.evaluate(X_test, y_test)
# print(f'loss (MSE): {loss}')

# Construir o modelo
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape(1),)),
    Dense(64, activation='relu'),
    Dense(1) # Saída única para regressão
])

# Compilar o modelo