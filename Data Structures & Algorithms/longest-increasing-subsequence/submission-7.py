class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        dp = [1] * len(nums)

        for i in range(len(nums)):
            print(nums[i])
            for j in range(i):
                if nums[j] < nums[i]:
                    print(dp[i], dp[j])
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)