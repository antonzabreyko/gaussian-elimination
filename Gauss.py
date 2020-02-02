#Important note: vectors are represented by Python lists. Matrices are 2d Lists.


class GaussianEliminator(object):

    def __init__(self):
        self.place_holder = None

    #equations is an mxn list containing the values for the parameters of the equations
    #solutions is an 1xn list containing the solutions to each of the equations
    def solve_system(self, equations, solutions):
        #assert len(solutions) <= len(equations), "Not enough equations to compute definite answer" ---> add this to checkPrereqs

        ideal_matrix = self.getIdealMatrix(equations)
        ideal_solutions = self.getIdealSolutions(equations, ideal_matrix, solutions)
        print(ideal_matrix)
        print(ideal_solutions)

        if self.checkPrereqs(ideal_matrix): #'''Step needs to be added to make sure that there is non-zero in all [i][i] indices'''
            self.solveIdealMatrix(ideal_matrix, ideal_solutions)
            print(ideal_solutions)
            return

        return "Cannot solve"

    def getIdealMatrix(self, equations):
        removed_indices = []
        if self.isZeroVector(equations[0]):
            return self.getIdealMatrix(equations[1:])
        ideal_matrix = [equations[0]]
        for i in range(1, len(equations)):
            if self.checkMatrixLinearIndependence(ideal_matrix, equations[i]):
                ideal_matrix.append(equations[i])

        return ideal_matrix

    #Return a vector of filtered solutions.
    def getIdealSolutions(self, equations, ideal_matrix, solutions):
        ideal_solutions = []
        for i in range(len(equations)):
            if equations[i] in ideal_matrix:
                ideal_solutions.append(solutions[i])
        return ideal_solutions

    #check that the matrix has the minimum number of linearly independent rows
    def checkPrereqs(self, equations):
        return len(equations) >= len(equations[0])

    def processMatrix(self, matrix):
        return matrix[0:]


    #Takes in an ideal nxn matrix, and solves it using Gaussian elimination.
    def solveIdealMatrix(self, equations, solutions):
        for i in range(len(equations)-1):
            for j in range(1, len(equations)):
                try:
                    scale_factor = equations[j][i]/equations[i][i]
                    equations[j][i] = equations[j][i] - equations[i][i] * scale_factor
                    solutions[j] = solutions[j] - solutions[i] * scale_factor
                except ZeroDivisionError:
                    continue

        for i in range(len(equations)-1, 0, -1):
            print('helllooo!')
            scale_factor = 1/equations[i][i]
            equations[i][i] *= scale_factor
            solutions[i] *= scale_factor
            for j in range(i-1, -1, -1):
                try:
                    scale_factor = equations[j][i]/equations[i][i]
                    equations[j][i] = equations[j][i] - equations[i][i] * scale_factor
                    solutions[j] = solutions[j] - solutions[i] * scale_factor
                except ZeroDivisionError:
                    continue
        print(equations)
        return solutions


    def checkOthers(self, parameters, remaining_equations, solutions):
        return None

    #checks if matrix's rows are linearly independent with the given vector
    def checkMatrixLinearIndependence(self, matrix, vector):
        for v in matrix:
            if not self.isLinearlyIndependent(v, vector):
                return False
        return True

    #checks if a given vector is the zero vector or not
    def isZeroVector(self, vector):
        for i in range(len(vector)):
            if vector[i] != 0:
                return False
        return True

    #checks to see if 2 vectors are linearly independent or not
    def isLinearlyIndependent(self, vector1, vector2):
        if len(vector1) != len(vector2): #in this problem, two vectors of non-equivalent length are defined as being linearly independent
            return True

        if len(vector1) == 0: #generally this will only be encountered in recursion, if one of the vectors is the zero vector
            return False

        try: #try to get a constant for testing linear independence
            const = vector1[0]/vector2[0]
        except ZeroDivisionError:
            return self.isLinearlyIndependent(vector1[1:], vector2[1:])

        for i in range(1, len(vector1)): #iterate through each index and see if any of them demonstrate linear independence
            try:
                if const != vector1[i]/vector2[i]:
                    return True
            except ZeroDivisionError:
                return True
        return False



def test(): #should probably implement a check to make sure its a square matrix
    gauss = GaussianEliminator()

    A = [
        [0, 0],
        [1, 2],
        [5, 6],
        [10, 12],
        [0, 0]]

    y = [0, 8, 10, 20, 0]
    print(gauss.solve_system(A, y))
test()
