class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            print (nums[i])
        res=min(nums)
        if res>0:
            return 1
        else:
            return -res+1
