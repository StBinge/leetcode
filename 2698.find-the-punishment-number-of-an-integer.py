#
# @lc app=leetcode.cn id=2698 lang=python3
# @lcpr version=30204
#
# [2698] 求一个整数的惩罚数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(s,idx,pre,t):
            if idx==len(s):
                return pre==t
            cur=0
            for i in range(idx,len(s)):
                cur=cur*10+int(s[i])
                if pre+cur>t:
                    break
                if dfs(s,i+1,pre+cur,t):
                    return True
            return False
                         
        ret=1
        for i in range(4,n+1):
            if dfs(str(i*i),0,0,i):
                ret+=i*i

            
        return ret
# @lc code=end
assert Solution().punishmentNumber(37)==1478
assert Solution().punishmentNumber(10)==182


#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 37\n
# @lcpr case=end

#

