n=int(input())
list=[]
for i in range(n):
    email=input()
    list.append(email)
for str in list:
    str1=str.endswith(".com")
    if str1==True:
        print(str)