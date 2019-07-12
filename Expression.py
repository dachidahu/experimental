def isToeplitz(arr):
    """
    @param arr: int[][]
    @return: bool
    """
      # our code goes here


    if not arr or not arr[0]:
        return True
    n, m = len(arr), len(arr[0])


    def isInboundary(r, c):
        if r >= 0 and r < n and c >= 0 and c < m:
            return True
        else:
            return False


    def verifyDiagonal(r, i):
        c = i
        v = arr[r][c]
        while True:
            r += 1
            c += 1
            t = isInboundary(r, c)
            if not t:
                break
            else:
                if arr[r][c] != v:
                    return False
        return True

    for i in range(m):
        if not verifyDiagonal(0, i):
            return False
    for i in range(n):
        if not verifyDiagonal(i, 0):
            return False
    return True


arr = [[1,2,3,4],[5,1,2,3],[6,6,1,2]]

print isToeplitz(arr)