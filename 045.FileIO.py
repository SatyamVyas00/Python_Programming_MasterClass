# jabber = open("FileIO\Readsample.txt",'r')
# for line in jabber:
#     if "dog" in line.lower():
#         print(line,end='')
# jabber.close()

# with open("FileIO\Readsample.txt",'r') as jabber:
#     for line in jabber:
#         if "JUM" in line.upper():
#             print(line,end='')

# with open("FileIO\Readsample.txt",'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line,end='')
#         line = jabber.readline()

# with open("FileIO\Readsample.txt",'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines:
#     print(line,end='')

with open("FileIO\Readsample.txt",'r') as jabber:
    lines = jabber.readlines()
print(lines)
for line in lines[::-1]:
    print(line,end='')
print("*"*50)
with open("FileIO\Readsample.txt",'r') as jabber:
    lines = jabber.read()
for line in lines[::-1]:
    print(line,end='')