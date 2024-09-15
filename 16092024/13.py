ip = '.'.join(f'{x:08b}' for x in [98,162,201,94])
print(ip)
mask = '.'.join(f'{x:08b}' for x in [98,162,192,0])
print(mask)
