import pandas as pd
import numpy as np
dict1 = {"Name":["Anish","Purujit","Souvik"],
         "Marks":["65","45","34"],
         "City":["Dankuni","Durgapur","Phulia"]
         }
df = pd.DataFrame(dict1)
print(df)
df.to_csv('Friends.csv')





