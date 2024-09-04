class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        paird={}

        for i,num in enumerate(nums):
            if target - num in paird:
                return [i, paird[target-num]]
            paird[num]=i
