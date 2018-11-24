import os
att=set(["back","buffer_overflow","ftp_write","guess_passwd","imap","ipsweep","land","loadmodule","multihop","neptune","nmap","perl","phf","pod","portsweep","rootkit","satan","smurf","spy","teardrop","warezclient","warezmaster"])
f=open("key.txt",'r')
a=f.readline()
b=int(a.rstrip())
for k in range(b):
	f1 = open("ip"+str(k+1)+".txt", "r")
	a=f.readline()
	c=a.rstrip()
	count=0
	n=0
	for x in f1:
		n=n+1
		if x.rstrip() in att:
			count=count+1
	if count >= 0.5*n:	
		os.system("sudo blockip "+str(c))
