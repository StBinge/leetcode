#
# @lc app=leetcode.cn id=2376 lang=python3
# @lcpr version=30204
#
# [2376] 统计特殊整数
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s=str(n)
        l=len(s)

        ret=0
        for i in range(l-1):
            ret+=9*math.perm(9,i)
        
        def pick(idx,cnt,limit=False):
            if cnt==0:
                return 0
            if idx==l:
                return 1*cnt
            if not limit:
                return math.perm(10-idx,l-idx)*cnt
            d=int(s[idx])

            used=set()
            for i in range(idx):
                if s[i]<=s[idx]:
                    used.add(s[i])
            no_limit=d-len(used)+(s[idx] in used)
            if no_limit<=0:
                cnt1=0
            else:
                cnt1=pick(idx+1,cnt*no_limit)
            if s[idx] in used:
                cnt2=0
            else:
                cnt2=pick(idx+1,cnt,True)
            return cnt1+cnt2

        last=pick(1,int(s[0])-1,False)+pick(1,1,True)
        return ret+last


        
# @lc code=end
assert Solution().countSpecialNumbers(99)==90
assert Solution().countSpecialNumbers(135)==110
assert Solution().countSpecialNumbers(5)==5
assert Solution().countSpecialNumbers(20)==19


#
# @lcpr case=start
# 20\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 135\n
# @lcpr case=end

#

