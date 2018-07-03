def norm(vector):
  total = 0
  for i in range(len(vector)):
    total += vector[i] ** 2
  total = total**(1/2)
  return total

def normalize(vector):
  new = []
  for i in range(len(vector)):
    total = 0
    total += vector[i] * (1 / norm(vector))
    new.append(total)
  return new

def dot(vector01, vector02):
  total = 0
  for i in range(len(vector01)):
    total += vector01[i] * vector02[i]
  return total

def ScaVecMulti(scalar, vector):
  new = []
  for i in range(len(vector)):
    total = 0
    total += vector[i] * scalar
    new.append(total)
  return new

def VecSub(vector01, vector02):
  new = []
  for i in range(len(vector01)):
    total = 0
    total += vector01[i] - vector02[i]
    new.append(total)
  return new

A = [[2, 1, 2], [1, -1, 1]]

def GrSc(A):
  n = len(A)
  m = len(A[0])
  Q = [[0] * m for i in range(n)]
  R = [[0] * n for i in range(n)]
  v = [[0] * m for i in range(n)]

  for i in range(n):
    v[i] = A[i]
  for i in range(n):
    R[i][i] = norm(v[i])
    Q[i] = normalize(v[i])
    for j in range(i + 1, n):
      R[i][j] = dot(Q[i],v[j])
      temp = ScaVecMulti(R[i][j], Q[i])
      v[j] = VecSub(v[j],temp)
  return [Q, R]

output = GrSc(A)
print(output[0])
print(output[1])
