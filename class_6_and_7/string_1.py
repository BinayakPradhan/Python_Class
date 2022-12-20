# # String is extremely important topic


# #doc string (function's documentation)
# """wfjisdufnsfdsufnsidu
#      kjgerkj"""  #can be used to comment

# # 1
# my_string = "Hello World"
# print(my_string[4])          #fourth character i.e. Hello ko 'o' print hunchha
# print(my_string[-1])       #last character
# print("World" in my_string)    #sentence bhako word bhaye 'True' natra 'False' dekhauchha
# print('e' in my_string) #for character
# #i)
# a = "Hello World"
# print(a in my_string)          #gives 'True'

# #2
# next_string = '''this is a multi line comment'''  #prints what's in ''' '''
# print(next_string)

# #3
# my_string1 = '''Used to write "quotation".''' #"  " yo lyauna esari string lekhne
# print(my_string1)

# #4
# my_string6 = "Hello, Good Morning to you all."
# for i in my_string6:
#      #print(i)   #individually each letter print garchha
#      if i == "o":
#         i = i.upper()
#      print(i)        #sentence ma bhako every 'o' lai uppercase ma langera print garchha
      
# #5 (String Slicing)
# my_string3 = "Have a great day"
# print(my_string3[:-1])      #suru bata print garera end samma jau except last character
# print(my_string3[::-1])     #reverse way ma sab print garcha 

# #index (first jun position ma chha tyo matra dinchha, aru same character matlab gardaina)
# print(my_string3.index("H"))
# print(my_string3.index("Have"))   #'H' matra khojchha esma
# print(my_string3.index(" "))

# next_eg = "Hello from our SEC fam"
# print(next_eg.index("o"))       #'Hello' ko o
# print(next_eg.index("our"))     #'our' ko o

# #Uppercasing
# name = "Binayak Pradhan"
# print(name.upper())
# print(name.lower())   #prints 'binayak pradhan'

# #Lowercasing
# upper_name = 'BINAYAK PRADHAN'    #"BINAYAK PRADHAN" gareni hunchha
# print(upper_name.lower())

# #Capitalize 
# name1 = "binayak pradhan"
# print(name1.capitalize())  #string ko sabse agadiko letter lai capital garchha

# #Title
# name2 = "sexy boy"
# print(name2.title())  #each word ko 1st letter lai capital garchha


# #Concatenation of String
# print(name1 + name2)   #prints 'binayak pradhangood boy'
# print(name1 +" "+name2)  #prints 'binayak pradhan good boy' , space halna

# # Split 
# split_string = "Hi Hope-you are nice"
# print(split_string.split(" "))  #every space aauda list banaucha
# print(split_string.split("-"))     # prints ['Hi Hope', 'you are nice']

# # join
# join_string = "Hello World from our class"
# print(join_string.split("o"))       #prints -> ['Hell', ' W', 'rld fr', 'm ', 'ur class']
# o_nabhako_list = join_string.split("o")
# print("o".join(o_nabhako_list))    #prints-> Hello World from our class; every list pachadi 'o' jodchha

# print(" ".join(['I','am','studying.']))     #afai list dinani milchha
# print("+".join(str(['I','am','studying.'])))    #pratek [,'space pachi + halchha
# print("---".join(["Until","we","find","a","way",str(123)]))     

# #Strip (unnecessary white spaces lai hataucha)
# my_stringS = "             Hello World              "
# print(my_stringS.strip())        #prints--> Hello World

# #Formatting
# a = "Ram Bahadur"
# #Method I
# b = f"My name is {a}."
# print(b)
# #Method II
# c = "My name is {0},I live in {1},My age is {2}".format(a, '''"Dhumbarhai"''',"20")
# print(c)        #prints -> My name is Ram Bahadur,I live in "Dhumbarhai",My age is 20

# #Replace
# s = "Hello Universe"
# s = s.replace("e","o")   #replaces every e with o, can be words too
# print(s)                  #prints -> Hollo Univorso

##Count (printing how many ab in string)
#my_string2 = "aaabcdefaaaabababababaababaabaabbba"
# print(my_string2.count("ab"))    #prints-> 10
# print(my_string2.count("aba"))  #prints-> 5

#Enumerate
my_es = "Hi and hello and bye hehe"
enu_list = my_es.split(" ")
# print(enu_list)
# for index,item in enumerate(enu_list):
#     print(index,item)

for index,item in enumerate(enu_list):     #jaile agadi ko le index ani pachadi ko le item ho
    if index % 2 == 0:
        enu_list[index] = item.upper()
print(enu_list)




