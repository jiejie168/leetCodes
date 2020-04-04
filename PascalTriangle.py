__author__ = 'Jie'
"""
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows: int):
        ## DP algorithm
        triangle_all=[]
        for i in range(numRows):
            row=(i+1)*[None]
            row[0],row[-1]=1,1

            for j in range(1,i):
                row[j]=triangle_all[i-1][j-1]+triangle_all[i-1][j]
            triangle_all.append(row)
        return triangle_all

solution=Solution()
all=solution.generate(5)
print (all)