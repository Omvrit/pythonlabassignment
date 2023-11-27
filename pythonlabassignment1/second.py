a=int(input("from where to find"))
b=int(input("till where to find"))
for i in range(a,b+1):
  num=i
  fact=1
  for j in range (1,num+1):
     fact=fact*j
  print(fact,end=",")