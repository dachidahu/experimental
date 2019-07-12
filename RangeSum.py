class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0] * len(nums)
        self.data = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            self.update(i, nums[i])
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff, self.nums[i] = val - self.nums[i], val
        i += 1
        while i <= len(self.nums):
            self.data[i] += diff
            i += (i & -i)

    def rangeSum(self, i):
        s = 0
        while i:
            s += self.data[i]
            i -= (i & -i)
        return s

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.rangeSum(j + 1) - self.rangeSum(i)

#2D

class FenwickTree:
    def __init__(self, m, n):
        self.d = [[0 for _ in range(n)] for _ in range(m)]
        self.m = m
        self.n = n

    def update(self, i, j, delta):
        k = j
        while i < self.m:
            j = k
            while j < self.n:
                self.d[i][j] += delta
                j += j & -j
            i += i & -i

    def query(self, i, j):
        s = 0
        k = j
        while i > 0:
            j = k
            while j > 0:
                s += self.d[i][j]
                j -= j & -j
            i -= i & -i
        return s


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        m = len(matrix)
        if not m:
            return
        n = len(matrix[0])
        if not n:
            return
        self.FT = FenwickTree(m + 1, n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.FT.update(i, j, matrix[i - 1][j - 1])

    def update(self, row, col, val):

        self.FT.update(row + 1, col + 1, val - self.matrix[row][col])
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):

        return self.FT.query(row2 + 1, col2 + 1) + self.FT.query(row1, col1) \
               - self.FT.query(row1, col2 + 1) - self.FT.query(row2 + 1, col1)





    # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)