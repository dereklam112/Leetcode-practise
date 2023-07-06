#requirement: sum of divisors, number with EXACTLY 4 divisors
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res=0
        for x in(nums):
            count= set()
            for y in range(1,int(sqrt(x))+1):
                if x%y == 0:
                    count.add(x//y)
                    count.add(y)
                    if len(count)>4:
                        break
            if len(count)==4:
                res +=sum(count)
        return res
