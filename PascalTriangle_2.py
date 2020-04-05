__author__ = 'Jie'

"""
119. Pascal's Triangle II
Given a non-negative index k where k <= 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
Example:
Input: 3
Output: [1,3,3,1]
"""

class Solution:
    def getRow_1(self, rowIndex: int):
        result_all=[]
        for i in range(rowIndex+1):
            row=[None]*(i+1)
            row[0],row[-1]=1,1

            for j in range(1,i):
                row[j]=result_all[i-1][j-1]+result_all[i-1][j]
            result_all.append(row)
        return result_all[rowIndex]

    def getRow_2(self,rowIndex):
        # complex is O(k)
        result=[1]+[0]*rowIndex  # use only an 1D array to restore data

        for i in range(rowIndex):
            result[0]=1
            for j in range(i+1,0,-1):
                #reversed add
                result[j]=result[j]+result[j-1]
        return  result


solution=Solution()
# result=solution.getRow_1(3)
result=solution.getRow_2(3)
print (result)