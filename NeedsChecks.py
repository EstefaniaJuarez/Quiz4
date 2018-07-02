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
    if ((type(vector01[i] and vector02[i]) != int) and (type(vector01[i] and vector02[i]) != float) and (type(vector01[i and vector02[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the dot product
  if inputStatus == True:
      x += vector01[i]*vector02[i]
    return x 
  else:
    print("invalid input")
    return None

def vecSubtract(vector,vector):
  '''
  The function vecSubtract takes in two vectors and returns the difference of the two. After the difference of each pair of corresponding elements has been computed, it then takes the number and puts it in a new list to return the updated vector.
  '''
  n = len(vector)
  p = len(vector)
  if n==p:
    x=[]
    #this for loop subtracts the two elements and then appends the difference into the new vector, x
    for i in range(len(vector)):
      x.append(vector[i]-vector[i])
    return x
  else:
    print("invalid input")
    return None

def QR_factor(matrix):
  A=[0]
  Q=[]
  R=[]
  if type(matrix) !=list:
    print ("invalid input")
    return None
  if len(matrix)==0:
    print ("invalid input")
    return None
  x=0
  for i in range(len(matrix)):
    if type(matrix[i]) !=list:
      print ("invalid input")
      return None
    if len(matrix[i])==0:
      print ("invalid input")
      return None
    for j in range(len(matrix[i])):
      if type(matrix[i][j]) !=int:
        print ("invalid input")
        return None
      if type(matrix[i][j]) !=float:
        print ("invalid input")
        return None
      if type(matrix[i][j]) !=complex:
        print ("invalid input")
        return None
