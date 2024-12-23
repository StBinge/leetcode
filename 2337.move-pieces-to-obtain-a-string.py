#
# @lc app=leetcode.cn id=2337 lang=python3
# @lcpr version=30204
#
# [2337] 移动片段得到字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        idx1=idx2=0
        N1=len(start)
        N2=len(target)
        while idx1<N1 or idx2<N2:
            while idx1<N1 and start[idx1]=='_':
                idx1+=1
            while idx2<N2 and target[idx2]=='_':
                idx2+=1
            ch1=start[idx1] if idx1<N1 else ''
            ch2=target[idx2] if idx2<N2 else ''
            if ch1!=ch2:
                return False
            if ch1=='' or (ch1=='L' and idx1>=idx2) or (ch1=='R' and idx1<=idx2):
                idx1+=1
                idx2+=1
                continue
            else:
                return False
        return True

# @lc code=end
assert Solution().canChange("_L","LR")==False
assert Solution().canChange(start = "_R", target = "R_")==False
assert Solution().canChange(start = "R_L_", target = "__LR")==False
assert Solution().canChange(start = "_L__R__R_", target = "L______RR")


#
# @lcpr case=start
# "_L__R__R_"\n"L______RR"\n
# @lcpr case=end

# @lcpr case=start
# "R_L_"\n"__LR"\n
# @lcpr case=end

# @lcpr case=start
# "_R"\n"R_"\n
# @lcpr case=end

#

