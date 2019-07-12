

#DP

# DFS solution with memory
def canPartition(nums):
    s = sum(nums)
    d = {}
    if s % 2 != 0:
        return False
    else:
        def helper(nums, i, target):
            if (i, target) in d:
                return d[(i,target)]
            elif target == 0:
                ans = True
            elif i >= len(nums):
                ans =  False
            elif nums[i] > target:
                ans =  False
            elif helper(nums, i+1, target) or helper(nums, i+1, target-nums[i]):
                ans = True
            else:
                ans = False
            d[(i, target)] = ans
            return ans
        return helper(nums, 0, s/2)

#BFS
def canPartition2(nums):
    s = sum(nums)
    d = {}
    if s % 2 != 0:
        return False
    else:
        nums.sort(reverse=True)
        def helper(start, target):
            if target == 0:
                return True
            if start >= len(nums):
                return False
            for i in range(start, len(nums)):
                if target - nums[i] < 0:
                    break;
                if helper(i+1, target-nums[i]):
                    return True
            return False
        return helper(0, s/2)

#DP 2D
def canPartition3(nums):
    s = sum(nums)
    n = len(nums)
    target = s / 2
    if s % 2 != 0:
        return False
    else:
        dp = [[False] * (target+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(target+1):
                if j == 0:
                    dp[i][j] = True
                else:
                    if j-nums[i-1] >= 0:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]


#DP 1D
def canPartition3(nums):
    s = sum(nums)
    n = len(nums)
    target = s / 2
    if s % 2 != 0:
        return False
    else:
        dp = [False] * (target+1)
        dp[0] = True
        for i in range(0, n):
            for j in range(target, 0, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] | dp[j-nums[i]]
        return dp[-1]


def CanPartitionK(nums, k):
    s = sum(nums)
    m = max(nums)
    n,r = divmod(s, k)
    if r != 0:
        return False
    if m > n:
        return False
    nums.sort()
    def helper(groups):
        if len(nums) == 0:
            return True
        else:
            v = nums.pop()
            for i, g in enumerate(groups):
                if g+v <= n:
                    groups[i] += v
                    if helper(groups):
                        return True
                    groups[i] -= v
                #no need to add
                if groups[i] == 0:
                    break;
            nums.append(v)
            return False







print canPartition3([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,97,95,99,99])

