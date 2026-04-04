class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def getCombs(index,currString):
            if index==len(digits):
                res.append(currString)
                return

            chars=digitToChar[digits[index]]
            for char in chars:
                getCombs(index+1,currString+char)

        if digits:
            getCombs(0,"")
            return res
        return []
        