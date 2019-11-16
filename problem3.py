n=int(input())
sum1=0
sum2=0
for i in range(0,n+1):
    sum1=sum1+(i**2)
for i in range(0,n+1):
    sum2=sum2+i
square=sum2**2
print(square-sum1)

