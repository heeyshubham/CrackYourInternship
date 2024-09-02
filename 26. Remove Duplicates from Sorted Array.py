class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check={}
        for number in nums:
            if number not in check:
                check[number]=1
        nums[:]=list(check.keys())
        return len(nums)
        
            

        