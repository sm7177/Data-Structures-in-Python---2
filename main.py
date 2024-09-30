# mytuple=["hello",[1,2,3,4],3.4,1.1,"nais"]
# for i in (mytuple):
#     print("this is:",i)
# mytuple[0]="goodbye"  
# print(mytuple)


setx={1,2,2,3,4,5,5,6}
print(setx)
setx.add(10)

print(setx)
sety={5,6,7,8,9,10,10,2,3}

print(setx.difference(sety))

print(setx.symmetric_difference(sety))

setz={"red","yellow","blue"}
seta={"red","green","pink"}

print(setz.intersection(seta))

print(setz.union(seta))