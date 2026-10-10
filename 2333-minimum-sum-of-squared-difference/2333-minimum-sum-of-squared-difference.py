class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Calculate absolute differences
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        
        k = k1 + k2
        total_diff = sum(diffs)
        
        # If total operations can reduce all differences to 0
        if total_diff <= k:
            return 0
        
        # Binary search for the optimal maximum difference limit
        low, high = 0, max(diffs)
        limit = high
        
        while low <= high:
            mid = (low + high) // 2
            # Calculate operations needed to bring all diffs down to 'mid'
            ops_needed = sum(max(0, d - mid) for d in diffs)
            
            if ops_needed <= k:
                limit = mid
                high = mid - 1  # Try to find a lower possible maximum limit
            else:
                low = mid + 1
        
        # Deduct operations used to bring everything down to 'limit'
        for i in range(len(diffs)):
            if diffs[i] > limit:
                k -= (diffs[i] - limit)
                diffs[i] = limit
        
        # Distribute the remaining k operations by reducing remaining 'limit' values by 1
        for i in range(len(diffs)):
            if k == 0:
                break
            if diffs[i] == limit:
                diffs[i] -= 1
                k -= 1
                
        # Return the final sum of squared differences
        return sum(d * d for d in diffs)