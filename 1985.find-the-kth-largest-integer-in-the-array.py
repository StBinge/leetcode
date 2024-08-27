#
# @lc app=leetcode.cn id=1985 lang=python3
# @lcpr version=30204
#
# [1985] 找出数组中的第 K 大整数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        def qsort(left, right):
            if left >= right:
                return nums[left]
            idx = randint(left, right)
            pivot = nums[idx]
            pl = len(pivot)
            nums[idx], nums[left] = nums[left], nums[idx]
            i = left + 1
            j = left
            r = right + 1
            while i < r:
                if pl < len(nums[i]) or (pl == len(nums[i]) and nums[i] > pivot):
                    nums[i], nums[j + 1] = nums[j + 1], nums[i]
                    j += 1
                    i += 1
                elif pl > len(nums[i]) or (pl == len(nums[i]) and nums[i] < pivot):
                    nums[i], nums[r - 1] = nums[r - 1], nums[i]
                    r -= 1
                else:
                    i += 1
            nums[left], nums[j] = nums[j], nums[left]
            if k <= j:
                return qsort(left, j - 1)
            elif k > r:
                return qsort(r, right)
            return nums[j]

        ret = qsort(0, len(nums) - 1)
        return ret


# @lc code=end
assert Solution().kthLargestNumber(nums=["0", "0"], k=2) == "0"
assert Solution().kthLargestNumber(nums=["2", "21", "12", "1"], k=3) == "2"
assert Solution().kthLargestNumber(nums=["3", "6", "7", "10"], k=4) == "3"


#
# @lcpr case=start
# ["3","6","7","10"]\n4\n
# @lcpr case=end

# @lcpr case=start
# ["2","21","12","1"]\n3\n
# @lcpr case=end

# @lcpr case=start
# ["0","0"]\n2\n
# @lcpr case=end

#
