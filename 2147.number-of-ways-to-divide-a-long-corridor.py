#
# @lc app=leetcode.cn id=2147 lang=python3
# @lcpr version=30204
#
# [2147] 分隔长廊的方案数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ret=1
        cnt_s=0
        pre=0
        for i,ch in enumerate(corridor):
            if ch=='S':
                cnt_s+=1
                if cnt_s>2 and cnt_s&1:
                    ret=(ret*(i-pre))%(10**9+7)
                pre=i
        return ret if cnt_s and cnt_s&1==0 else 0
        


# @lc code=end
assert Solution().numberOfWays()


#
# @lcpr case=start
# "SSPPSPS"\n
# @lcpr case=end

# @lcpr case=start
# "PPSPSP"\n
# @lcpr case=end

# @lcpr case=start
# "S"\n
# @lcpr case=end

#

