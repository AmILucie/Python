import pandas as pd
import numpy as np
data = pd.read_csv("Road_from_Rehandle_Pad.csv", index_col=0)


#not professionaly but defining data I would like to work with 

print(data.head())
#vsecko = data.columns
#print(vsecko)
data = data.iloc[1:-1]
#data = pd.to_numeric(data[['TimeStamp','T_D_Actual_brake_torque','IN_Engine_cycle_speed']])
#print(data)
data[['Time', 'Torque', 'Engine_speed', 'Act_pos']] = data[['Time', 'Torque', 'Engine_speed', 'Act_pos']].apply(pd.to_numeric)
print(data[['Time', 'Torque', 'Engine_speed', 'Act_pos']].dtypes)

#first try to sorting data somehow 
test_time = data.Time.iloc[-1] #value of last time stamp 
print(test_time)







#iloc je funkce pro definici lokace  
# df.iloc[1:4]
#for index, row in df.iterrows()
#d data == 


