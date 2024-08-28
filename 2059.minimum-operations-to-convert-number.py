#
# @lc app=leetcode.cn id=2059 lang=python3
# @lcpr version=30204
#
# [2059] 转化数字的最小运算数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        N = len(nums)
        f = [float("inf")] * 1001
        q = deque()
        if 0 <= goal <= 1000:
            f[goal] = 0
            q.append([0, goal])
        else:
            for n in nums:
                xor = n ^ goal
                if 0 <= xor <= 1000:
                    f[xor] = 1
                    q.append([1, xor])
                if 0 <= goal + n <= 1000:
                    f[goal + n] = 1
                    q.append([1, goal + n])
                if 0 <= goal - n <= 1000:
                    f[goal - n] = 1
                    q.append([1, goal - n])
            

        if f[start]<float('inf'):
            return f[start]
        while q:
            cost, val = q.popleft()
            cost+=1
            for n in nums:
                for nxt in [val + n, val - n, val ^ n]:
                    if nxt == start:
                        return cost
                    if 0 <= nxt <= 1000 and cost < f[nxt]:
                        f[nxt] = cost
                        q.append([cost, nxt])
        return -1


# @lc code=end
assert Solution().minimumOperations([77, 74, 20], 79, 92) == 3
assert Solution().minimumOperations([648,-262,-938,-156,85,552,568,-576,-70,148,872,-847,571,533,775,-545,-38,627,84,-459,-635,33,-520,-990,95,-480,597,-905,453,-588,-642,-150,543,-950,-285,-59,-808,-751,128,-295,-231,-893,-352,-78,-475,-201,-875,-132,643,177,-691,-758,699,850,902,-560,300,-982,-39,486,690,997,-108,-189,948,191,599,-513,592,-916,-779,466,738,452,779,891,15,-452,-671,-217,787,-20,-12,283,-278,198,-598,-281,303,478,45,-558,731,-639,649,123,855,77,-897,635,-953,-913,384,139,833,-610,-8,-96,-749,-489,950,293,-300,-437,-294,407,-466,321,-372,-838,342,298,-23,503,348,823,306,-997,422,637,-414,241,686,-507,-958,242,-345,376,146,-230,874,338,642,79,996,-646,-945,-141,-279,372,608,-608,145,-309,256,-226,689,578,718,-594,770,-879,-282,720,373,-311,-124,768,406,-582,-595,-902,-836,-494,-960,-841,235,431,467,420,-415,-102,-936,749,752,443,359,-955,-166,590,-647,261,-501,124,-474,-697,-404,882,425,-398,305,-467,-194,137,993,-28,-989,-46,-976,-252,687,126,712,-215,-737,-987,-966,-716,-465,723,343,942,86,-521,-888,-686,258,473,-569,930,885,125,-490,311,772,68,-40,-894,-315,793,-316,-199,100,-202,170,-614,138,-399,470,-885,654,-865,-131,573,-609,969,-174,783,575,312,-250,-317,-333,441,140],420,-93) == 1
assert Solution().minimumOperations([2, 8, 16], 0, 1) == -1
assert Solution().minimumOperations(nums=[2, 4, 12], start=2, goal=12) == 2


#
# @lcpr case=start
# [2,4,12]\n2\n12\n
# @lcpr case=end

# @lcpr case=start
# [3,5,7]\n0\n-4\n
# @lcpr case=end

# @lcpr case=start
# [2,8,16]\n0\n1\n
# @lcpr case=end

#
