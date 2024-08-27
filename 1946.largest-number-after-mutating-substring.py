#
# @lc app=leetcode.cn id=1946 lang=python3
# @lcpr version=30204
#
# [1946] 子字符串突变后可能得到的最大整数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        s=list(num)
        N=len(s)
        for i in range(N):
            n=int(s[i])
            if change[n]<=n:
                continue
            for j in range(i,N):
                n=int(s[j])
                if n>change[n]:
                    break
                s[j]=str(change[n])
            break
        return ''.join(s)
# @lc code=end
assert Solution().maximumNumber(num = "5", change = [1,4,7,5,3,2,5,6,9,4])=="5"
assert Solution().maximumNumber(num = "021", change = [9,4,3,5,7,2,1,9,0,6])=="934"
assert Solution().maximumNumber(num = "132", change = [9,8,5,0,3,6,4,2,6,8])=='832'


#
# @lcpr case=start
# "132"\n[9,8,5,0,3,6,4,2,6,8]\n
# @lcpr case=end

# @lcpr case=start
# "021"\n[9,4,3,5,7,2,1,9,0,6]\n
# @lcpr case=end

# @lcpr case=start
# "5"\n[1,4,7,5,3,2,5,6,9,4]\n
# @lcpr case=end

#

