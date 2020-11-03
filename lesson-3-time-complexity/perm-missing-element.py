'''
An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''

# sorting and then looking for the missing element doesn't work here because time complexity is too high

def solution_mathematical(A):
    expected = (len(A) + 1) * (len(A) + 2) // 2
    # This problem has a mathematical solution, based on the fact that the sum of consecutive integers from 1 to n is equal to n(n+1)/2.

    return expected - sum(A)

