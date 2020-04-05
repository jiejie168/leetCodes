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
        if n<=1:
            return n
        return self.fibonaci(n-1)+self.fibonaci(n-2)

    def fibonaci_dp(self,n):
        ## using DP
        if n==0:
            return 0
        fib=(n+1)*[None]
        fib[0]=0
        fib[1]=1
        for i in range(2,n+1):
            fib[i]=fib[i-1]+fib[i-2]
        return fib[n]

recursion=Recursion()

# f=recursion.factorial(50)
# print (f)
fib=recursion.fibonaci(10)
fib1=recursion.fibonaci_dp(10)
print (fib)
print(fib1)