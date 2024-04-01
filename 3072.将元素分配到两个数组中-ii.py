#
# @lc app=leetcode.cn id=3072 lang=python3
#
# [3072] 将元素分配到两个数组中 II
#
from sbw import *
# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_set=sorted(set(nums),reverse=True)
        idx_map={n:idx for idx,n in enumerate(sorted_set,1)}
        Max=len(sorted_set)+1
        tree=[0]*Max
        def low_bit(x):
            return x&-x
        def add(x,val):
            while x<Max:
                tree[x]+=val
                x+=low_bit(x)

        def get(x):
            ret=0
            while x>0:
                ret+=tree[x]
                x-=low_bit(x)
            return ret
        def remap(x):
            return idx_map[x]
        ret1=[nums[0]]
        ret2=[nums[1]]
        add(remap(nums[0]),1)
        add(remap(nums[1]),-1)
        for n in nums[2:]:
            x=remap(n)-1
            cnt=get(x)
            v=0
            if cnt>0:
                ret1.append(n)
                v=1
            elif cnt<0:
                ret2.append(n)
                v=-1
            elif len(ret1)<=len(ret2):
                ret1.append(n)
                v=1
            else:
                ret2.append(n)
                v=-1
            add(remap(n),v)
        return ret1+ret2
            

# @lc code=end
assert Solution().resultArray([3,3,3,3])==[3,3,3,3]
assert Solution().resultArray([5,14,3,1,2])==[5,3,1,2,14]
assert Solution().resultArray([2,1,3,3])==[2,3,1,3]
