name = "Satyam"
age = 20

print(name,age,"Python",2020)

#print(*object,sep=' ',end='\n',file=sys.stdout,fllush=False)   print function
print(name,age,"Python",2020,sep=", ")

#.join function
flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

print(",".join(flowers))
#OR
seperator = " | "
output = seperator.join(flowers)
print(output)

#.split
pangram = """The quick brown
fox jump\tover
the lazy dog"""
words=pangram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))
print()
generated_list = ['9',' ',
                  '2','2','3',' ',
                  '3','7','2',' ',
                  '0','3','6',' ',
                  '8','5','4',' ',
                  '7','7','5',' ',
                  '8','0','7']
values = "".join(generated_list)
print(values)
print()
values_list = values.split()
print(values_list)
print()
int_list = []
for val in values_list:
    int_list.append(int(val))

print(int_list)