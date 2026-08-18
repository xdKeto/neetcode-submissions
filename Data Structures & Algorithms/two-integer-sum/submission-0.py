class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        for i, num in enumerate(nums):
            temp = target - num
            ans.append(i)
            for j in range(i+1, len(nums)):
                if nums[j] == temp:
                    ans.append(j)
                    return ans
            ans.clear()
        return []