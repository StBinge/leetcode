#
# @lc app=leetcode.cn id=3310 lang=python3
# @lcpr version=30204
#
# [3310] 移除可疑的方法
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        calls=defaultdict(list)
        for x,y in invocations:
            calls[x].append(y)
        
        bad={k}
        q=[k]
        while q:
            x=q.pop()
            for nxt in calls[x]:
                if nxt not in bad:
                    bad.add(nxt)
                    q.append(nxt)

        for x,y in invocations:
            if x not in bad and y in bad:
                return list(range(n))
        
        return [i for i in range(n) if i not in bad]



# @lc code=end
assert Solution().remainingMethods(3,2,[[1,0],[2,0]])== [0,1,2]
assert Solution().remainingMethods(n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]])== []
assert Solution().remainingMethods(n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]])== [3,4]
assert Solution().remainingMethods(n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]])==[0,1,2,3]


#
# @lcpr case=start
# 4\n1\n[[1,2],[0,1],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n0\n[[1,2],[0,2],[0,1],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n[[1,2],[0,1],[2,0]]\n
# @lcpr case=end

#

