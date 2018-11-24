#!/bin/sh
sudo tcpdump -w 20150122_1630.pcap -c 2000
bro -r 20150122_1630.pcap darpa2gurekddcup.bro > conn.list
sort -n conn.list > conn_sort.list
gcc trafAld.c -o trafAld.out
./trafAld.out conn_sort.list
python listtocsv.py
python extract.py
python kddtokddfin.py
mv key.txt ..
