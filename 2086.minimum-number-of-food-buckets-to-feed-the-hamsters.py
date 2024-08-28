#
# @lc app=leetcode.cn id=2086 lang=python3
# @lcpr version=30204
#
# [2086] 喂食仓鼠的最小食物桶数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        ret=0
        N=len(hamsters)
        idx=0
        while idx<N:
            if hamsters[idx]=='H':
                if idx+1<N and hamsters[idx+1]=='.':
                    ret+=1
                    idx+=2
                elif idx>0 and hamsters[idx-1]=='.':
                    ret+=1
                else:
                    return -1
            idx+=1
        return ret

# @lc code=end
assert Solution().minimumBuckets('.H.H.')==1


#
# @lcpr case=start
# "H..H"\n
# @lcpr case=end

# @lcpr case=start
# ".H.H."\n
# @lcpr case=end

# @lcpr case=start
# ".HHH."\n
# @lcpr case=end

#

