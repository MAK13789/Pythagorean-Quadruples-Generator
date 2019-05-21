xval = []
yval = []
zval = []
for i in range(1, 50):
    for j in range(1, 50):
        for k in range(1, 50):
            a = i * i
            b = j * j
            c = k * k
            d = a + b + c
            e = d ** 0.5
            f = e.is_integer()
            if (f == True):
                #print (i)
                #print (j)
                #print (k)
                #print (e)
                #print (" ")
                xval.append(i)
                yval.append(j)
                zval.append(k)
print (xval)
print (" ")
print (yval)
print (" ")
print (zval)
