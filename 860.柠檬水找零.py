#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#
from typing import List
# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for bill in bills:
            if bill==5:
                five+=1
                continue
            elif bill==10:
                if five==0:
                    return False
                ten+=1
                five-=1
            else:
                if ten>0:
                    if five>0:
                        five-=1
                        ten-=1
                    else:
                        return False
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
                
# @lc code=end
bills=[5,5,5,10,20]
assert Solution().lemonadeChange(bills)
bills = [5,5,10,10,20]
assert Solution().lemonadeChange(bills)==False
