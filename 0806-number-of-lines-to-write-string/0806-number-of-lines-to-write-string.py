class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res, cur = 1, 0
        for i in s:
            width = widths[ord(i) - ord('a')]
            res += 1 if cur + width > 100 else 0
            cur = width if cur + width > 100 else cur + width
        return [res, cur]