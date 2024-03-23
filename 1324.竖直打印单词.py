#
# @lc app=leetcode.cn id=1324 lang=python3
#
# [1324] 竖直打印单词
#
from sbw import *
# @lc code=start
import itertools
class Solution:
    def printVertically(self, s: str) -> List[str]:
        return [''.join(row).rstrip() for row in itertools.zip_longest(*s.split(' '),fillvalue=' ')]
# @lc code=end
assert Solution().printVertically("TO BE OR NOT TO BE")==["TBONTB","OEROOE","   T"]
assert Solution().printVertically("HOW ARE YOU")==["HAY","ORO","WEU"]
