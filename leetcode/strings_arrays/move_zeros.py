class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
          if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

test = Solution()
nums = [0, 1, 0, 3, 12]
test.moveZeroes(nums)
print(nums)