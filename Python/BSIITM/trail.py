#User function Template for python3
import math
class Solution:
    def isPrime (self, N):
        flag = 0
        # code here
        if ((N == 0) or (N == 1) ):
            return 0
        elif ((N == 2) or (N == 3) or (N == 5) or (N == 7)):
            return 1
        elif(N < 9):
            for i in range (2,9):
                if (N % i == 0):
                    flag = 0
                    break
                else:
                    flag =1
                
        else:
            for j in range (2, int(math.sqrt(N))+1):
                if (N % j == 0):
                    flag = 0
                    break
                else:
                    flag = 1
        if (flag == 1):
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends