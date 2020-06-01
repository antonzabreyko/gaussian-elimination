'''Implementation of Gaussian Elimination using numpy. The purpose of this is twofold:
first, to solve the system if it is solvable. Second, to return an optimal number of steps
in which the system can be solved using the algorithm.
@author Anton A. Zabreyko'''

import numpy as np
'''Object storing the static method.'''
class GaussElim(object):

    '''Main method that handles the Gaussian Elimination procedure. '''
    @staticmethod
    def solveSystem(equations, solutions):
        if not GaussElim.__prelims__(equations, solutions):
            return



    '''Ensures that the inputs are valid.'''
    @staticmethod
    def __prelims__(equations, solutions):
        try:
            assert equations.shape[1] == solutions.shape[1]
        except AssertionError as e:
            print("Mistmatch: {0} equation(s), {1} solution(s)".format(equations.shape[1], solutions.shape[1]))
            return False
        return True

    '''For an NxM matrix, return an NxN matrix with all linearly independent rows/columns. '''
    @staticmethod
    def __ideal__(equations):
        ideal_matrix = equations[0]
        for i in range(1, ideal_matrix.shape[0]):
            if np.linalg.lstsq()



def test():
    equations = np.array([[1, 2], [5, 6]])
    solutions = np.array([[3, 11, 10]])
    print(GaussElim.solveSystem(equations, solutions))

test()
