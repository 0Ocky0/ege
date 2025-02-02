from ipaddress import *
net4 = list(ip_network('98.162.77.94/98.162.64.0',0))
a=0
print (net4)
for x in net4:
    a+=1
    print (f"{bin(int(x))[2:]},{x},{a}")