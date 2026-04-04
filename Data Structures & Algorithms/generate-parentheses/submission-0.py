class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(oc,cc,balance,res):
            if oc==cc==0:
                res.append(balance)
                return
            if oc!=0:
                generate(oc-1,cc,balance+"(",res)
            if oc<cc: # i.e. open brackets should be used more in order for close brackets to be used
                generate(oc,cc-1,balance+")",res)

        oc=n
        cc=n
        balance=""
        res=[]
        generate(oc,cc,balance,res)
        return res
        