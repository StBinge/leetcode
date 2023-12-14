#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
from sbw import *
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # n=len(fruits)
        l=0
        counter={}
        ret=0
        for r,fr in enumerate(fruits):
            counter[fr]=counter.get(fr,0)+1
            while len(counter)>2:
                counter[fruits[l]]-=1
                if counter[fruits[l]]==0:
                    del counter[fruits[l]]
                l+=1
            ret=max(ret,r-l+1)
        return ret

# @lc code=end
fruits = [3,3,3,1,2,1,1,2,3,3,4]
assert Solution().totalFruit(fruits)==5

fruits = [1,2,3,2,2]
assert Solution().totalFruit(fruits)==4

fruits = [0,1,2,2]
assert Solution().totalFruit(fruits)==3

fruits = [1,2,1]
assert Solution().totalFruit(fruits)==3
