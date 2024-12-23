#
# @lc app=leetcode.cn id=2248 lang=python3
# @lcpr version=30204
#
# [2248] 多个数组求交集
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from itertools import chain
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        cnt=Counter(chain(*nums))
        ret=[k for k in cnt if cnt[k]==len(nums)]
        ret.sort()
        return ret
# @lc code=end
assert Solution().intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])==[3,4]


#
# @lcpr case=start
# [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#

