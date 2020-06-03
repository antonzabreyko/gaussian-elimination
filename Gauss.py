'''Implementation of Gaussian Elimination using numpy. The purpose of this is twofold:
first, to solve the system if it is solvable. Second, to return an optimal number of steps
in which the system can be solved using the algorithm.
@author Anton A. Zabreyko'''

import numpy as np
'''Object storing the implementation.'''
class GaussElim(object):

    '''Main method that handles the Gaussian Elimination procedure. '''
    @staticmethod
    def solveSystem(equations, solutions):
        if not GaussElim.__prelims__(equations, solutions):
            return

        ideal_system, ideal_solutions = GaussElim.__ideal__(equations, solutions)

    


    '''Ensures that the inputs are valid.'''
    @staticmethod
    def __prelims__(equations, solutions):
        try:
            assert equations.shape[0] == solutions.shape[0]
        except AssertionError as e:
            print("Mismatch: {0} equation(s), {1} solution(s)".format(equations.shape[1], solutions.shape[1]))
            return False
        return True

    '''For an NxM matrix, return an NxN matrix with all linearly independent rows/columns,
        and their corresponding solutions. '''
    @staticmethod
    def __ideal__(equations, solutions):
        ideal_matrix = equations[0][np.newaxis].T
        ideal_solutions = solutions[0][0]
        for i in range(1, equations.shape[0]):
            current = equations[i][np.newaxis].T
            factors = GaussElim.__lstsq__(ideal_matrix, current)
            if not GaussElim.__zero__(np.dot(ideal_matrix, factors) - current):
                ideal_matrix = np.hstack((ideal_matrix, current))
                ideal_solutions = np.vstack((ideal_solutions, solutions[i]))

        return ideal_matrix[:equations.shape[1]].T, ideal_solutions

    '''Checks to see if vector is approximately equal to the zero vector.
        This is needed to deal with Python's approximations. '''
    @staticmethod
    def __zero__(vector):
        return np.allclose(vector, np.zeros((vector.shape[0], 1)))


    ''' An implementation of least squares that does not fail for the vector case. '''
    @staticmethod
    def __lstsq__(A, y):
        if A.shape[1] == 1:
            return np.dot(A.T, y) / (np.linalg.norm(A) ** 2)
        else:
            return np.linalg.lstsq(A, y)



def test():
    equations = np.array([[1, 2], [5, 6]])
    solutions = np.array([[3], [11]])
    print(GaussElim.solveSystem(equations, solutions))

test()
