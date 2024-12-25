#
# @lc app=leetcode.cn id=2409 lang=python3
# @lcpr version=30204
#
# [2409] 统计共同度过的日子数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        def parse(data: str):
            month = int(data[:2])
            day = int(data[3:])
            Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return day + sum(Days[: month - 1])

        x1, y1 = parse(arriveAlice), parse(leaveAlice)
        x2, y2 = parse(arriveBob), parse(leaveBob)
        x = max(x1, x2)
        y = min(y1, y2)
        return max(y - x + 1, 0)


# @lc code=end
assert (
    Solution().countDaysTogether(
        arriveAlice="10-01", leaveAlice="10-31", arriveBob="11-01", leaveBob="12-31"
    )
    == 0
)
assert (
    Solution().countDaysTogether(
        arriveAlice="08-15", leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19"
    )
    == 3
)


#
# @lcpr case=start
# "08-15"\n"08-18"\n"08-16"\n"08-19"\n
# @lcpr case=end

# @lcpr case=start
# "10-01"\n"10-31"\n"11-01"\n"12-31"\n
# @lcpr case=end

#
