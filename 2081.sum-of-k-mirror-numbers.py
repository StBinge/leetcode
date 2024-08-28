#
# @lc app=leetcode.cn id=2081 lang=python3
# @lcpr version=30204
#
# [2081] k 镜像数字的和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # ret=sum(range(1,k+1))

        def check(digits:list):
            for i in range(len(digits)//2+1):
                if digits[i]!=digits[-1-i]:
                    return False
            return True

        # for x in range(k+1,10):
        #     digits=[]
        #     _x=x
        #     while x:
        #         digits.append(x%k)
        #         x//=k
        #     ret+=check(digits)*_x

        ret=0
        cnt=0
        length=1
        while cnt<n:
            left_part=(length+1)//2
            for left in range(10**(left_part-1),10**left_part):
                s=str(left)
                if length&1:
                    s=s+s[-2:-left_part-1:-1]
                else:
                    s=s+s[::-1]
                x=int(s)
                _x=x
                digits=[]
                while x:
                    digits.append(x%k)
                    x//=k
                if check(digits):
                    ret+=_x
                    cnt+=1
                    if cnt==n:
                        return ret
            length+=1
        return ret

# @lc code=end
assert Solution().kMirror(7,17)==20379000
assert Solution().kMirror(3,7)==499
assert Solution().kMirror(2,5)==25


#
# @lcpr case=start
# 2\n5\n
# @lcpr case=end

# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 7\n17\n
# @lcpr case=end

#

