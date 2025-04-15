# Load a CSV file into a Pandas DataFrame.
# import pandas as pd
# df=pd.DataFrame({'Name':['Suraj','Sudip','Pandey'],'Age':[20,21,22],'Gender':['Male','Male','Male'],'Rating':[3.5,4.0,4.5]})
# df.to_csv('test.csv',index=False)
import pandas as pd
df = pd.read_csv('test.csv')
print(df)