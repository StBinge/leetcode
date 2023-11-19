#
# @lc app=leetcode.cn id=745 lang=python3
#
# [745] 前缀和后缀搜索
#
from typing import List


# @lc code=start





class WordFilter:
    def __init__(self, words: List[str]):
        memo={}
        for i,word in enumerate(words):
            L=len(word)
            for x in range(1,L+1):
                for y in range(1,L+1):
                    key=word[:x]+'#'+word[-y:]
                    memo[key]=i
        self.memo=memo


    def f(self, pref: str, suff: str) -> int:
        return self.memo.get(pref+'#'+suff,-1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# @lc code=end
wordFilter = WordFilter(["apple", "orange"])

assert wordFilter.f("ora", "e") == 1
assert wordFilter.f("a", "e") == 0
assert wordFilter.f("a", "a") == -1
assert wordFilter.f("ora", "le") == -1
