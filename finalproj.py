A = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00], [0.3025, 0.36, 0.4225, 0.49, 0.5625, 0.64, 0.7225, 0.81, 0.9025, 1], [0.166375, 0.216, 0.274625, 0.343, 0.421875, 0.512, 0.614125, 0.729, 0.857375, 1]]

y = [1.102, 1.099, 1.017, 1.111, 1.117, 1.152, 1.265, 1.380, 1.575, 1.857]

#norm(vector) takes a vector and returns the 2nd norm
def norm(vector):
  '''this function takes a vector as its argument. It squares each element in the vector and then sqaure roots the sum of the squares.
  '''
  total = 0 #this is before the for statement for adding purposes.
  for i in range(len(vector)):
    total += vector[i] ** 2 #takes each element of vector and squares them.
  total = total**(1/2)#takes the sqaure root of the sum found above.
  return total
#this function finds the normalized vector.
def normalize(vector):
  '''
  This function takes the vector as its argument and multiplies it by the (1/norm(vector))
  '''
  new = [] #new bracket
  for i in range(len(vector)):
    total = 0 #after for statement as adding is not involved.
    total += vector[i] * (1 / norm(vector))
    #divides the vector by the 2nd norm found above.
    new.append(total)
  return new

#this function takes the dot product of two vectors.
def dot(vector01, vector02):
  '''
  This function takes two vectors and multiplies each element together and then adds them.
  '''
  if len(vector01) != len(vector02):
    print('invalid input')
    for i in range(len(vector01)):
      if (type(vector01[i]) != int) and (type(vector01[i]) != float) and (type(vector01[i] != complex)):
        print('invalid input')
  total = 0 #before the for statement so it performs addition.
  for i in range(len(vector01)):
    total += vector01[i] * vector02[i] #multiplies each element of the vectors by each other and then adds them all together to get a scalar.
  return total
#ScaVecMulti takes a scalar and a vector and multiplies it together.
def ScaVecMulti(scalar, vector):
  '''
  this function takes a scalar and a vector as its arguments and returns the product of the two. It takes each element of the vector and multiplies it by the scalar to get the total. It then is put into the new brackets.
  '''
  new = [] #will be brackets for answer
  for i in range(len(vector)):
    total = 0
    total += vector[i] * scalar #takes each element of the vector and multiplies it by the scalar.
    new.append(total)#puts the total inside the brackets.
  return new
#VecSub takes two vectors and subtracts the first from the second.
def VecSub(vector01, vector02):
  '''
  This function takes two vectors as its arguments and subtracts each element in order and then returns a new vector.
  '''
  if len(vector01) != len(vector02):
    print('invalid input')
    return None
    for i in range(len(vector01)):
      if (type(vector01[i]) != int) and (type(vector01[i]) != float) and (type(vector01[i] != complex)):
        print('invalid input')
  new = [] #will be new brackets for answer.
  for i in range(len(vector01)):
    total = 0 #after for statement to reset.
    total += vector01[i] - vector02[i]#subtracts elements individually from vector02 from vector01.
    new.append(total) #adds the total into the brackets.
  return new

#GrSc takes the Gram-Schmidt algorithm and returns Q and R.
def GrSc(A):
  '''
  this functions takes in the matrix A as the argument. It takes the functions above of norm, normalize, dot, scalarvectormultiplication and vector subtraction and returns the QR factorization.
  '''
  n = len(A) #row
  m = len(A[0]) #columns
  Q = [[0] * m for i in range(n)] #zeromatrix
  R = [[0] * n for i in range(n)] #zero matrix
  v = [[0] * m for i in range(n)] #zero matrix
  if len(A) != len(v):
    print('invalid input')
  for i in range(n):
    v[i] = A[i] #the vector[i] is the individual vectors of A.
  for i in range(n):
    R[i][i] = norm(v[i]) #takes the norm function above
    Q[i] = normalize(v[i]) #takes the normalize function above
    for j in range(i + 1, n):
      R[i][j] = dot(Q[i],v[j]) #takes the norm vector and the vectors and multiplies them together, and then adds them to make the scalar.
      temp = ScaVecMulti(R[i][j], Q[i]) #takes the dot product and the normalize vector and multiplies them together.
      v[j] = VecSub(v[j],temp) #subtracts the ScaVecMulti from the vectors.
  return [Q, R]
QR = GrSc(A) #defines QR for the independent Q and R.

Q = QR[0] #defines Q
R = QR[1] #defines R

'''
def trans(Q):
  m = len(Q)
  n = len(Q[0])
  new = [[0] * m for i in range(n)]
  for i in range(len(Q)):
    for j in range(len(Q[0])):
      new[j][i] = Q[i][j]
  return new
QT = trans(Q)
'''
#transmatvecMulti multiplies the matrix Q and vector y together.
def transmatvecMulti(Q, y):
  '''
  This function takes the matrix Q and the vector y as its arguments and multiplies them together. We wanted the transform of Q, but I used the function for matrix vector multiplication that uses a matrix made of rows, instead of columns. So Q could be used, since it is made of column vectors.
  '''
  new = [] #used for the answer.
  for i in range(len(Q)):
    product = 0 #since we want no addition this appears after the for statement.
    for j in range(len(y)):
      product += Q[i][j] * y[j]
    new.append(product) #appends product inside the new brackets.
  return new
b = transmatvecMulti(Q, y) #defining b
#backsub is finding the unknown starting with the end.

def backsub(R, b):
  '''
  this function takes the the vector R and the vector b and returns the unknowns c. Being called backwards substitution, it starts with the last unknown, solves it, and then uses it to solve for the next unknown.
  '''
  a = len(b) - 1
  c = [0] * len(b)
  c[a] = b[a] / R[a][a]
  for i in range(a, 0, -1):
    c[i] = b[i]
    for j in range(i +1, a):
      c[i] = c[i] - c[j]*R[j][i]
      c[i] = c[i] / R[i][i]
  return c
print(A)
print(GrSc(A))
print(backsub(R, b))
