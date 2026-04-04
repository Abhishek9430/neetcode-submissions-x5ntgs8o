class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def generate(oc,cc,balance):
            if oc==cc==0:
                print(balance)
                res.append(balance)
                return
            
            if oc!=0:
                generate(oc-1,cc,balance+"(")
            if oc<cc:
                generate(oc,cc-1,balance+")")
            
        generate(n,n,"")
        return res
        