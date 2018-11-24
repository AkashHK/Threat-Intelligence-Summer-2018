import pandas as pd
import numpy as np
import datetime
f=open("key.txt",'r')
a=f.readline()
b=int (a.rstrip())
for k in range(b):
	data = pd.read_csv(str(k+1)+'/o'+str(k+1)+".csv",header=None)
	d=list(data)
	for i in range(1,39,1):
		y=str(i)
		d=pd.DataFrame(data.iloc[:,i-1])
		d.columns=["Month"]
		d["#Passengers"]=d["Month"]
		for j in range(len(d)):
			x=datetime.datetime.now()
			d.loc[j,'Month']=x.strftime('%H-%M-%S.%f')
		d.to_csv(str(k+1)+'/'+'sep'+y+'.csv', index=False)
