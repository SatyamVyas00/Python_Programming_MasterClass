import pickle

# details = ("Satyam Vyas",
#           "DITU",
#           ((1,"BTech"),
#            (2,"CSE"),
#            (3,"ML")))
# with open("FileIO\Pickling.pickle",'wb') as pickle_file:
#     pickle.dump(details,pickle_file)

# with open("FileIO\Pickling.pickle",'rb') as load_pickle_file:
#     detail = pickle.load(load_pickle_file)
# print(detail)
# name,college,course = detail
# print(name)
# print(college)
# print(course)

details = ("Satyam Vyas",
          "DITU",
          ((1,"BTech"),
           (2,"CSE"),
           (3,"ML")))
even = list(range(0,10,2))
odd = list(range(1,10,2))
with open("FileIO\Pickling.pickle",'wb') as pickle_file:
    pickle.dump(details,pickle_file,protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even,pickle_file,protocol=0)
    pickle.dump(odd,pickle_file,protocol=pickle.DEFAULT_PROTOCOL)
    pickle .dump(2998302,pickle_file)

with open("FileIO\Pickling.pickle",'rb') as load_pickle_file:
    details_list = pickle.load(load_pickle_file)
    even_list =  pickle.load(load_pickle_file)
    odd_list = pickle.load(load_pickle_file)
    x = pickle.load(load_pickle_file)
print(details_list)
print(even_list)
print(odd_list)
print(x)
name,college,course = details_list
print(name)
print(college)
print(course)