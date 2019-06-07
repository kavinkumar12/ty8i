x=int(input())
y=input().split()
k=[]
for i in range(0,x):
  if(int(y[i])==i):
    k.append(y[i])
if(k==[]):
  print("-1")
else:
  k.sort()
  for j in range(0,len(k)):
    print(k[j],end=" ")
