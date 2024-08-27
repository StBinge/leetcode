#
# @lc app=leetcode.cn id=2038 lang=python3
# @lcpr version=30204
#
# [2038] 如果相邻两个颜色均相同则删除当前颜色
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnta=cntb=0
        deleta=deletb=0

        for c in colors:
            if c=='A':
                cnta+=1
                deletb+=max(0,cntb-2)
                cntb=0
            else :
                cntb+=1
                deleta+=max(0,cnta-2)
                cnta=0

        deletb+=max(0,cntb-2)
        deleta+=max(0,cnta-2)
        
        return deleta>deletb
# @lc code=end
assert Solution().winnerOfGame('AAAABBBB')==False


#
# @lcpr case=start
# "AAABABB"\n
# @lcpr case=end

# @lcpr case=start
# "AA"\n
# @lcpr case=end

# @lcpr case=start
# "ABBBBBBBAAA"\n
# @lcpr case=end

#

