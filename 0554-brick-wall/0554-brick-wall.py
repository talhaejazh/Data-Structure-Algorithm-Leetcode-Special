class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0 : 0} #mapping position : count of brick gaps

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())
            