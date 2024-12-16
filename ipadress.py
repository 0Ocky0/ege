#2231
from ipaddress import *
net4 = list(ip_network('162.198.0.157/255.255.255.224',0))
a=0
print (net4)
for x in net4:
    a+=1
    print (f"{bin(int(x))[2:]},{x},{a}")
    s=bin(int(x))[2:]
    print (s,s.count('1'),s.count('0'))




#╨в╨╕╨┐ 13 11308
# 203.155.196.98

for i in range(23,24):
    subnet1=ip_network(f"203.155.196.98/{i}", 0)
    # for x in subnet1:
    #     print (x)
    print(subnet1)



#17330

for i in range(32,0,-1):
    subnet1=ip_network(f"98.162.71.150/{i}",0)


    subnet2=ip_network(f"98.162.71.140/{i}",0)
    if subnet1==subnet2:
        print(i,subnet1,subnet2)
        break
for x in subnet1:
    print (x)
# for x in ip_network(f"98.162.71.150/28",0):
#     print (ip_network(f"98.162.71.150/28",0),x)