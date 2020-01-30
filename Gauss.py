import numpy as np


class GaussianEliminator(object):

    def __init__(self):
        self.place_holder = None

    #equations is an nxn list containing the values for the parameters of the equations
    #solutions is an 1xn list containing the solutions to each of the equations
    def solve_system(self, equations, solutions):
        return checkPrereqs(equations)

    #check that the matrix has the minimum number of linearly independent rows
    def checkPrereqs(self, equations):
        return None

    def pre_processMatrix(self, equations):
        return None

    def solveIdealMatrix(self, equations, solutions):
        return None

    def checkOthers(self, parameters, remaining_equations, solutions):
        return None

    #checks to see if 2 vectors are linearly independent or not
    def isLinearlyIndependent(self, vector1, vector2):
        if len(vector1) != len(vector2):
            return True
        if len(vector1) == 0:
            return False

        try:
            const = vector1[0]/vector2[0]
        except ZeroDivisionError:
            return self.isLinearlyIndependent(vector1[1:], vector2[1:])

        for i in range(1, len(vector1)):
            try:
                if const != vector1[i]/vector2[i]:
                    return True
            except ZeroDivisionError:
                return True
        return False



def test(): #should probably implement a check to make sure its a square matrix
    gauss = GaussianEliminator()

    A = [
        [1, 2],
        [5, 6]]

    y = [8, 10]
    #print(gauss.solve_system(A, y))
    print(gauss.isLinearlyIndependent([5, 4, 0], [0, 1, 0]))
test()
