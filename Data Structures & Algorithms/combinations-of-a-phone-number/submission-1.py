class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        letters = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        dp = {}
        dp[0] = [f"{c}" for c in letters[digits[0]]]
        n = len(digits)
        def dfs(i):
            if i in dp: return dp[i]
            res = []
            combis = dfs(i-1)
            for combi in combis:
                for c in letters[digits[i]]:
                    res.append(combi+c)
            dp[i]=res
            return res

        return dfs(n-1)