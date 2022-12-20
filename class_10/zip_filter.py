
# # #MAP (function name, ani tyo function ko argument pathaune)
# #     #i) same size ko mile jastai different length ko ni milcha
# #     #ii) Jati ota ni list pass garna milcha

# # my_list = [1,2,3,4,5,6,7,8,9,10]
# # next_list = my_list[::-1]
# # my_tuple = (1,1,1,1,1,1,1,1,1,1) #tuple ni milcha jodna


# # #function definition
# # def sum_of_num(a,b,c):
# #     return a + b + c


# # #passing arguments in functions
# # print(sum_of_num(1,2,3))

# # #print(sum) garda whole lai nai object consider garera address dincha
# # sum = map(sum_of_num, my_list, next_list, my_tuple)
# # print(list(sum))


# #Zip (list ko index milne, elements haru lai tuple banaucha ani as a whole lai chai list banaucha)
#     #i) farak length ko zip garda sab se choto length lai priority dera zipped list banaucha sabse kaam length ko list




# lis = [2,2,2,2,2,2,2,2,2]
# lis1 = [1,2,3,4,5,6,7,8,9,10]
# lisinv = lis1[::-1]
# mr_tuple1 = (7,7,7,7,7)
# short_list = [1,2,3,4]

# #zip in list
# zipped_list = list(zip(lis, lis1, lisinv))        #list lekhna birse object banaucha address dincha

# print(zipped_list)

# #zip in tuple
# zipped_tuple = tuple(zip(lisinv, mr_tuple1, short_list))
# print(zipped_tuple)


# #Use "MAP" & "LAMBDA"

# l_list = list(filter(lambda x : x%2 == 0, lis1))
# print(l_list)

#*****************FILTER******************
#true is only printed

my_list1 = [1,2,3,4,5,6,7,8,9,10]
def check_even(num):
    if num%2 == 0:
        return True
    else:
        return False
NEW_LIST2 = list(filter(check_even, my_list1))
print(NEW_LIST2)

#using filter and lambda
NEW_LIST2 = list(filter(lambda x : x%2 ==0, my_list1))
print(NEW_LIST2)