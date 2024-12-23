#
# @lc app=leetcode.cn id=LCS 02 lang=python3
# @lcpr version=30204
#
# [LCS 02] 完成一半题目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        cnt=Counter(questions)
        ret=0
        N=len(questions)>>1
        for v in sorted(cnt.values(),reverse=True):
            if N>0:
                ret+=1
                N-=v
            else:
                break
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,1,6,2]`>\n
# @lcpr case=end

# @lcpr case=start
# [1,5,1,3,4,5,2,5,3,3,8,6]`>\n
# @lcpr case=end

#

