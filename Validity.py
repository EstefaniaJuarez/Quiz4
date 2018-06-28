def QR_factor(matrix):
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
