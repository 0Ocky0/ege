P = [int(i) for i in range(10, 30)]
Q = [int(i) for i in range(13, 19)]
A = [int(i) for i in range(10, 30)]
for x in range(1, 52):
    if not (((x in A) <= (x in P)) or (x in Q)):
        A.remove(x)
print(len(A) - 1)
