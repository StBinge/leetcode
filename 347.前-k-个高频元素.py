#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from typing import List
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for n in nums:
            cnt=counter.get(n,0)+1
            counter[n]=cnt
        ar=list(counter.items())

        k-=1
        left,right=0,len(ar)-1
        while True:
            # l,r=left,right
            pivot=ar[left][1]
            # pivot_item=ar[right]
            index=left
            for i in range(left+1,right+1):
                if ar[i][1]>pivot:
                    index+=1
                    ar[i],ar[index]=ar[index],ar[i]
            ar[index],ar[left]=ar[left],ar[index]
            if index==k:
                return [item[0] for item in ar[:k+1] ]
            if index>k:
                right=index-1
            else:
                left=index+1
            
                
# @lc code=end
print(Solution().topKFrequent([5,2,5,3,5,3,1,1,3],2))#3,5
print(Solution().topKFrequent( [5,3,1,1,1,3,73,1],2))#1,3
print(Solution().topKFrequent( [4,1,-1,2,-1,2,3],2))# -1,2
print(Solution().topKFrequent( [1,1,1,2,2,3],2))#1 2
print(Solution().topKFrequent( [1],1))#1
