# %% [markdown]
# Es una librería fundamental para la computación cientifica en python
# 
# - proporsiona arrays de N dimensiones
# - implementa funciones matemáticas sofisticadas
# - proporsiona herramientas para integrar C/C++ y Fortran
# - proporsiona mecanismos para facilitar la realización de tareas relacionadas con álgebra lineal o números aleatorios

# %% [markdown]
# Arrays
# 
# - en numpy cada dimensión se denomina axis
# - el número de dimensiones se denimina rank
# - la lista de dimensiones con sus correspondiente longitud se denomina shape
# - el número total de elementos (multuplicar la longitud de las dimensiones) se denomina size

# %%
import numpy as np

zeros_array = np.zeros((2,4)) # array de dos dimensiones
print(zeros_array)
print(zeros_array.shape) # shape
print(zeros_array.ndim) # rank
print(zeros_array.size) # size

# %% [markdown]
# zeros_array es un array:
# - con 2 axis, el primero de longitud 2 y el segundo de longitud 4
# - con un rank igual a 2
# - con un shape igual a (2,4)
# - con un size igual a 8

# %%
ones_array = np.ones((2,4,6)) # array de tres dimensiones
print(ones_array)
print(ones_array.shape) # shape
print(ones_array.ndim) # rank
print(ones_array.size) # size

# %%
# arrays cuyo valor es indicado como segundo parámetro de la función
np.full((2,4,7), 8)

# %%
# numpy empty no es predecible, inicializa el array con los 
# valores que hayan en memeria en ese momento

np.empty((2,4))

# %%
# inicializando arrays con listas de python

numbers_list = [2,4,6,8]
array_list = np.array(numbers_list)
print(array_list)

array_list_two_dimensions = np.array([numbers_list, [10, 12, 14, 16]])
print(array_list_two_dimensions)


# %%
# creación de un array utilizando una función basada en rangos
#(mínimo, máximo, número de elementos)

array_ranges = np.linspace(0, 6, 10)
print(array_ranges)


# %%
# creación de arrays con valosres aleatorios

random_array = np.random.rand(2,3,4)
print(random_array)

# %%
# inicialización de un array con valores aleatiros conforme a una distrubución normal

random_array_normal = np.random.randn(2,4)
print(random_array_normal)

# %% [markdown]
# Acceso a los elementos de un array

# %%
# ejemplo con array de una dimensión

array_uni = np.array([1, 3, 5, 7, 9, 11])
print(array_uni.shape)
print(array_uni.ndim)
print(array_uni)

# accediendo al cuarto elemento
print(array_uni[4])

# slicing
print(array_uni[2:4])

# stride
print(array_uni[0::3])

# %%
# ejemplo con array de una multidimensional
array_mult = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(array_mult.shape)
print(array_mult)

# accediendo al cuarto elemento
print(array_mult[0,3]) # fila 0, elemento 3

# accediendo a la fila entera
print(array_mult[1:]) 

# accediendo al tercer elemento de todas las filas
print(array_mult[0:2, 2]) 
print(array_mult[:, 2]) # simplificado

# %% [markdown]
# Modificar un Array

# %%
# creación de un array inicializandolo con un rango de 0-27

arr_range = np.arange(28)
print(arr_range)

# cambiar las dimensiones

arr_range.shape = (7,4)
print(arr_range)

# la redimensión del array anterior apunta a los mismos datos
# si se modifica esto modificará el array original

arr_range2 = arr_range.reshape(4, 7)
print(arr_range2)

print('----- modificación de array copia -----')
arr_range2[0,2] = 50

print('array copia: \n', arr_range2)
print('array original: \n', arr_range)

# convertir array multidimensional en unidimensional

arr_range_uni = arr_range2.ravel()
print(arr_range_uni)


# %% [markdown]
# Operaciones aaritméticas con arrays

# %%
# crear 2 arrays unidimencionales

array_uni_op1 = np.arange(2, 18, 2)
array_uni_op2 = np.arange(8)

print('array 1:\n', array_uni_op1)
print('array 2:\n', array_uni_op2)

print('----- suma -----')
print(array_uni_op1 + array_uni_op2)

print('----- resta -----')
print(array_uni_op1 - array_uni_op2)

print('----- multiplicación -----')
print(array_uni_op1 * array_uni_op2)

# %% [markdown]
# Broadcasting
# 
# Si se aplican operaciones aritméticas con arrays que no tienen la misma forma (shape) numpy aplica una propiedad
# que se denomina como broadcasting

# %%
# operaciones aritméticad en arrays unidimensionales

array_uni_op3 = np.arange(5)
array_uni_op4 = np.array([3])

print('shape array 1: ', array_uni_op3.shape)
print('array 1: ', array_uni_op3)

print()

print('shape array 2: ', array_uni_op4.shape)
print('array : ', array_uni_op4)

print('----- suma -----')
print(array_uni_op3 + array_uni_op4)

print('----- resta -----')
print(array_uni_op3 - array_uni_op4)

print('----- multiplicación -----')
print(array_uni_op3 * array_uni_op4)

# %%
# operaciones aritméticads con array multidimensional y unidimensional

array_mult_op1 = np.arange(6)
array_mult_op1.shape = (2,3)
print('shape array 1', array_mult_op1.shape)
print('array 1 \n', array_mult_op1)

print()

array_mult_op2 = np.arange(6, 18, 4)
print('shape array 2', array_mult_op2.shape)
print('array 1 \n', array_mult_op2)

print('----- suma -----')
print(array_mult_op1 + array_mult_op2)

print('----- resta -----')
print(array_mult_op1 - array_mult_op2)

print('----- multiplicación -----')
print(array_mult_op1 * array_mult_op2)


# %% [markdown]
# Funciones estadísticas sobre arrays

# %%
# crear array unidimensiona

array_est1 = np.arange(1, 20, 2)
print('array 1: \n', array_est1)

# calcular la media de todos los valores de un array

print(array_est1.mean())

# suma de los elementos
print(array_est1.sum())

# %% [markdown]
# Funciones universales eficientes proporsionadas por numpy

# %%
# cuadrado de los elementos de un array

array_ufunc = np.arange(1, 20, 2)

print('----- square -----')
print(np.square(array_ufunc))

# raíz cuadrada de los elementos de un array

print('----- sqrt -----')
print(np.sqrt(array_ufunc))

# exponencial de los elementos de un array

print('----- exp -----')
print(np.exp(array_ufunc))

# logaritmo de los elementos de un array

print('----- log -----')
print(np.log(array_ufunc))


