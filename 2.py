n=int(input("輸入"))
a=n*2.10
b=n*2.10
c=(n-120)*3.02+120*2.10
d=(n-120)*2.68+120*2.10
e=(n-330)*4.39+210*3.02+120*2.10
f=(n-330)*3.61+210*2.68+120*2.10
g=(n-500)*4.97+170*4.39+210*3.02+120*2.10
h=(n-500)*4.01+170*3.61+210*2.68+120*2.10
x=(n-700)*5.63+200*4.97+170*4.39+210*3.02+120*2.10
y=(n-700)*4.50+200*4.01+170*3.61+210*2.68+120*2.10
if n<=120:
    print("Summer months:"+str(a))
    print("Non-Summer months:"+str(b))
elif 121<=n<=330:
    print("Summer months:"+str(c))
    print("Non-Summer months:"+str(d))
elif 331<=n<=500:
    print("Summer months:"+str(e))
    print("Non-Summer months:"+str(f))
elif 501<=n<=700:
    print("Summer months:"+str(g))
    print("Non-Summer months:"+str(h))
elif n>700:
    print("Summer months:"+str(x))
    print("Non-Summer months:"+str(y))
