class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) == 0:
            return False

        nums.sort()
        p1, p2 = 0, 1
        
        for i in nums:
            # print(nums[p1], nums[p2])
            if nums[p1] == nums[p2]:
                return True
            elif p2 == (len(nums) - 1):
                return False
            else:
                p1 += 1
                p2 += 1