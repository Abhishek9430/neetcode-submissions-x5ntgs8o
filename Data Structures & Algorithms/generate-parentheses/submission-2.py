class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(ob,cb,balance):
            if ob == cb == 0:
                res.append(balance)

            if ob != 0:
                generate(ob-1,cb,balance+"(")
            if ob < cb:
                generate(ob,cb-1,balance+")")
            
        generate(n,n,"")
        return res