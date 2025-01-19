from ipaddress import *
net4 = list(ip_network('218.194.82.148/255.255.255.192',0))
a=0
print (net4)
for x in net4:
    a+=1
    print (f"{bin(int(x))[2:]},{x},{a}")