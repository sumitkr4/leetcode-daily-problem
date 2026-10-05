class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth=0
        ans=0
        
        for i,ch in enumerate(s):
            if ch=='(':
                depth+=1
            else:
                if s[i-1]=='(':
                    ans+= 2**(depth-1)
                depth-=1
        return ans            