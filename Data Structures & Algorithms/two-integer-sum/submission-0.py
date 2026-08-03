class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            diff = target - number 
            if diff in seen:
                return [seen[diff], index]
            seen[number] = index
        return 