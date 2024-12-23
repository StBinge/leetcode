#
# @lc app=leetcode.cn id=LCR 075 lang=python3
# @lcpr version=30204
#
# [LCR 075] 数组的相对排序
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        cnt=Counter(arr1)
        ret=[]
        for n in arr2:
            ret.extend([n]*cnt[n])
            del cnt[n]
        for n in sorted(cnt.keys()):
            ret.extend([n]*cnt[n])
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]\n
# @lcpr case=end

#

