# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum.
from typing import List


def maxSubArray_iterative(nums: List[int]) -> int:
    sum = 0
    maxsum = 0
    max = nums[0]
    for x in nums:
        if max < x:
            max = x
        sum += x
        if sum < 0:
            sum = 0
        if maxsum < sum:
            maxsum = sum
    if max < 0:
        return max
    return maxsum


def maxSubArray_helper(nums: List[int]) -> (int, int, int, int):
    if len(nums) == 1:
        return nums[0], nums[0], nums[0], nums[0]
    mid = len(nums) // 2
    (subLeft, prefixLeft, suffixLeft, sumLeft) = maxSubArray_helper(nums[:mid])
    (subRight, prefixRight, suffixRight, sumRight) = maxSubArray_helper(nums[mid:])
    subarray = max(subLeft, subRight, suffixLeft + prefixRight)
    prefix = max(prefixLeft, sumLeft + prefixRight)
    suffix = max(suffixRight, sumRight + suffixLeft)
    sumTotal = sumLeft + sumRight
    return subarray, prefix, suffix, sumTotal


def maxSubArray_recursive( nums: List[int]) -> int:
    solution_set = maxSubArray_helper(nums)
    return solution_set[0]


if __name__ == "__main__":
    list1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray_recursive(list1))
    print(max(list1))
