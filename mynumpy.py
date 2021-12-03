def matrixMultMatrix(A, B):
    _checkIsMatrixAndMatrixOfNumbers(A, "A")
    _checkIsMatrixAndMatrixOfNumbers(B, "B")

    l, mA = _getMatrixSize(A)
    mB, n = _getMatrixSize(B)

    if mA != mB:
        raise ValueError(f"Matrices has wrong size A({l} x {mA}) and B({mB} x {n})")

    C = []

    for i in range(l):
        newRowC = []
        for j in range(n):
            newValueC = 0
            for r in range(mA):
                newValueC += A[i][r] * B[r][j]
            newRowC.append(newValueC)
        C.append(newRowC)
    
    return C

def matrixMultVector(A, B):
    _checkIsMatrixAndMatrixOfNumbers(A, "A")
    _checkIsVectorAndVectorOfNumbers(B, "B")
    
    m, nA = _getMatrixSize(A)
    nB = len(B)
    
    if nA != nB:
        raise ValueError(f"Matrix or vector has wrong size A({m} x {nA}) and B({nB})")
    
    C = []

    for i in range(m):
        newValueC = 0
        for j in range(nA):
            newValueC += A[i][j] * B[j]
        C.append(newValueC)

    return C

def vectorMultVector(A, B):
    _checkIsVectorAndVectorOfNumbers(A, "A")
    _checkIsVectorAndVectorOfNumbers(B, "B")

    nA = len(A)
    nB = len(B)

    if nA != nB:
        raise ValueError(f"Vectors has different size A({nA}) and B({nB})")
        
    C = 0

    for i in range(nA):
        C += A[i] * B[i]

    return C

def _checkIsMatrixAndMatrixOfNumbers(A, matrixName):
    if(not type(A) == list or not all(type(row) == list for row in A)):
        raise TypeError(f"{matrixName} is not matrix")

    if(not all(_allElemetsInVectorIsNumbers(row) for row in A)):
        raise TypeError(f"{matrixName} is not matrix of numbers")

def _checkIsVectorAndVectorOfNumbers(A, vectorName):
    if(not type(A) == list):
        raise TypeError(f"{vectorName} is not vector")

    if(not _allElemetsInVectorIsNumbers(A)):
        raise TypeError(f"{vectorName} is not vector of numbers")

def _allElemetsInVectorIsNumbers(A):
    return all(type(element) == int or type(element) == float for element in A)

def _getMatrixSize(A):
    m = len(A)
    n = []

    for row in A:
        n.append(len(row))

    uniqueN = list(set(n))

    if(len(uniqueN) != 1):
        raise ValueError("You should use square matrix")

    if(uniqueN[0] == 0):
        raise ValueError("All matrix rows are empty")
    
    return [m, uniqueN[0]]

