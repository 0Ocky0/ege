# from itertools import *
# t="13 14 15 18 26 27 28 31 34 35 37 41 43 46 47 51 53 58 62 64 67 68 72 73 74 76 81 82 85 86"
# g="АБ АВ АГ АЖ БА БВ БД БИ ВА ВД ВБ ГА ГЕ ГЖ ДБ ДВ ДЕ ДИ ЕД ЕГ ЕИ ЕЖ ЖИ ЖЕ ЖГ ЖА ИБ ИЕ ИД ИЖ"
# s=set(g.replace(' ',''))
# for p in permutations(s):
#     nt=t
#     for i,v in enumerate(p):
#         nt=nt.replace(str(i+1),v)
#     if set(g.split())==set(nt.split()):
#         print (p)
from itertools import *
t="12 13 15 21 23 24 27 31 32 35 42 47 51 53 56 57 65 67 72 74 75 76"
g="АБ АК АИ БА БК БВ ВГ ВБ ВМ ГВ ГД ЕД ЕИ ИЕ ИА ИМ КБ КА КМ МВ МД МИ МК"
s=set(g.replace(' ',''))
for p in permutations(s):
    nt=t
    for i,v in enumerate(p):
        nt=nt.replace(str(i+1),v)
    if set(g.split())==set(nt.split()):
        print (p)