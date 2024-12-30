from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
    

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # check if the value in the middle index is already the target
            if nums[mid] == target:
                return mid
            # else we want to check if l < mid to decide which half of the container we should search
            elif nums[l] <= nums[mid]:
                # now check if the target is outside of those ranges
                if target < nums[l] or target > nums[mid]:
                    # focus on right side
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1