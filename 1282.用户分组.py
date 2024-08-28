#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#
from sbw import *


# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = {}
        ret = []
        for i, g in enumerate(groupSizes):
            ar = group.setdefault(g, [])
            ar.append(i)
            if len(ar) == g:
                ret.append(ar)
                group[g] = []
        # ret=[]
        # for k,v in group.items():
        #     for i in range(0,len(v),k):
        #         ret.append(v[i:i+k])
        return ret


# @lc code=end
def is_equal(gs):
    ret = Solution().groupThePeople(gs)
    for g in ret:
        l = len(g)
        assert l != 0
        for idx in g:
            assert gs[idx] == l


is_equal([2, 1, 3, 3, 3, 2])
groupSizes = [3, 3, 3, 3, 3, 1, 3]
is_equal(groupSizes)
