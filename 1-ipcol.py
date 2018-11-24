import pandas as pd
d = pd.read_csv("tcpdump.csv", header=None)
q = pd.DataFrame(d.ix[:,5])
q.to_csv("ipfin.csv", index=False, header=False)