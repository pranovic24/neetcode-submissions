class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Brute Force - Time: O(n^2), Space: O(1)
        result = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    break
                count += 1
            result = max(count, result)
        return result