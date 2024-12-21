from ipaddress import *
from itertools import *
cnt = 0
for ip in ip_network("170.155.137.181/170.155.136.0", 0):
    bin_ip = format(ip, 'b')
    if bin_ip[:16].count("1") >= bin_ip[16:].count("1"):
        print(cnt)