#
# @lc app=leetcode.cn id=3387 lang=python3
# @lcpr version=30204
#
# [3387] 两天自由外汇交易后的最大货币数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:

        def calc(pairs,rates):
            g=defaultdict(list)
            for [x,y],r in zip(pairs,rates):
                g[x].append([y,r])
                g[y].append([x,1/r])
            
            dist={}
            q=[[initialCurrency,1.0]]
            while q:
                cur,val=q.pop()
                if cur in dist:
                    continue
                dist[cur]=val
                for nxt,r in g[cur]:
                    q.append([nxt,val*r])
            return dist
        
        day1_mount=calc(pairs1,rates1)
        day2_mount=calc(pairs2,rates2)
        return max(day1_mount.get(k,0)/v for k,v in day2_mount.items())
# @lc code=end
assert Solution().maxAmount(initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0])==1.0
assert Solution().maxAmount(initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0])==1.5
assert Solution().maxAmount(initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0])==720.0


#
# @lcpr case=start
# "EUR"\n[["EUR","USD"],["USD","JPY"]]\n[2.0,3.0]\n[["JPY","USD"],["USD","CHF"],["CHF","EUR"]]\n[4.0,5.0,6.0]\n
# @lcpr case=end

# @lcpr case=start
# "NGN"\n[["NGN","EUR"]]\n[9.0]\n[["NGN","EUR"]]\n[6.0]\n
# @lcpr case=end

# @lcpr case=start
# "USD"\n[["USD","EUR"]]\n[1.0]\n[["EUR","JPY"]]\n[10.0]\n
# @lcpr case=end

#

