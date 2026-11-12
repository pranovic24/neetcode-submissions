class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n), Space: O(1)/O(n)
        prod, zero_count = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        
        if zero_count > 1: 
            return [0] * len(nums)
        
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count:
                result[i] = 0 if num else prod
            else:
                result[i] = prod // num
        return result

        