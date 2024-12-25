#
# @lc app=leetcode.cn id=2167 lang=python3
# @lcpr version=30204
#
# [2167] 移除所有载有违禁货物车厢所需的最少时间
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTime(self, s: str) -> int:
        N=len(s)
        pre_cnt1=[0]
        for ch in s:
            pre_cnt1.append(pre_cnt1[-1]+(ch=='1'))
        
        @cache
        def dfs(l,r):
            if l>r:
                return 0
            left,right=l,r
            while left<=right and s[left]=='1':
                left+=1
            
            while right>=left and s[right]=='1':
                right-=1
            
            if left>right:
                return r-l+1
            
            edge_removed=left-l+r-right
            mid_cnt1=pre_cnt1[right+1]-pre_cnt1[left]
            if mid_cnt1==0:
                return edge_removed
            mid_removed=mid_cnt1*2
            _left=left
            while s[_left]=='0':
                _left+=1
            mid_removed=min(mid_removed,dfs(_left,right))

            _right=right
            while s[_right]=='0':
                _right-=1
            mid_removed=min(mid_removed,dfs(left,_right))
            return edge_removed+mid_removed

        ret=dfs(0,len(s)-1)
        return ret


# @lc code=end
assert Solution().minimumTime('010110')==5
assert Solution().minimumTime('101')==2
assert Solution().minimumTime('011001111111101001010000001010011')==25
assert Solution().minimumTime('1100101')==5
assert Solution().minimumTime('010011')==4


#
# @lcpr case=start
# "1100101"\n
# @lcpr case=end

# @lcpr case=start
# "0010"\n
# @lcpr case=end

#

