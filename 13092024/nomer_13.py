ip = '.'.join(f'{x:08b}' for x in [111,81,27,224])
print(ip)
mask = '.'.join(f'{x:08b}' for x in [111,81,27,192])
print(mask)
