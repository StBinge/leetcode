#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在LR字符串中交换相邻字符
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        L=len(start)
        i=j=0
        while i<L and j<L:
            while i<L and start[i]=='X':
                i+=1
            while j<L and end[j]=='X':
                j+=1
            if i==L or j==L:
                break
            if start[i]==end[j]:
                if (start[i]=='L' and i>=j) or (start[i]=='R' and i<=j):
                    i+=1
                    j+=1
                    continue
                return False
            else:
                return False
        while i<L:
            if start[i]!='X':
                return False
            i+=1
        
        while j<L:
            if end[j]!='X':
                return False
            j+=1
        return True

                

# @lc code=end
assert Solution().canTransform('X','L')==False

start = "RXXLRXRXL"
end = "XRLXXRRLX"
assert Solution().canTransform(start,end)
assert Solution().canTransform('LXR','RXL')==False
start="LXXLXRLXXL"#LLRLL
end="XLLXRXLXLX"  #LLRLL
assert Solution().canTransform(start,end)==False
