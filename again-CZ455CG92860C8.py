import pandas as pd
import numpy as np
data = pd.read_csv("Road_from_Rehandle_Pad.csv")
low_memory=False

#not professionaly but defining data I would like to work with 

print(data.head())
vsecko = data.columns
print(vsecko)
data = data.iloc[1:-1]
#data = pd.to_numeric(data[['TimeStamp','T_D_Actual_brake_torque','IN_Engine_cycle_speed']])

time = data['TimeStamp']
#type(time)
#time = time.iloc[1:-1]
time = pd.to_numeric(time)
#print(time)
engine_speed = data['IN_Engine_cycle_speed']
engine_speed = pd.to_numeric(engine_speed)
#print(engine_speed)
torque = data['T_D_Actual_brake_torque']
torque = pd.to_numeric(torque)
#print(torque)
act_pos=data['ACM_Vgth_hb_position_dmnd_ctrl']
act_pos=pd.to_numeric(act_pos)
print(act_pos)

#first try to sorting data somehow 




