'''key value pair save garna use hunchha'''

# dictionary_1 = {'a':104, 4:'four', 'c':None}   #key:value ->key int,float,string j rakhna ni payo
# # print(dictionary_1)

# # print(dictionary_1['a'])                 #key diyo bhane tesko value print garchha

# # print (len(dictionary_1))                   #gives dictionary_1 length



# # print(dictionary_1.values())             #prints values of dictionary --> dict_values([104, 'four', None])
# # print(type(dictionary_1.values()))      #dictionary_1.values() class ho bhanera dekhauchha

# # print(dictionary_1.keys())                 #prints keys of dictionary -->dict_keys(['a', 4, 'c'])
# # print(type(dictionary_1.keys()))          #(dictionary_1.keys()) class ho bhanera dekhauchha 

# # for key,value in dictionary_1.items():    #keys ra values dekhaucha 
# #     print(key)
# #     print(value)
# #     print(key,value)

# # for key in dictionary_1.keys():
# #     print(key)

# # for value in dictionary_1.values():
# #     print(value)

# my_listing = (1,2,3,4,5)                   #yo tuple ho najhukkine
# my_dict = {1:"one",2:"two"}
# print(my_dict)                             #printing a dictionary


# #to insert new key and values
# my_dict["three"] = 3        
# my_dict["title"] = "Superman"      
# my_dict[4] = "four"
# my_dict[5] = "five"         
# print(my_dict)



# print(my_dict.items())                     #prints--->dict_items([(1, 'one'), (2, 'two'), ('three', 3)])


# #to check whether there is required value in the key

# print(my_dict['title'] == 'Superman')                #True (key diyera check garne ho)
# print(my_dict[2] == 'hello')                #False  (value check gareko wrong bhako le false)


# #POP
# print(my_dict.pop(2))                       #2 bhanne key lai pop gareko
# print(my_dict.pop('title'))                 #title bhanne pop gareko, pop garda chai key diyo bhane value return garcha ani delete ni
# print(my_dict)                              #2 ra title bhanne key delete gare pachi ko print


# #popitem
# print(my_dict.popitem())                    #key:value sabse last ko delete gardincha popitem le
# print(my_dict)                              #last ko item delete bhaisake pachi ko print gareko ho

# #Update(updating values)
# my_dict.update({1:"Batman"})                #1 bhanne key ko value lai change gareko
# print(my_dict)                              #batman bhanne 1 ko value hali sake pachi ko print gareko

# print(my_dict.update({1:"Flash"}))          #esari garda chai hamro output ma None dekhaucha


# #Nested Dictionary

# my_dict["baby_dict"] = {7:'a', 8:'b', 'college':'sagarmatha'}
# print(my_dict)


#################            CLASSWORK               ########################

sagarmatha = {
        "Education Department": {
                "Computer Science": {
                        "HOD":"Bharat Bhatta", 
                        "no_of_students": 100
                },
                "Civil": {
                        "HOD":"Sudip Lamsal",
                        "no_of_students": 200
                }
        },
        "Admin Department": {
                "Accounts": {
                        "HOD":"Chaturbhuj Nepali",
                        "no_of_students": 50
                }
        }
}
print(sagarmatha)