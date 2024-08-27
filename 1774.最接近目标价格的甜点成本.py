#
# @lc app=leetcode.cn id=1774 lang=python3
#
# [1774] 最接近目标价格的甜点成本
#
from sbw import *
# @lc code=start
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        baseCosts.sort()
        dif=min(abs(baseCosts[0]-target),abs(baseCosts[-1]-target))
        max_topping=dif+target-baseCosts[0]
        if max_topping<=0:
            return baseCosts[0]
        
        toppings=set([0])
        for t in toppingCosts:
            temp=set()
            for pre in toppings:
                cur=pre+t
                for _ in range(2):
                    if cur>max_topping:
                        break
                    temp.add(cur)
                    cur+=t
            toppings.update(temp)
        toppings=sorted(toppings)
        
        TN=len(toppings)
        tid=TN-1
        if toppings[-1]+baseCosts[-1]<=target:
            return toppings[-1]+baseCosts[-1]
        if toppings[0]+baseCosts[0]>=target:
            return toppings[0]+baseCosts[0]
        ret=baseCosts[-1]
        for base in baseCosts:
            while tid>=0 and base+toppings[tid]>target:
                tid-=1
            cur_cost=base+(toppings[tid] if tid>=0 else 0)
            cur_dif=abs(cur_cost-target)
            if cur_dif<dif:
                dif=cur_dif
                ret=cur_cost
            elif cur_dif==dif:
                ret=min(ret,cur_cost)
            if cur_cost< target and tid+1<TN:
                prev_cost=base+toppings[tid+1]
                if prev_cost-target<dif:
                    dif=prev_cost-target
                    ret=prev_cost
            if ret==target:
                return ret
        return ret
            
# @lc code=end
assert Solution().closestCost([4,10,8,8],[10,6,10,9,9,6,5],7)==8
assert Solution().closestCost([3,10],[2,5],9)==8
assert Solution().closestCost([4],[9],9)==13
assert Solution().closestCost(baseCosts = [10], toppingCosts = [1], target = 1)==10
assert Solution().closestCost(baseCosts = [3,10], toppingCosts = [2,5], target = 9)==8
assert Solution().closestCost(baseCosts = [2,3], toppingCosts = [4,5,100], target = 18)==17
assert Solution().closestCost(baseCosts = [1,7], toppingCosts = [3,4], target = 10)==10
