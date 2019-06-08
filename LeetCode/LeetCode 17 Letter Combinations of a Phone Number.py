class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_map = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz')
        }

        if not digits:
            return []

        if len(digits) == 1:
            return letter_map[digits]

        res = ['']
        for digit in digits:
            res = [strs+c for strs in res for c in letter_map[digit]]

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))