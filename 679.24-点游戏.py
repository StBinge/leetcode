#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#
from typing import List
# @lc code=start
import math
from fractions import Fraction
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # if cards[0]*cards[1]*cards[3]*cards[2]<24:
        #     return False
        
        add,mul,div,sub=0,1,2,3
        def calc(nums:list):
            L=len(nums)
            if L==0:
                return False
            if L==1:
                return nums[-1]==24

            for i,x in enumerate(nums):
                for j,y in enumerate(nums):
                    if i==j:
                        continue
                    new_nums=[]
                    for z in range(L):
                        if i==z or z==j:
                            continue
                        new_nums.append(nums[z])

                    for k in range(4):
                        if k<2 and i>j:
                            continue

                        if k==mul:
                            new_nums.append(x*y)
                        elif k==div:
                            if y==0:
                                continue
                            new_nums.append(x/y)
                        elif k==add:
                            new_nums.append(x+y)
                        elif k==sub:
                            new_nums.append(x-y)
                        
                        if calc(new_nums):
                            return True
                        new_nums.pop()
            return False
        nums=[Fraction(n) for n in cards]

        return calc(nums)

# @lc code=end

assert Solution().judgePoint24([1,9,1,2])
assert Solution().judgePoint24([1,5,9,1])==False
assert Solution().judgePoint24([4,1,8,7])
assert Solution().judgePoint24([1,2,1,2])==False