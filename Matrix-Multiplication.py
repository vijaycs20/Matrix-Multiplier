n=int(input("Enter the order of the matrix (3) : "))
matrix1 = []
for i in range(n):
   row = list(map(int, input().split()))
   matrix1.append(row)
   
matrix2 = []
for i in range(n):
   row = list(map(int, input().split()))
   matrix2.append(row)   

output  = [[0,0,0],  
            [0,0,0],  
            [0,0,0]]  
  
for i in range(len(matrix1)):  
    for j in range(len(matrix2)):  
        output[i][j] = matrix1[i][j]  * matrix2[i][j]  
  
print("The product of Matrices is = ",output)  