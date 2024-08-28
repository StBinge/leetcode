#
# @lc app=leetcode.cn id=1944 lang=python3
# @lcpr version=30204
#
# [1944] 队列中可以看到的人数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        N=len(heights)
        ret=[0]*N
        st=[]
        for i in range(N-1,-1,-1):
            h=heights[i]
            cnt=0
            while st and h>=st[-1]:
                st.pop()
                cnt+=1
            ret[i]=cnt+(len(st)>0)
            st.append(heights[i])
        return ret
# @lc code=end
assert Solution().canSeePersonsCount([3,1,5,8,6])==[2,1,1,1,0]
assert Solution().canSeePersonsCount([5,1,2,3,10])==[4,1,1,1,0]
assert Solution().canSeePersonsCount([10,6,8,5,11,9])==[3,1,2,1,1,0]


#
# @lcpr case=start
# [10,6,8,5,11,9]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,2,3,10]\n
# @lcpr case=end

#

