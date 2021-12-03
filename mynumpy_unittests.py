import unittest
from mynumpy import matrixMultMatrix, matrixMultVector, vectorMultVector

class Test_ownnumpy(unittest.TestCase):
    def assertTestCasesError(self, methodToTest, testCases, errorType):
        for testCase in testCases:
            with self.subTest(i=testCase):
                with self.assertRaises(errorType) as error:
                    methodToTest(testCase["A"], testCase["B"])
                self.assertEqual(str(error.exception), testCase["expectedErrorMessage"])

    def assertTestCaseResult(self, methodToTest, testCases):
        for testCase in testCases:
            with self.subTest(i=testCase):
                C = methodToTest(testCase["A"], testCase["B"])
                self.assertEqual(C, testCase["expectedC"])

    def test_matrixMultMatrix_whenWrongArgumentType(self):
        testCases = [
            {"A": "Not matrix", "B": [[4], [5], [6]], "expectedErrorMessage": "A is not matrix"},
            {"A": [[1, 2, 3]], "B": "Not matrix", "expectedErrorMessage": "B is not matrix"},
            {"A": [""], "B":  [[4], [5], [6]], "expectedErrorMessage": "A is not matrix"},
            {"A": [[1, 2, 3]], "B": [[4], [5], ""], "expectedErrorMessage": "B is not matrix"},
            {"A": [[1, 2, ""]], "B": [[4], [5], [6]], "expectedErrorMessage": "A is not matrix of numbers"},
            {"A": [[1, 2, 3]], "B": [[4], [5], [""]], "expectedErrorMessage": "B is not matrix of numbers"}
        ]
        self.assertTestCasesError(matrixMultMatrix, testCases, TypeError)

    def test_matrixMultMatrix_whenMatrixWrongFormat(self):
        testCases = [
            {"A":  [[1, 2, 3], []], "B": [[4], [5], [6]], "expectedErrorMessage": "You should use square matrix"},
            {"A":  [[1, 2, 3]], "B": [[4, 2], [5], [6]], "expectedErrorMessage": "You should use square matrix"},
            {"A":  [[]], "B": [[4, 2], [5], [6]], "expectedErrorMessage": "All matrix rows are empty"},
            {"A":  [[1, 2, 3]], "B": [[], [], []], "expectedErrorMessage": "All matrix rows are empty"}
        ]
        self.assertTestCasesError(matrixMultMatrix, testCases, ValueError)

    def test_matrixMultMatrix_whenImpossibleToMultiplyMatrices(self):
        testCases = [
            {"A":  [[1, 2, 3], [2, 1, 1]], "B": [[4], [5]], "expectedErrorMessage": "Matrices has wrong size A(2 x 3) and B(2 x 1)"},
            {"A":  [[1, 2, 3, 4, 5]], "B": [[4], [5], [6]], "expectedErrorMessage": "Matrices has wrong size A(1 x 5) and B(3 x 1)"}
        ]
        self.assertTestCasesError(matrixMultMatrix, testCases, ValueError)

    def test_matrixMultMatrix_correctMatrices(self):
        testCases = [
            {"A": [[2, -3, 1], [5, 4, -2]], "B": [[-7, 5], [2, -1], [4, 3]], "expectedC": [[-16, 16], [-35, 15]]},
            {"A": [[1, 2, 3]],              "B": [[4], [5], [6]],            "expectedC": [[32]]},
            {"A": [[4], [5], [6]],          "B": [[1, 2, 3]],                "expectedC": [[4, 8, 12], [5, 10, 15], [6, 12, 18]]}]
        self.assertTestCaseResult(matrixMultMatrix, testCases)
    
    def test_matrixMultVector_whenWrongArgumentType(self):
        testCases = [
            {"A": "Not matrix", "B": [4, 5, 6], "expectedErrorMessage": "A is not matrix"},
            {"A": [""], "B":  [4, 5, 6], "expectedErrorMessage": "A is not matrix"},
            {"A": [[1, 2, 3]], "B": "Not vector", "expectedErrorMessage": "B is not vector"},
            {"A": [[1, 2, ""]], "B": [4, 5, 6], "expectedErrorMessage": "A is not matrix of numbers"},
            {"A": [[1, 2, 3]], "B": [4, 5, ""], "expectedErrorMessage": "B is not vector of numbers"}
        ]
        self.assertTestCasesError(matrixMultVector, testCases, TypeError)

    def test_matrixMultVector_whenMatrixWrongFormat(self):
        testCases = [
            {"A":  [[1, 2, 3], []], "B": [4, 5, 6], "expectedErrorMessage": "You should use square matrix"},
            {"A":  [[]], "B": [4, 5, 6], "expectedErrorMessage": "All matrix rows are empty"}
        ]
        self.assertTestCasesError(matrixMultVector, testCases, ValueError)

    def test_matrixMultVector_whenImpossibleToMultiplyMatrixAndVector(self):
        testCases = [
            {"A":  [[1, 2, 3], [2, 1, 1]], "B": [4, 5], "expectedErrorMessage": "Matrix or vector has wrong size A(2 x 3) and B(2)"},
            {"A":  [[1, 2, 3, 4, 5]], "B": [4, 5, 6], "expectedErrorMessage": "Matrix or vector has wrong size A(1 x 5) and B(3)"}
        ]
        self.assertTestCasesError(matrixMultVector, testCases, ValueError)

    def test_matrixMultVector_correctMatrices(self):
        testCases = [
            {"A": [[2, -3, 1], [5, 4, -2]], "B": [1, 6, 5], "expectedC": [-11, 19]},
            {"A": [[2, 10], [3, -7], [9, 5]], "B": [0, -4], "expectedC": [-40, 28, -20]}
        ]
        self.assertTestCaseResult(matrixMultVector, testCases)

    def test_vectorMultVector_whenWrongArgumentType(self):
        testCases = [
            {"A": "Not vector", "B": [4, 5, 6], "expectedErrorMessage": "A is not vector"},
            {"A": [1, 2, 3], "B": "Not vector", "expectedErrorMessage": "B is not vector"},
            {"A": [1, 2, ""], "B": [4, 5, 6], "expectedErrorMessage": "A is not vector of numbers"},
            {"A": [1, 2, 3], "B": [4, 5, ""], "expectedErrorMessage": "B is not vector of numbers"}
        ]
        self.assertTestCasesError(vectorMultVector, testCases, TypeError)

    def test_vectorMultVector_whenImpossibleToMultiplyMatrixAndVector(self):
        testCases = [
            {"A":  [1, 2, 3], "B": [4, 5], "expectedErrorMessage": "Vectors has different size A(3) and B(2)"},
            {"A":  [1, 2, 3, 4, 5], "B": [4, 5, 6], "expectedErrorMessage": "Vectors has different size A(5) and B(3)"}
        ]
        self.assertTestCasesError(vectorMultVector, testCases, ValueError)

    def test_vectorMultVector_correctMatrices(self):
        testCases = [
            {"A": [1, 2, 3], "B": [4, 5, -3], "expectedC": 5},
            {"A": [7, 0, 1, 2, 3], "B": [0, 3, 4, 9, -3], "expectedC": 13}
        ]
        self.assertTestCaseResult(vectorMultVector, testCases)

if __name__ == '__main__':
    unittest.main()