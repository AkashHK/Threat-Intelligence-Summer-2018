import pandas as pd
import os
f=open("key.txt","r")
a=f.readline()
b=a.rstrip()
for k in range (int(b)):
	os.system("mkdir "+ str(k+1))
	data = pd.read_csv("ip"+str(k+1)+".csv",header=None)
	del data[0]
	del data[1]
	del data[2]
	del data[3]
	del data[4]
	del data[5]
	del data[7]
	del data[8]
	del data[9]
	#del data[10]
	data.to_csv(str(k+1)+'/o'+str(k+1)+'.csv', index=False, header=None)
	os.system("mv "+str(k+1)+" ..")
os.system("mv key.txt ..")
