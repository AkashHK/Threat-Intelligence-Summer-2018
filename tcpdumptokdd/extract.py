import csv
import subprocess
a= subprocess.check_output("route -n | awk 'FNR == 3 {print $2}'",shell=True)
fg = open('tcpdump.csv','r')
inc = csv.reader(fg)
arr = []
for row in inc:
	arr.append(row[5])

look_for = set([])
look = []
for i in range(len(arr)):
	count = 0
	for j in range(i+1,len(arr)):
		if(arr[j] == arr[i]):
			count = count + 1
	if(count > 10):
		if a.rstrip() != arr[i]:
			if arr[i] not in look_for:
				look_for.add(arr[i])
				look.append(arr[i])

for k in range(len(look)):
	with open('tcpdump.csv','r') as inf, open('ip'+str(k+1)+'.csv','w') as outf:
	    incsv = csv.reader(inf)#, delimiter=',')
	    outcsv = csv.writer(outf)#, delimiter=',')
	    outcsv.writerows(row for row in incsv if row[5] == look[k])

f=open("key.txt","w")
f.write(str(len(look))+'\n')
for k in range(len(look)):
	f.write(str(look[k])+'\n')
#import pandas as pd
#df = pd.read_csv('wye_data.csv')
#df.to_csv('newdump.csv', index=False)
#route -n | awk 'FNR == 3 {print $2}'

