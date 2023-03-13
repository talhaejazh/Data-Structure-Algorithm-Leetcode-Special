class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: 
            return False
        N=len(matrix[0]) #x-axis length no. columns
        M=len(matrix) #y-axis length col no. row
        l,r=0,(M*N)-1 #flatten the matrix virtually
            
        while l<=r:
            mid=(l+r)//2
            if matrix[mid//N][mid%N]==target:
                return True
            elif matrix[mid//N][mid%N]<target:
                l=mid+1
            else:
                r=mid-1
        return False
            
        