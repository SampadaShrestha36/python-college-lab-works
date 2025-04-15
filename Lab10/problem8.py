# Calculate the cumulative sum of a NumPy array and store the results in a new Pandas DataFrame column. 
import pandas as pd
import numpy as np
data={'Values': [100, 200, 300, 400, 500]}
df=pd.DataFrame(data)
na=np.array(df['Values'])
df['Cumulative_Sum']=np.cumsum(na)
print(df)