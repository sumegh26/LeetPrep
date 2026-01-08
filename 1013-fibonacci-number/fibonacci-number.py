class Solution:
    def fib(self, n: int) -> int:

        #Base cases
        if n==1:
            return 1
        if n==0:
            return 0
            
        #recursive case
        return self.fib(n-1) + self.fib(n-2)
            