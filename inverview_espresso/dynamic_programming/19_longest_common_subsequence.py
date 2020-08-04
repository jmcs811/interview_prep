# given two strings, return the longest common sub sequence

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        len1, len2 = len(text1), len(text2)
        dp = [[0]*(len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1):
            for j in range(len2):
                if text1[i] == text1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[-1][-1]