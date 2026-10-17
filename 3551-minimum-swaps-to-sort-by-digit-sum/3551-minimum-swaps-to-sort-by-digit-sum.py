from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        n = len(nums)

        # Sort by digit sum, then by the number itself
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its target index
        target_index = {
            num: i for i, num in enumerate(sorted_nums)
        }

        visited = [False] * n
        swaps = 0

        # Count cycles in the permutation
        for i in range(n):
            if visited[i]:
                continue

            current = i
            cycle_size = 0

            while not visited[current]:
                visited[current] = True
                current = target_index[nums[current]]
                cycle_size += 1

            swaps += max(0, cycle_size - 1)

        return swaps