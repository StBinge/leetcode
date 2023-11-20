#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#
from typing import List
# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        short=long=None
        if len(list1)>len(list2):
            short=list2
            long=list1
        else:
            short=list1
            long=list2
        
        s={n:i for i,n in enumerate(short)}
        max_sum=len(list1)+len(list2)
        ret=[]
        for i,n in enumerate(long):
            if i>max_sum:
                break
            if n in s:
                idx_sum=i+s[n]
                if idx_sum<max_sum:
                    max_sum=idx_sum
                    ret=[n]
                elif idx_sum==max_sum:
                    ret.append(n)
        return ret

# @lc code=end
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
assert Solution().findRestaurant(list1,list2)==["Shogun"]

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
assert Solution().findRestaurant(list1,list2)==["Shogun"]
