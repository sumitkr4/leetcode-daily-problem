from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree stores:
        # sum_tree: sum of distinct counts
        # sq_tree: sum of squared distinct counts
        sum_tree = [0] * (4 * n)
        sq_tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, val):
            length = right - left + 1
            old_sum = sum_tree[node]

            sq_tree[node] = (
                sq_tree[node]
                + 2 * val * old_sum
                + length * val * val
            ) % MOD

            sum_tree[node] = (
                old_sum + length * val
            ) % MOD

            lazy[node] += val

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            val = lazy[node]

            apply(node * 2, left, mid, val)
            apply(node * 2 + 1, mid + 1, right, val)

            lazy[node] = 0

        def update(node, left, right, ql, qr, val):
            if ql > right or qr < left:
                return

            if ql <= left and right <= qr:
                apply(node, left, right, val)
                return

            push(node, left, right)

            mid = (left + right) // 2

            update(
                node * 2, left, mid, ql, qr, val
            )
            update(
                node * 2 + 1, mid + 1, right,
                ql, qr, val
            )

            sum_tree[node] = (
                sum_tree[node * 2]
                + sum_tree[node * 2 + 1]
            ) % MOD

            sq_tree[node] = (
                sq_tree[node * 2]
                + sq_tree[node * 2 + 1]
            ) % MOD

        last_seen = {}
        answer = 0

        for i, value in enumerate(nums):
            previous = last_seen.get(value, -1)

            # Distinct counts increase for these start positions.
            update(
                1, 0, n - 1,
                previous + 1, i, 1
            )

            last_seen[value] = i

            # Sum of squares for all subarrays ending at i.
            answer = (
                answer + sq_tree[1]
            ) % MOD

        return answer