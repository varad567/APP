"""
Experiment 10 - Create a one-dimensional NumPy array containing numbers 1 to 10 (CO-4)
"""
import numpy as np

arr = np.arange(1, 11)

print("Array:", arr)
print("Type:", type(arr))
print("Data type:", arr.dtype)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)

# Basic operations on the array
print("\nSum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max(), " Min:", arr.min())
print("Array * 2:", arr * 2)
print("Even numbers:", arr[arr % 2 == 0])
print("First five elements:", arr[:5])
print("Reversed:", arr[::-1])
