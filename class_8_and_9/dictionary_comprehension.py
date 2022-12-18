

# # # #Dictionary Comprehension

# # price_of_item = {
# #             'apple': 120,
# #             'banana': 330,
# #             'orange': 210,
# #             'pear': 210,
# #             'grape': 410,
# #             'pineapple': 560,
# #             'strawberry': 770,
# #             'watermelon': 660
# # }
# #dicrtionary comprehension use garera key ma 's ra value ma value plus *13 of value gareko
# # # # item_dict = {f"{key}'s" : value + value * 0.13 for key,value in price_of_item.items()}

# # # # print(item_dict)

# # # item_dict1 = {f"{key} + Doubled" : value + value for key,value in price_of_item.items()}
# # # print(item_dict1)

# # item_dict2 = {key : value + value * 0.13 for key,value in price_of_item.items()}
# # print(item_dict2)

# #Using FUNCTION using Default Arguments
# price_of_item = {
#             'apple': 120,
#             'banana': 330,
#             'orange': 210,
#             'pear': 210,
#             'grape': 410,
#             'pineapple': 560,
#             'strawberry': 770,
#             'watermelon': 660
# }


# def get_price_of_items(item, tax_rate = 0.13):
#         return {key : value + value * tax_rate for key,value in item.items()}

# print(get_price_of_items(price_of_item))                                #VAT added price

# print(get_price_of_items(price_of_item, 0.15))                          #15% VAT added wala chai


#Create a function which takes x and returns it's functional value:
# n = input("Enter a number: ")
# x = float(n)
# def get_func(x):
#     return {x*x + 5*x + 1}

# print("The value is: ",get_func(x))



# #Implicitly called Functions
# f = lambda x : x**2 + 5*x + 1  #LAMBDA  used #chalcha and memory end ni yei huncha chalesi #No effects in memory
# print(f(1))

# #Use in string
# g = lambda name : name + " hero"
# print(g("Super"))

# #Passing two arguments
# h = lambda x,y : 3 * x * x + 5 * x * y + 5
# print("The value is: ",h(1,2))




