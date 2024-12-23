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
        colors_cnt=defaultdict(int)
        balls=defaultdict(int)
        ret=[]
        for b,c in queries:
            pre_c=balls[b]
            if pre_c>0:
                colors_cnt[pre_c]-=1
                if colors_cnt[pre_c]==0:
                    del colors_cnt[pre_c]
            balls[b]=c
            colors_cnt[c]+=1
            ret.append(len(colors_cnt))
        return ret

# @lc code=end
assert Solution().queryResults(limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]])==[1,2,2,3,4]
assert Solution().queryResults(limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]])==[1,2,2,3]


#
# @lcpr case=start
# 4\n[[1,4],[2,5],[1,3],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,1],[1,2],[2,2],[3,4],[4,5]]\n
# @lcpr case=end

#

