import pandas as pd
data=pd.read_csv("trafAld.csv",sep='\s+',header=None)
data.to_csv("tcpdump.csv", header=None)