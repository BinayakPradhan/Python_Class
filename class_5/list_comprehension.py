#list comprehension is basically used for loops, it is advaced form of python


my_es = "Hi and hello and bye hehe"
enu_list = my_es.split(" ")
# print(enu_list)
# for index,item in enumerate(enu_list):
#     print(index,item)

#normal way of using enumeration
# for index,item in enumerate(enu_list):     #jaile agadi ko le index ani pachadi ko le item ho
#     if index % 2 == 0:
#         enu_list[index] = item.upper()
# print(enu_list)

#Using list comprehension
b = [item.upper() for item in enu_list if enu_list.index(item) % 2 == 0]
#k garne ho,loop,condition
print(b)