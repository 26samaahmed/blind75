from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                new_str += i.lower()
        return new_str[0:] == new_str[::-1]
    

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # loop through every character and its index
        for i, a in enumerate(nums):
            # skip if the current num is a duplicate
            if i > 0 and a == nums[i - 1]:
                continue

            # use 2 pointer method to find every triplet that gives 0 with the current a number
            l, r = i + 1, len(nums) - 1
            while l < r:
                # if the current sum is greater than 0, decrement the r pointer
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else: # if the sum is equal 0 then append it to the final list
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    

    def maxArea(self, heights: List[int]) -> int:
        # for area, im trying to get the longest width * shorter height of the 2 poles
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            longest_width = r - l
            shorter_height = min(heights[l], heights[r])
            area = longest_width * shorter_height
            max_area = max(max_area, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area


