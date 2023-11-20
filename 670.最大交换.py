#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num<10:
            return num
        array=list(str(num))
        L=len(array)
        maxId=L-1
        # maxVal=array[-1]

        idx1,idx2=-1,-1
        for i in range(L-2,-1,-1):
            if array[i]>array[maxId]:
                # maxVal=array[i]
                maxId=i
            elif array[i]<array[maxId]:
                idx1=i
                idx2=maxId
        if idx1<0:
            return num
        array[idx1],array[idx2]=array[idx2],array[idx1]
        return int(''.join(array))


# @lc code=end
assert Solution().maximumSwap(98368)==98863
assert Solution().maximumSwap(9973)==9973
assert Solution().maximumSwap(2736)==7236
