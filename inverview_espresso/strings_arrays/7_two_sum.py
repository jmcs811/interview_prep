
# TIME: O(n^2)
# SPACE: O(1)
def two_sum_naive(nums, target):
    for i, num in enumerate(nums):
        for j in range(i+1, len(nums)):
            if nums[j] == (target - num):
                return [i, j]

# TIME: O(n)
# SPACE: O(n)
def two_sum_one_pass(nums, target):
    ht = {}
    for i, num in enumerate(nums):
        counterPart = target - num
        if counterPart in ht:
            return [ht[counterPart], i]
        else:
            ht[num] = i



print(two_sum_naive([3,4,8,2], 6))
print(two_sum_one_pass([3,4,8,2], 6))