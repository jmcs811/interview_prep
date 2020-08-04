# TIME: O(n^2)
# SPACE: O(n)
def three_sum(nums):
    answer = []
    nums.sort()
    length = len(nums)
    for i in range(length):
        left, right = i + 1, length - 1
        if i > 0 and nums[i - 1] == nums[i]: continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                answer.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left + 1] == nums[left]:
                    left += 1
                while left < right and nums[right - 1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
            elif total > 0:
                right -= 1
            else:
                left += 1
        return answer
print(three_sum([-1, 0, 1, 2, -1, -4]))