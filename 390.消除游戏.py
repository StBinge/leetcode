#
# @lc app=leetcode.cn id=390 lang=python3
#
# [390] 消除游戏
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        head=1
        step=1
        left=True
        cnt=n
        while cnt>1:
            if left:
                left=False
                head+=step
                cnt//=2
            else:
                if cnt%2==1:
                    head+=step
                cnt//=2
                left=True
            step*=2
        return head
# @lc code=end

assert Solution().lastRemaining(9)==6
assert Solution().lastRemaining(1)==1