#
# @lc app=leetcode.cn id=1964 lang=python3
# @lcpr version=30204
#
# [1964] 找出到每个位置为止最长的有效障碍赛跑路线
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ret=[]
        d=[]
        for h in obstacles:
            if not d or h>=d[-1]:
                ret.append(len(d)+1)
                d.append(h)
            else:
                idx=bisect_right(d,h)
                ret.append(idx+1)
                d[idx]=h

        return ret

# @lc code=end
assert Solution().longestObstacleCourseAtEachPosition([3,1,5,6,4,2])==[1,1,2,3,2,2]
assert Solution().longestObstacleCourseAtEachPosition([2,2,1])==[1,2,1]
assert Solution().longestObstacleCourseAtEachPosition([1,2,3,2])==[1,2,3,3]


#
# @lcpr case=start
# [1,2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,5,6,4,2]\n
# @lcpr case=end

#

