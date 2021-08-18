shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

#continue
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy "+item)

print("*"*50)
#break
item_to_find = "spam"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at=index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

print("*"*50)
#while loop
chosen_item = None
while chosen_item not in shopping_list:
    chosen_item = input("please input a item from shopping list to buy ")
    if chosen_item.casefold() == "quit":
        print("Exiting...")
        break

print("Let's Buy {}".format(chosen_item))

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break