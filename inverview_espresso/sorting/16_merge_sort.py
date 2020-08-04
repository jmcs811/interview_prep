class Solution(object):
    def sortArray(self, nums):
        return self.mergeSort(nums)

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) / 2
        left = nums[:mid]
        right = nums[mid:]

        left = self.mergeSort(left)
        left = self.mergeSort(right)

        block = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                block.append(left[l])
                l += 1
            else:
                block.append[right[r]]
                r += 1
            
        if l < len(left):
            block += left[l:]

        if r < len(right):
            block += right[r:]

        return block
            