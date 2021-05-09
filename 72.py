n=int(input("請輸入n:"))
k=int(input("請輸入k:"))
total=0
x=n//k
total=n+x
if x>=k:
    y=x//k
    total+=y
print(total)