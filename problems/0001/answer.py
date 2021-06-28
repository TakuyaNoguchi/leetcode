class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, m in enumerate(nums):
            for j, n in enumerate(nums[(i + 1):(len(nums))]):
                if m + n == target:
                    return([i, j + i + 1])
