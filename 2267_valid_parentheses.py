class Solution:

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n = len(grid[0])
        
        if (m+n-1)%2==1:
            return False

        if grid[0][0]==")" or grid[m-1][n-1]=="(":
            return False
        memo = {}
        return self.solve(0,0,0,grid,m,n,memo)

    def solve(self,i,j,openCount,grid,m,n,memo):
        state=(i,j,openCount)
        if state in memo:
            return memo[state]

        if grid[i][j]=="(":
            openCount +=1
        else:
            openCount-=1

        if openCount<0 : 
            memo[state]=False
            return False

        if (i==m-1) and (j==n-1):
            memo[state]=(openCount==0)
            return memo[state]

        #move down

        if i+1<m:
            if self.solve(i+1,j,openCount,grid,m,n,memo):
                memo[state]=True
                return True

        #move right
        if j+1<n:
            if self.solve(i,j+1,openCount,grid,m,n,memo):
                memo[state] = True
                return True
        memo[state] = False
        return False
        

        
grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
vp = Solution()
print(vp.hasValidPath(grid))
