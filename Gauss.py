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
    def __prelims__(equations, solutions):
        try:
            assert equations.shape[1] == solutions.shape[1]
        except AssertionError as e:
            print("Mistmatch: {1} equation(s), {2} solution(s)".format(equations.shape[1]. solutions.shape[1]))
            return False
        return True





def test():
    equations = np.array([[1, 2], [5, 6]])
    solutions = np.array([[3, 11]])
    print(GaussElim.solveSystem(equations, solutions))

test()
