#
# @lc app=leetcode.cn id=1773 lang=python3
#
# [1773] 统计匹配检索规则的物品数量
#
from sbw import *
# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx=0
        if ruleKey=='color':
            idx=1
        elif ruleKey=='name':
            idx=2
        return sum(item[idx]==ruleValue for item in items)
# @lc code=end
assert (ret:=Solution().countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))==1
