__author__ = 'Jie'
"""
training of utilize recursion algorithm
"""

class Recursion:

    def factorial(self,n):
        ## procedure: 1) inital conditions,  2) find the recursion relation, 3) when to end
        if n<=1:
            return 1
        return n*self.factorial(n-1)

    def fibonaci(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fibonaci(n-1)+self.fibonaci(n-2)

recursion=Recursion()

# f=recursion.factorial(50)
# print (f)
fib=recursion.fibonaci(5)
print (fib)