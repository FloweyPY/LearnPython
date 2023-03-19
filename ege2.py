print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x <= (not(y <= z))) or w) == False:
                    print(x, y, z, w)
                    
perem = (2*729**1021-2*243**1022+81**1023-2*27**1024-1025, 3)
print(perem)