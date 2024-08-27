#
# @lc app=leetcode.cn id=1963 lang=python3
# @lcpr version=30204
#
# [1963] 使字符串平衡的最小交换次数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        ret = 0
        cnt=0
        for ch in s:
            if ch=='[':
                cnt+=1
            else:
                cnt-=1
                if cnt==-1:
                    ret+=1
                    cnt+=2
        return ret


# @lc code=end
assert Solution().minSwaps("[]") == 0
assert Solution().minSwaps("]]][[[") == 2
assert Solution().minSwaps("][][") == 1


#
# @lcpr case=start
# "][]["\n
# @lcpr case=end

# @lcpr case=start
# "]]][[["\n
# @lcpr case=end

# @lcpr case=start
# "[]"\n
# @lcpr case=end

#
