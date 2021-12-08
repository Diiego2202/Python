import math
x = int(input())
a=math.floor(x/3600)
b = x-(a*3600)
y = math.floor(b/60)
c = b-(y*60)
z = math.floor(c/60)
d = c-(z*60)
print(f'{a}:{y}:{d}')