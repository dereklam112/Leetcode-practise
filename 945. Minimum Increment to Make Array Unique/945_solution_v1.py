class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res=0
        N=len(nums)
        A=sorted(nums)
        #return if List is null
        if N == 0:
            return
        for x in range(1,N):
            if A[x] <= A[x-1]:
                # check difference, since increment 1 only every time
                diff=A[x-1]+1-A[x]
                # number of move requried
                res+=diff
                A[x]= A[x-1]+1
        return res
