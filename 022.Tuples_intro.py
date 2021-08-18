#Tupples are immutable
#all lists operation can be performed on tupples
#tupples are printed between ( )
t=("a","b","c")
print(t)

name = "Satyam"
age = 20
print(name,age,"Python",2021)
print((name,age,"Python",2021))

hello = "Welcome to","Year",2021
print(hello)
print(hello[0])
print(hello[1])
print(hello[2])


hello2 = list(hello)
print(hello2)
hello2[0]="This is"
print(hello2)

print()
#unpacking a tupple
a = b = c = d = e = f = 42
print(c)

x,y,z=1,2,76
print(x)
print(y)
print(z)

print("unpacking a tupple")

data = 1,2,76 # data represent a tupple
print(data)
x,y,z=data
print(x)
print(y)
print(z)

print("unpacking a list")

data_list = [12,13,14]
# data_list.append(15) #error
p,q,r=data_list
print(p)
print(q)
print(r)

for t in enumerate("abcdefgh"):
    print(t)