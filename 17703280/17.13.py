from ipaddress import *
ip1 = ip_address('157.220.185.237')
ip2 = ip_address('157.220.184.230')
otv = []
for mask in range(15,33):
    net = ip_network(f'157.220.185.237/{mask}', 0)
    if (ip1 in net) and (ip2 in net):
        count = 0
        for ip in net:
            if f'{ip:b}'.count('1') == 15:
                count += 1
        otv.append(count)
print(min(otv))
