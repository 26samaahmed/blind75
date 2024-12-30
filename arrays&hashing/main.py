from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hash_map = {}
         for i in nums:
            if i in hash_map:
                return True
            else:
                hash_map[i] = 1
         return False


    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            map1[s[i]] = 1 + map1.get(s[i], 0)
            map2[t[i]] = 1 + map2.get(t[i], 0)

        for k in map1:
            if map1[k] != map2.get(k, 0): # compare values (occurences)
                return False
        return True
    

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track_map = {}
        for i in range(len(nums)):
            if target - nums[i] in track_map:
                return [track_map[target - nums[i]], i]
            else:
                track_map[nums[i]] = i

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        matching_map = {}
        main_list = []
        for word in strs:
            sorted_strs.append(''.join(sorted(word)))

        for i in range(len(sorted_strs)):
            if sorted_strs[i] in matching_map:
                matching_map[sorted_strs[i]].append(i)
            else:
                matching_map[sorted_strs[i]] = [i]

        for j in matching_map:
            new_arr = []
            for k in matching_map[j]:
                new_arr.append(strs[k])
            main_list.append(new_arr)
            new_arr = []
        

        return main_list
    

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)
        for n, c in hash_map.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    

    # Solve again bc this is brute force and gets TLE on leetcode
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = 1
        copy = nums.copy()
        for i in range(len(nums)):
            copy.pop(i)
            for j in copy:
                n *= j
            res.append(n)
            copy = nums.copy()
            n = 1
        return res
    

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_seq = 0
        for n in numSet:
            # check if its the start of a sequence. A start of a sequence means there is no number before it
            if (n - 1) not in numSet:
                # then check if there's numbers after it
                length = 0
                while (n + length) in numSet: 
                    length += 1
                # find the maximum
                longest_seq = max(length, longest_seq)
        return longest_seq