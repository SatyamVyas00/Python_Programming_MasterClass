def cpy(dict :dict ) -> dict:
    new_dict = {}
    for keys in dict.keys():
        if str(type(dict[keys])) == "<class 'list'>":
            new_dict[keys]=dict[keys].copy()
        elif str(type(dict[keys])) == "<class 'dict'>":
            new_dict[keys]=cpy(dict[keys])
        else:
            new_dict[keys]=dict[keys]
    return new_dict

lion_list = ["scary","big","cat"]
elephant_list = ["big","grey","wrinkled"]
teddy_list = ["cuddly","stuffed"]

dict1 = {
    "lion" : "lion_list",
    "elephant" : {1:"big",2:"grey",3:"wrinkled"},
    "teddy" : teddy_list,
}

dict2 =  cpy(dict1)
teddy_list.append("toy")
dict2["elephant"][3] = "old"
print(dict1)
print(dict2)
print()
print(id(dict1["teddy"]),dict1["teddy"])
print(id(dict2["teddy"]),dict2["teddy"])