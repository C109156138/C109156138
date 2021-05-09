a=int(input("輸入:"))
a=str(a)
b=list(a)
c=list(a)
b.sort()
c.sort(reverse=True)
d=str()
e=str()
for f in range(0,len(b),1):
    d=d+b[f]
    e=e+c[f]
d=int(d)
e=int(e)
print(e-d)