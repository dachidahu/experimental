class Solution(object):
    def findMedianSortedArrays(self, A, B):

        la, lb = len(A), len(B)
        if (la + lb) % 2 == 0:
            return (self.findKth(A, B, (la + lb) / 2) + self.findKth(A, B, (la + lb) / 2 - 1)) / 2.0
        else:
            return self.findKth(A, B, (la + lb) / 2)



    def findKth(self, A, B, k):
        if not A:
            return B
        if not B:
            return A
        n, m = len(A)/2, len(B)/2
        if n+m > k:
            if A[n] > B[m]:
                return self.findKth(A[:n], B, k)

            else:
                return self.findKth(A, B[:m], k)
        else:
            if A[n] > B[m]:
                return self.findKth(A, B[m:], k-m-1)
            else:
                return self.findKth(A[n:], B, k-n-1)







