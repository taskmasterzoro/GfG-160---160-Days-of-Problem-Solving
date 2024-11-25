#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here 
        n=len(arr)
        if n<2:
            return -1
        max=sec=float('-inf')
        for num in arr:
            if num > max:
                sec=max
                max=num
            elif num>sec and num!=max:
                sec=num
        if sec==float('-inf'):
            return -1
        else:
            return sec

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
