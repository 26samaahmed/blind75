from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] <= min_val:
                min_val = prices[i]
            else:
                for j in range(i, len(prices)):
                    profit = abs(min_val - prices[j])
                    max_profit = max(max_profit, profit)
        return max_profit
    

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_window = ""
        max_length = 0
        for i in range(len(s)):
            if s[i] not in longest_window:
                longest_window += s[i]
            else:
                max_length = max(max_length, len(longest_window))
                # include anything after the first occurence of the duplicate
                longest_window = longest_window[longest_window.index(s[i]) + 1:] + s[i]   
        max_length = max(max_length, len(longest_window))
        return max_length