#
# @lc app=leetcode.cn id=LCP 18 lang=python3
# @lcpr version=30204
#
# [LCP 18] 早餐组合
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        s=[0]*(x+1)
        for st in staple:
            if st<=x:
                s[st]+=1
        
        for i in range(1,x+1):
            s[i]+=s[i-1]
        
        ret=0
        for d in drinks:
            if d<=x:
                ret+=s[x-d]
                ret%=(10**9+7)
        return ret

# @lc code=end



#
# @lcpr case=start
# [10,20,5]\n[5,5,2]\n15`>\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1]\n[8,9,5,1]\n9`>\n
# @lcpr case=end

#

