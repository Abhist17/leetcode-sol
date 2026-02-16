class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        maxLen = max(len(word) for word in wordDict)
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for l in range(1, min(maxLen, i) + 1):
                if dp[i - l] and s[i - l:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[n]