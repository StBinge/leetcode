#
# @lc app=leetcode.cn id=2418 lang=python3
# @lcpr version=30204
#
# [2418] 按身高排序
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_idx=sorted(range(len(names)),key=heights.__getitem__,reverse=True)
        return [names[idx] for idx in sorted_idx]
# @lc code=end



#
# @lcpr case=start
# ["Mary","John","Emma"]\n[180,165,170]\n
# @lcpr case=end

# @lcpr case=start
# ["Alice","Bob","Bob"]\n[155,185,150]\n
# @lcpr case=end

#

