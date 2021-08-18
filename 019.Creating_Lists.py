empty_lists = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("4856379120")
print(digits)

#copy a list
#more_numbers = list(numbers)
#more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(more_numbers is numbers)

computer_parts = ["computer","monitor","keyboard","mouse","mouse mat"]
print(computer_parts)
#replacing
computer_parts[3] = "trackpad"
print(computer_parts)

#replacing slices
computer_parts[3:] = ["trackball"]
print(computer_parts)

#deleting items
data = [1,2,3,4,5,6,7,8,9,10]
del data[0:2]
print(data)
del data[5:]
print(data)

data=[1,4,5,100,105,110,120,130,140,150,170,199,200,201,210,250,299]
print(data)
min_valid = 100
max_valid = 200

#process the low value in list
stop = 0

for index,value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

#procezs the high value in list
start = 0

for index in range(len(data) -1,-1,-1):
    #print(index)
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)
del data[start:]
print(data)

#reverse reomving of data
print()
data = [104,101,4,105,308,103,5,107,100,306,106,102,108]
# for index in range(len(data)-1,-1,-1):
#     if data[index]<min_valid or data[index]>max_valid:
#         print(index,data)
#         del data[index]
# print(data)
top_index = len(data)-1
for index,value in enumerate(reversed(data)):
    if value<min_valid or value>max_valid:
        print(top_index-index,value)
        del data[top_index-index]

print(data)