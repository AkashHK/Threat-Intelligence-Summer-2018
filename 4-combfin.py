import pandas as pd
import csv
f=open("key.txt",'r')
a=f.readline()
b=int(a.rstrip())
for k in range(b):
	to_merge = [str(k+1)+'/{}.csv'.format(i) for i in range(38)]
	dfs = []
	for filename in to_merge:
	    # read the csv, making sure the first two columns are str
	    df = pd.read_csv(filename, header=None, converters={0: str, 1: str})
	    # throw away all but the first two columns
	    df = df.ix[:,:1]
	    # change the column names so they won't collide during concatenation
	    df.columns = [filename + str(cname) for cname in df.columns]
	    dfs.append(df)

	# concatenate them horizontally
	merged = pd.concat(dfs,axis=1)
	# write it out
	merged.to_csv("merged"+str(k+1)+".csv", header=None, index=None)
