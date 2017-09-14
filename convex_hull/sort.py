__author__ = 'kingofspace0wzz'

import numpy as np

def sort(A, axis = 0):

    quick_sort(A, 0, A.shape[0]-1, axis)

def quick_sort(A, p, r, axis):

    if p < r:
        q = partition(A, p, r, axis)
        quick_sort(A, p, q-1, axis)
        quick_sort(A, q+1, r, axis)


def partition(A, p, r, axis):

    x = A[r][axis]

    i = p-1
    for j in range(p, r):
        if A[j][axis] <= x:
            i = i+1

            temp = A[j]
            A[j] = A[i]
            A[i] = temp


    temp = list(A[i+1])

    A[i+1] = A[r]

    A[r] = np.array(temp)


    return i+1


def test():

    x = np.array([[3,2],[1,2],[5,6],[8,0]])
    sort(x, axis =0)
    print(x)

if __name__ == '__main__':
    test()
