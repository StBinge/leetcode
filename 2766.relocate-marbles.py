#
# @lc app=leetcode.cn id=2766 lang=python3
# @lcpr version=30204
#
# [2766] 重新放置石块
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        pos=set(nums)
        for f,t in zip(moveFrom,moveTo):
            if f==t:
                continue
            pos.remove(f)
            pos.add(t)
        return sorted(pos)
# @lc code=end
assert Solution().relocateMarbles([3,4],[4,3,1,2,2,3,2,4,1],[3,1,2,2,3,2,4,1,1])==[1]
assert Solution().relocateMarbles(nums = [1,1,3,3], moveFrom = [1,3], moveTo = [2,2])==[2]


#
# @lcpr case=start
# [1,6,7,8]\n[1,7,2]\n[2,9,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,3,3]\n[1,3]\n[2,2]\n
# @lcpr case=end

#

