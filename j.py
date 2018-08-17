def asfg(x):
 if x<2:
  flag=False
 elif x==2:
  flag=True
 else:
  flag=True
  for i in range (2,x-1)=
   if x%i==0:
    flag=False
    break
 return flag

p=input("num")
if asfg(p):
 print("es primo")
else:
 print("no es primo")

