#
# @lc app=leetcode.cn id=2151 lang=python3
# @lcpr version=30204
#
# [2151] 基于陈述统计最多好人数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        N=len(statements)
        good_masks=[]
        bad_masks=[]
        for state in statements:
            gm=bm=0
            for i,mark in enumerate(state):
                if mark==0:
                    bm|=1<<i
                elif mark==1:
                    gm|=1<<i
            good_masks.append(gm)
            bad_masks.append(bm)
        
        ret=0
        Mask=(1<<N)-1
        for good_mask in range(1,1<<N):
            cnt=good_mask.bit_count()
            if cnt<=ret:
                continue
            bad_mask=Mask^good_mask

            for i in range(N):
                if good_mask & (1<<i):
                    gm=good_masks[i]
                    if gm & bad_mask:
                        break
                    bm=bad_masks[i]
                    if bm & good_mask:
                        break
            else:
                ret=max(ret,cnt)
        return ret

# @lc code=end
assert Solution().maximumGood([[2,1,2],[1,2,2],[2,0,2]])==2


#
# @lcpr case=start
# [[2,1,2],[1,2,2],[2,0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,0],[0,2]]\n
# @lcpr case=end

#

