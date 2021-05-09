x=input("請輸入一字元為:")
y=reversed(list(x))
if list(x)==list(y):
    print("YES")
else:
    print("NO")