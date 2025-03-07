#
# @lc app=leetcode.cn id=2289 lang=python3
# @lcpr version=30204
#
# [2289] 使数组按非递减顺序排列
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        N=len(nums)
        st=[]
        ret=0
        for n in nums:
            step=0
            while st and st[-1][0]<=n:
                step=max(step,st.pop()[1])
            if st:
                step+=1
            else:
                step=0
            st.append([n,step])
            ret=max(ret,step)
        return ret
            

            



# @lc code=end
assert Solution().totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]) == 3
assert Solution().totalSteps([4, 5, 7, 7, 13]) == 0
assert Solution().totalSteps([10,1,2,3,4,5,6,1,2,3]) == 6


#
# @lcpr case=start
# [5,3,4,4,7,3,6,11,8,5,11]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,7,7,13]\n
# @lcpr case=end

#
