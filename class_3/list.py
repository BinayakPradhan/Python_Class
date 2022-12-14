
#List
my_list = [1,2,3,"Hello",3.5] #jun datatype ko list banaunani milchha
print(my_list)
#my_list [list_position] 
#my_list [-1]      , last ko value dincha
#my_list [-2]   , last ko bhanda left ko  value dincha
#my_list [list_position] = list    , kunai position ko value change garchha
#len (my_list)   , list ko length dincha
#my_list.append("world")   , last ma gara rakhdinchha one at a time matra
#my_list.append(["world",4,2.5])   , list bhitra arko list banauna milchha
#my_list.pop()  ,last ko list ma bhako element pop hunchha
#my_list.pop(list_ko_position)  , tyo position ko element delete hunchha
#my_list.count(listmabhako_kei_element)  , tyo element purai list bhari kati chha count dinchha
#my_list.insert(list_ko_position,element)  , tyo positon ma element add huncha
#max (my_list)   , same datatype chha bhane max size dekhaucha list ko

##class_4(slicing)
#ending point bhanda ek agadi samma matra linchha, afulai include gardaina ,eg:my_list[0:10:2]
#last samma jada chai(or kei value nalekhda), aafulai ni include garchha , eg:my_list[0::2]
#my_list[::-1]   , inverse dincha
#my_list[-1:-7/7:-1]  , reverse garchha, starting point: -1, ending point chai ki -7 kita 7 dida jasari deko tei bata count garne
#my_list[1:2:2] ,starting point: ending point: difference  
#my_list[::2]  , starting, ending narakhi difference line
