##4 2-dimensional Matrix
# mat_A = [[1,2,3],[4,5,6],[7,8,9]]
# mat_B = [[2,4,6],[8,10,12],[14,16,18]]
# print(mat_A)
# print(mat_A [0][-2])  #mat_A ko [0 index ko list] [0 index ma bhako list ko -2 position]


# #Adding two matrix

# mat_A = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# mat_B = [[1,1,1],
#          [1,1,1],
#          [1,1,1]]
# mat_add = [[0,0,0],
#            [0,0,0],
#            [0,0,0]]
# for i in range (len(mat_A)):                        #   row count ko lagi
#     for j in range (len(mat_A[0])):                 #   column count ko lagi 
#         mat_add[i][j] = mat_A[i][j] + mat_B[i][j]
# print(mat_add)


#Multiplication of two matrix

mat_A = [[1,2],
         [4,5]]
mat_B = [[1,1],
         [1,1]]
mat_mult = [[0,0],
            [0,0]]
for i in range(len(mat_A)):                        #  A row count ko lagi
    for j in range(len(mat_A[0])):                 #   A column count ko lagi 
        mat_mult[i][j] = 0
        for k in range (len(mat_B)):                #   B row count ko lagi or value adjust ko lagi rakheko A/B j rakhdani hunchha
             mat_mult[i][j] += mat_A[i][k] * mat_B[k][j]
print(mat_mult)