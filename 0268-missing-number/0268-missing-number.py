class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # i!=nums[i]
        # return i
        n=len(nums)
        sumN_num = (n*(n+1))//2
        sum_nums = sum(nums)
        missingN_num=sumN_num-sum_nums        
        return missingN_num
