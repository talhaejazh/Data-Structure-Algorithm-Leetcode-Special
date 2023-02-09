class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        A=nums
        A.sort()
        i = 0
        while i < len(A) and A[i] < 0 and k > 0:
            k-= 1
            A[i] *= -1
            i += 1
        if k % 2 == 0:
            return sum(A)
        else:
            return sum(A) - 2*min(A)