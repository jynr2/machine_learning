# %% [markdown]
# Regresión Lineal: Coste de un incidente de seguridad

# %% [markdown]
# En este ejercicio se explican los fundamentos básicos de la regresión lineal aplicada a un caso de uso sencillo relacionado con la Ciberseguridad.

# %% [markdown]
# Ejercicio
# 
# El ejercicio consiste en predecir el coste de un incidente de seguridad en base al número de equipos que se han visto afectados. El conjunto de datos es generado de manera aleatoria.

# %%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

X = 2 * np.random.rand(100, 1) # 100 valores, 1 dimensiones
y = 4 + 3 * X + np.random.rand(100, 1)

print('La longitud del conjunto de datos es:', len(X))

# %% [markdown]
# Modificación del conjunto de datos

# %%
data = {'n_equipos_afectados': X.flatten(), 'coste': y.flatten()} # flatten convertir un arreglo multidimensional en un vector unidimensional (una sola fila de datos).
df = pd.DataFrame(data)
df.head(10)

# %%
# Escalando el número de equpos afectados
df['n_equipos_afectados'] = df['n_equipos_afectados'] * 1000
df['n_equipos_afectados'] = df['n_equipos_afectados'].astype('int')

# Escalando el coste
df['coste'] = df['coste'] * 10000
df['coste'] = df['coste'].astype('int')

# %% [markdown]
# Construcción del modelo

# %%
# Construcción del modelo y ajuste de la función hipótesis
lin_reg = LinearRegression()
lin_reg.fit(df['n_equipos_afectados'].values.reshape(-1, 1), df['coste'])


# %%
# accediendo al parámetro theta 0 después del cálculo
lin_reg.intercept_

# %%
# accediendo al parámetro theta 1 después del cálculo
lin_reg.coef_

# %%
# Predicción para el valor mínimo y máximo del conjunto de datos de entrenamiento
X_min_max = np.array([[df["n_equipos_afectados"].min()], [df["n_equipos_afectados"].max()]])
y_train_pred = lin_reg.predict(X_min_max)

# %% [markdown]
# Predicción de nuevos ejemplos

# %%
x_new = np.array([[1300]]) # 1300 equipos afectados

# Predicción del coste que tendría el incidente
coste = lin_reg.predict(x_new) 

print("El coste del incidente sería:", int(coste[0]), "€")
