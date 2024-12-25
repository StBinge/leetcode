#
# @lc app=leetcode.cn id=3160 lang=python3
# @lcpr version=30204
#
# [3160] 所有球里面不同颜色的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors=defaultdict(int)
        colors_cnt=defaultdict(int)
        cnt=0
        ret=[]
        for b,c in queries:
            old=colors[b]
            if old>0:
                colors_cnt[old]-=1
                if colors_cnt[old]==0:
                    cnt-=1
            colors[b]=c
            colors_cnt[c]+=1
            if colors_cnt[c]==1:
                cnt+=1
            ret.append(cnt)
        return ret

# @lc code=end



#
# @lcpr case=start
# 4\n[[1,4],[2,5],[1,3],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,1],[1,2],[2,2],[3,4],[4,5]]\n
# @lcpr case=end

#

