x,total=input("輸入月租費型式及通話時間").split(' ')
x=int(x)
total=int(total)
if(x==186 and 186<=total<186*2):
    print(total*0.9*0.09)
elif(x==186 and total>=186*2):
    print(total*0.8*0.09)
elif(x==386 and 386<=total<386*2):
    print(total*0.8*0.08)
elif(x==386 and total>=386*2):
    print(total*0.7*0.08)
elif(x==586 and 586<=total<586*2):
    print(total*0.7*0.07)
elif(x==586 and total>=586*2):
    print(total*0.6*0.07)
elif(x==986 and 986<=total<986*2):
    print(total*0.6*0.06)
elif(x==986 and total>=986*2):
    print(total*0.5*0.06)