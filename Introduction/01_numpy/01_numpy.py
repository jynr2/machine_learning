import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])
array_range = np.arange(1, 7)

print(array)
print(array_range)

print(type(array))
print(type(array_range))

print(array[0])

array[0] = 100
print(array)

print(array.size)
array.sort()
print(array.size)
print(array[::-1])

print(array.dtype)

array_two = np.array([1, 2, 3, 4, 5, 6], dtype='i')
print(array_two)
print(array_two.dtype)
print(array_two.itemsize)