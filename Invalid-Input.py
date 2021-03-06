#Return TwoNorm
def twoNorm(vector):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the 2-norm
  if inputStatus == True:
    result = 0
# This for loop will compute the sum of the squares of the elements of the vector. 
    for i in range(len(vector)):
      result = result + (vector[i]**2)
    result = result**(1/2)
    return result

#Return ScalarVector
def scalarVecMulti(scalar,vector):
  '''
  This function takes in a scalar and vector as its inputs. The scalar is multiplied to each element of the vector. The result is then placed into the new vector, x.
  '''
  inputStatus=True
  x = []
  #This for loop takes the multiplication of each element of the vector and the scalar and appends the product to new vector x.
  for i in range(len(vector)):
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the product of the scalar and vector
  if inputStatus == True:
    x.append(vector[i]*scalar)
  return x

#Returns Dot Product
def dot(vector01,vector02):
  '''
  This function takes in two vectors as its inputs and produces the resulting dot product. The dot product is computed by multiplying corresponding elements of each vector. Once the multiplication is complete, the numbers are then added together, resulting in an integer.
  '''
  n = len(vector01)
  p = len(vector02)
  inputStatus=True
  #The following line is checking that the length of both vectors is equal to ensure that multiplication is possible
  if n==p:
    x=0
    #This for loop is taking each  corresponding element, multiplying them, and adding them together for the final integer.
    for i in range(len(vector01)):  
      if ((type(vector01[i] and vector02[i]) != int) and (type(vector01[i] and vector02[i]) != float) and (type(vector01[i] and vector02[i]) !=complex)):
        inputStatus = False
        print("Invalid Input")
  # If the input is valid the function continues to compute the dot product
  if inputStatus == True:
      x += vector01[i]*vector02[i]
      return x 
  else:
    print("invalid input")
    return None

def vecSubtract(vector03,vector04):
  '''
  The function vecSubtract takes in two vectors and returns the difference of the two. After the difference of each pair of corresponding elements has been computed, it then takes the number and puts it in a new list to return the updated vector.
  '''
  n = len(vector03)
  p = len(vector04)
  inputStatus=True
  if n==p:
    x=[]
    #this for loop subtracts the two elements and then appends the difference into the new vector, x
    for i in range(len(vector03)):
      if ((type(vector03[i] and vector04[i]) != int) and (type(vector03[i] and vector04[i]) != float) and (type(vector03[i] and vector04[i]) !=complex)):
        inputStatus = False
        print("Invalid Input")
  # If the input is valid the function continues to compute the dot product
  if inputStatus == True:
    x.append(vector03[i]-vector04[i])
    return x
  else:
    print("invalid input")
    return None

def normalize(vector07):
  '''
  This function takes a vector and calculates the normalized vector.The norm of vector has been calculated in question 4 and is being referenced for this question. Then, the normalized vector is calculated by dividing each element in the specified vector by the norm using the infinity norm.  
  '''
  norm = twoNorm(vector07)
  x = []
  #This for loop divides each element of vector07 and divides it by the norm of vector07. It then appends the number to the new normalized vector, x.
  for i in range(len(vector07)):
    x.append(vector07[i]/norm)
  return (x)

def QR_factor(matrix):
  '''
  This function computes the Modified Gran-Schmidt of the given matrix. It utilizes the two norm to then normalize the vectors in matrix A, which becomes the Q vector. We then use the dot product function on the normalized vector and the second vector in the matrix. The last function we use is vector subtraction, which calculates each normalized vector in the Q matrix. The final result is the factorized matrix A into matrix Q and an upper triangular matrix R.
  '''
  #The following checks make sure that the input is a valid matrix.
  if type(matrix) !=list:
    print ("invalid input")
    return None
  if len(matrix)==0:
    print ("invalid input")
    return None
  for i in range(len(matrix)):
    if type(matrix[i]) !=list:
      print ("invalid input")
      return None
    if len(matrix[i])==0:
      print ("invalid input")
      return None
    for j in range(len(matrix)):
      if type(matrix[i][j]) !=int and type(matrix[i][j]) != float and type(matrix[i][j]) !=complex:
        print ("invalid input")
        return None
  #We have defined these lengths as variables  to use throughout the function
  m=len(matrix[0])
  n=len(matrix)
  V=matrix
  R=[[0]*n for i in range(n)]
  Q=[[0]*m for i in range(n)]
  for i in range(n):
    #This for loop calculates the norm of the matrix and normalize the first vector
    R[i][i]=twoNorm(V[i])
    Q[i]=normalize(V[i])
    #This for loop normalizes the rest of the vectors in the matrix by the use of the dot product function, scalar multiplication, and vector subtraction.
    for j in range(i+1,n):
      R[j][i]=dot(Q[i],V[j])
      temp=scalarVecMulti(R[j][i],Q[i])
      V[j]=vecSubtract(V[j],temp)
  return [Q,R]
matrix=[[1,0,1],[2,1,0]]
print(QR_factor(matrix))
