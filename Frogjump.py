#https://leetcode.com/problems/frog-jump/
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        canJump = ()
        mem = {}
        for i in range(len(stones)):
            canJump[stones[i]] = i
            if stones[i] > 2*stones[i-1] and i > 3:
                return False

        def helper(stones, k, pos):
            if pos == stones[-1]:
                return True
            else:
                for i in [k-1, k, k+1]:
                    if i > 0 and pos+i in canJump:
                        if helper(stones, i, pos+i):
                            return True
                return False