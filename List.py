import parcer


lst = []
lst = parcer.parse(parcer.get_html('https://www.random.org/integers/?num=10000&min=0&max=1&col=10&base=10&format=html&rnd=new'))
for i in range(0, len(lst)):
    lst[i] = int(lst[i])

quantityOne = sum(lst)
quantityZero = len(lst) - sum(lst)
d1 = {'One' : quantityOne , 'Zero' : quantityZero}
print(d1)


def doubleZero(b):
   n = 0
   for x in range(0,len(b)):
       if b[x] == 0 and b[x-1] == 0:
         n += 1
   return n


def doubleOne(u):
    n = 0
    for x in range(0,len(u)):
        if u[x] == 1 and u[x-1] == 1:
           n += 1
    return n


def oneZero(l):
    n = 0
    for x in range(0,len(l)):
        if l[x] == 0 and l[x-1] == 1:
            n += 1
    return n


def zeroOne(s):
    n = 0
    for x in range(0,len(s)):
        if s[x] == 1 and s[x-1] == 0:
            n += 1
    return n


dZe = doubleZero(lst) 
dOn = doubleOne(lst)
oZe = oneZero(lst)
zOn = zeroOne(lst)
d2 = {'Doble Zero' : dZe, 'Double One' : dOn, 'One Zero' : oZe, 'Zero One' : zOn} 
print(d2)


def tripleZero(h):
    n = 0
    for x in range(0,len(h)):
        if h[x] == 0 and h[x-1] == 0 and h[x-2] == 0:
            n += 1
    return n


def tripleOne(i):
    n = 0
    for x in range(0,len(i)):
        if i[x] == 1 and i[x-1] == 1 and i[x-2] == 1:
            n += 1
    return n


def zeroOneZero(t):
    n = 0
    for x in range(0,len(t)):
        if t[x] == 0 and t[x-1] == 1 and t[x-2] == 0:
          n += 1
    return n


def oneZeroOne(k):
    n = 0
    for x in range(0,len(k)):
        if k[x] == 1 and k[x-1] == 0 and k[x-2] == 1:
          n += 1
    return n


def oneZeroZero(y):
    n = 0
    for x in range(0,len(y)):
        if y[x] == 0 and y[x-1] == 0 and y[x-2] == 1:
          n += 1
    return n


def zeroZeroOne(w):
    n = 0
    for x in range(0,len(w)):
        if w[x] == 1 and w[x-1] == 0 and w[x-2] == 0:
          n += 1
    return n


def zeroOneOne(q):
    n = 0
    for x in range(0,len(q)):
        if q[x] == 1 and q[x-1] == 1 and q[x-2] == 0:
          n += 1
    return n


def oneOneZero(a):
    n = 0
    for x in range(0,len(a)):
        if a[x] == 0 and a[x-1] == 1 and a[x-2] == 1:
          n += 1
    return n

trZ = tripleZero(lst)
trO = tripleOne(lst)
zOz = zeroOneZero(lst)
oZo = oneZeroOne(lst)
oZz = oneZeroZero(lst)
zZo = zeroZeroOne(lst)
zOo = zeroOneOne(lst)
oOz = oneOneZero(lst)
d3 = {'Triple Zero' : trZ, 'Triple One' : trO, 'Zero One Zero' : zOz, 'One Zero One' : oZo, 'One Zero Zero' : oZz, 'Zero Zero One' : zZo,
'Zero One One' : zOo, 'One One Zero' : oOz}
print(d3)


def percentOne (one):
   return round(lst.count(1) * 100 / len(lst),2)


def percentZero(zero):
   return round(lst.count(0) * 100 / len(lst),2)


one = percentOne(lst)
zero = percentZero(lst)
d4 = {'Percent One' : one , 'Percent Zero' : zero}
print(d4)
