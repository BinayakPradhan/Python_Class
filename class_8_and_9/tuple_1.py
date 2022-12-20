'''List is mutable(can be changed)
    but tuple is non-mutable(cannot be changed),tuple is used while saving password, or kunai
    theme select garda change huna nadina
    '''

my_tuple = (10,20,30,'a','hello',"world")
# print(my_tuple)
# print(len (my_tuple))
# print(my_tuple [2])    #indexing hunchha

# #indexing huncha bhane loop chalauna milchha
# for i in my_tuple:
#     print(i)

#pop,insert,append,delete(purai tuple delete garna milcha but element mildaina): these doesn't work on tuple
#tara use garnai paryo bhane esari garne
my_list = list(my_tuple)    #converting tuple to list
my_list.append(1234)        #print(my_list.append(1234)); yo garda return 'None' garcha but append chai garcha
print(my_list)

tup = tuple(my_list)        #converting list to tuple
print(tup)
print(tup.count('hello')) #kunai pani element kati watacha bhanera herna
