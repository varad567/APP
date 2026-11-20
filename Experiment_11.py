"""
Experiment 11 - Create a Pandas Series with ten random numbers (CO-4)
"""
import numpy as np
import pandas as pd

np.random.seed(42)   # same random numbers every run

series = pd.Series(np.random.randint(1, 100, size=10))
print("Pandas Series with 10 random numbers:")
print(series)

# Series with custom index
labelled = pd.Series(np.random.rand(10).round(2), index=list("abcdefghij"))
print("\nSeries with custom index:")
print(labelled)

print("\nStatistics of the first series:")
print(series.describe())
print("\nValues greater than 50:")
print(series[series > 50])
