class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False]*n
        dp.append(True)
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if dp[i]==True: break
                if s[i:i+len(word)]==word and dp[i+len(word)]==True:
                    dp[i] = True
        return dp[0]