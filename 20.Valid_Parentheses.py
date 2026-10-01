class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        st=[]

        for ch in s:
            if len(st)==0:
                st.append(ch)
                continue
            if ch == ')' or ch == '}' or ch == ']':
                if st[-1]==par[ch]:
                    st.pop()
                else:
                    st.append(ch)
            else:
                st.append(ch)

        if len(st):
            return False
        return True

s=Solution()
print(s.isValid("()[]{}"))

