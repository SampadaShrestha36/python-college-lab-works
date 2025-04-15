# Create a DataFrame from a NumPy array with custom column names.
import pandas as pd
import numpy as np
numpy_array = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
column_names = ['A', 'B', 'C']
df = pd.DataFrame(numpy_array, columns=column_names)
print(df)