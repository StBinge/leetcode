#
# @lc app=leetcode.cn id=2024 lang=python3
# @lcpr version=30204
#
# [2024] 考试的最大困扰度
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def change(ch):
            left=0
            cnt=k
            ret=0
            for right in range(len(answerKey)):
                if answerKey[right]!=ch:
                    if cnt==0:
                        ret=max(ret,right-left)
                        while answerKey[left]==ch:
                            left+=1
                        left+=1
                        cnt+=1
                    cnt-=1
            return max(ret,len(answerKey)-left)
        
        cnt_t=change('T')
        cnt_f=change('F')
        return max(cnt_f,cnt_t)
                    
# @lc code=end
assert Solution().maxConsecutiveAnswers(answerKey = "TTFTTFTT", k = 1)==5
assert Solution().maxConsecutiveAnswers(answerKey = "TFFT", k = 1)==3
assert Solution().maxConsecutiveAnswers(answerKey = "TTFF", k = 2)==4


#
# @lcpr case=start
# "TTFF"\n2\n
# @lcpr case=end

# @lcpr case=start
# "TFFT"\n1\n
# @lcpr case=end

# @lcpr case=start
# "TTFTTFTT"\n1\n
# @lcpr case=end

#

