from ipaddress import*
net = ip_network('226.185.90.162/255.255.252.0',0)
count = 0
for ad in net:
    if ad == ip_address('226.185.90.162'):
        print(count)
    count += 1