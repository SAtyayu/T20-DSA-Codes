from math import gcd
from functools import reduce

# Read input
array_length, query_count = map(int, input().split())
array = list(map(int, input().split()))

# Step 1: Compute prefix GCDs
# prefix_gcd[i] = GCD of array[0] to array[i]
prefix_gcd = [0] * array_length
prefix_gcd[0] = array[0]
for i in range(1, array_length):
    prefix_gcd[i] = gcd(prefix_gcd[i - 1], array[i])

# Step 2: Compute suffix GCDs
# suffix_gcd[i] = GCD of array[i] to array[array_length - 1]
suffix_gcd = [0] * array_length
suffix_gcd[-1] = array[-1]
for i in range(array_length - 2, -1, -1):
    suffix_gcd[i] = gcd(suffix_gcd[i + 1], array[i])

# Step 3: Handle each query
for _ in range(query_count):
    left, right = map(int, input().split())
    left -= 1  # Convert to 0-based indexing
    right -= 1

    # Compute GCD of the remaining elements
    if left == 0:
        # All elements before `left` are excluded
        result_gcd = suffix_gcd[right + 1] if right + 1 < array_length else 0
    elif right == array_length - 1:
        # All elements after `right` are excluded
        result_gcd = prefix_gcd[left - 1]
    else:
        # Combine GCD of both left and right remaining parts
        result_gcd = gcd(prefix_gcd[left - 1], suffix_gcd[right + 1])

    print(result_gcd)
