class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # sorting two list for comparison
        target = sorted(target)
        arr = sorted(arr)
        if target!=arr:
            return False
        return True
