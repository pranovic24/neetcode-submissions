class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(1)
        result, count = 0, 0
        for num in nums:
            count = count + 1 if num else 0
            result = max(count, result)
        return result
        
        
        # Brute Force - Time: O(n^2), Space: O(1)
        # result = 0
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] == 0:
        #             break
        #         count += 1
        #     result = max(count, result)
        # return result