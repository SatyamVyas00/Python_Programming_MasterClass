# cities = ["Rishikesh","Haridwar","Dehradun","Nainital"]

# with open("FileIO\Writesample.txt",'w') as city_file:
#     for city in cities:
#         print(city,file=city_file)

# cities = []
# with open("FileIO\Writesample.txt",'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

# details = "Satyam Vyas","DITU",(
#     (1,"BTech"),(2,"CSE"),(3,"ML"))
with open("FileIO\Writesample.txt",'a') as details_file:
    for i in range(2,13):
        for j in range(1,13):
            print("{1:>2} times {0} is {2}".format(i,j,i*j),file=details_file)
        print("*"*50,file=details_file)

# with open("FileIO\Writesample.txt",'r') as details_file:
#      content = details_file.readline()
#
# details = eval(content)
# print(details)
# name,college,branch_details = details
# print(name)
# print(college)