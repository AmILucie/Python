import pandas as pd
import numpy as np
data = pd.read_csv("Road_from_Rehandle_Pad.csv", skiprows=range(1,2))
data = data.astype(np.float32)

#data = pd.to_numeric(data)
# data = pd.to_numeric(data)
print(data)

