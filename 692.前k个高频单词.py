#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
from typing import List

# @lc code=start
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return sorted(counter.keys(), key=lambda x: (-counter[x], x))[:k]


# @lc code=end
words = ["aaa", "aa", "a"]
k = 3
assert Solution().topKFrequent(words, k) == ["a", "aa", "aaa"]
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
assert Solution().topKFrequent(words, k) == ["i", "love"]
assert Solution().topKFrequent(words, 1) == ["i"]

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
assert Solution().topKFrequent(words, k) == ["the", "is", "sunny", "day"]
