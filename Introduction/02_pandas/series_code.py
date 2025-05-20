# %% [markdown]
# Pandas es una librería que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento y fáciles de usar. 
# * La estructura de datos principal es el DataFrame, que puede considerarse como una tabla 2D en memoria (como una hoja de cálculo, con nombres de columna y etiquetas de fila). 
# * Muchas funciones disponibles en Excel están disponibles mediante programación, como crear tablas dinámicas, calcular columnas basadas en otras columnas, trazar gráficos, etc.
# * Proporciona un alto rendimiento para manipular (unir, dividir, modificar…) grandes conjuntos de datos

# %% [markdown]
# La librería Pandas, de manera genérica, contiene las siguientes estructuras de datos:
# * **Series**: Array de una dimensión
# * **DataFrame**: Se corresponde con una tabla de 2 dimensiones
# * **Panel**: Similar a un diccionario de DataFrames

# %%
import pandas as pd
import numpy as np

# %%

# series

s = pd.Series([2, 4, 6, 8, 10])
print(s)

# Creación de un objeto Series inicializándolo con un diccionario de Python
altura = {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
s = pd.Series(altura)
print(s)

# %%
# Creación de un objeto Series inicializándolo con algunos 
# de los elementos de un diccionario de Python
altura = {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
s = pd.Series(altura, index = ["Pedro", "Julia"])
print(s)

# %%
# Creación de un objeto Series inicializandolo con un escalar
s = pd.Series(34, ["test1", "test2", "test3"])
print(s)

# %% [markdown]
# Acceso a los elementos de un objeto Series
# 
# Cada elemento en un objeto Series tiene un identificador único que se denomina **_index label_**.

# %%
# Creación de un objeto Series
s = pd.Series([2, 4, 6, 8], index=["num1", "num2", "num3", "num4"])
print(s)

# %%
# Accediendo al tercer elemento del objeto
s["num3"]

# %%
# loc es la forma estándar de acceder a un elemento de un objeto Series por atributo
s.loc["num3"]

# %%
# iloc es la forma estándar de acceder a un elemento de un objeto Series por posición
s.iloc[2]

# %%
# Accediendo al segundo y tercer elemento por posición
s.iloc[2:4]

# %% [markdown]
# Operaciones aritméticas con el objeto Series

# %%
# Creacion de un objeto Series
s = pd.Series([2, 4, 6, 8, 10])
print(s)

# %%
# Los objeto Series son similares y compatibles con los Arrays de Numpy
# Ufunc de Numpy para sumar los elementos de un Array
np.sum(s)

# %%
# El resto de operaciones aritméticas de Numpy sobre Arrays también son posibles
# Más información al respecto en la Introducción a Numpy
s * 2

# %% [markdown]
# Representación gráfica de un objeto Series

# %%
# Creación de un objeto Series denominado Temperaturas
temperaturas = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9]
s = pd.Series(temperaturas, name="Temperaturas")
s