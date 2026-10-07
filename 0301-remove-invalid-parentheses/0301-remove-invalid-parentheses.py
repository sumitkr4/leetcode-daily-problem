class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        min_remove = self.minRemoval(s)
        result=set()
        def backtracking(index, current, removed):
            
            if removed> min_remove:
                return

            if index==len(s):
                if removed == min_remove and isValid(current):
                    result.add(current)
                return

            ch = s[index]

            if ch == '(' or ch == ')':
                # KEEP
                backtracking(index+1,current+ch,removed)
                # REMOVE
                backtracking(index+1,current,removed+1)
            else:
                # Normal character → KEEP
                backtracking(index + 1, current + ch, removed)

        def isValid(current):
            balance=0
            for ch in current:
                if ch=="(":
                    balance+=1
                elif ch==')':
                    balance-=1
                    if balance < 0:
                        return False
            return balance == 0

        backtracking(0,"",0)
        return list(result)


    def minRemoval(self,s):
        stack=[]
        for bracket in s:
            if bracket =='(':
                stack.append(bracket)
            elif bracket ==')':
                if len(stack)>0 and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(bracket)
        return len(stack)

