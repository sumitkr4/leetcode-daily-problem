
class Solution:
    def minInsertions(self, s: str) -> int:
        balance = 0
        ans = 0

        for bracket in s:

            if bracket == '(':

                # balance must be even before adding a new '('
                if balance % 2 == 1:
                    ans += 1
                    balance -= 1

                balance += 2

            else:
                balance -= 1

                # No '(' available for this ')'
                if balance < 0:
                    ans += 1
                    balance = 1

        return ans + balance


