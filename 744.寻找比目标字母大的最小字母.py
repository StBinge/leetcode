#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#
from typing import List
# @lc code=start
import bisect
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>=letters[-1]:
            return letters[0]
        return letters[bisect.bisect_right(letters,target)]
# @lc code=end
letters = ["c", "f", "j"]
target = "a"
assert Solution().nextGreatestLetter(letters,target)=='c'
letters = ["c","f","j"]
target = "c"
assert Solution().nextGreatestLetter(letters,target)=='f'
