import poly.polyomino as pm

n = 4

for pol in pm.free(pm.generate(n)):
    print(pol, "\n")
