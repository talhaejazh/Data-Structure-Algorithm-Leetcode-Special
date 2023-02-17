class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        
        l = 0
        for r, c in enumerate(s2):
            cnt[c] -= 1
            while cnt[c] < 0:  # If number of characters `c` is more than our expectation
                cnt[s2[l]] += 1  # Slide left until cnt[c] == 0
                l += 1
            if r - l + 1 == len(s1):  # If we already filled enough `p.length()` chars
                return True
            
        return False