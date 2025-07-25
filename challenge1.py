def min_operations_to_zero(array_length: int, target_sum: int, array: list[int]) -> int:
    # Dictionary to store suffix sums and minimum steps to reach them from the right
    suffix_sum_map = {}
    current_suffix_sum = 0

    # Traverse from right to left to build suffix sum map
    for index in range(array_length - 1, -1, -1):
        current_suffix_sum += array[index]
        # Store the number of steps only for the first occurrence of the suffix sum
        if current_suffix_sum not in suffix_sum_map:
            suffix_sum_map[current_suffix_sum] = array_length - index

    current_prefix_sum = 0
    minimum_operations = float('inf')

    # Check if removing only from right side can reach the target
    if target_sum in suffix_sum_map:
        minimum_operations = suffix_sum_map[target_sum]

    # Traverse from left to right to compute prefix sums
    for index in range(array_length):
        current_prefix_sum += array[index]
        
        # Case 1: prefix sum alone is enough
        if current_prefix_sum == target_sum:
            minimum_operations = min(minimum_operations, index + 1)

        # Case 2: Combine prefix and suffix (non-overlapping)
        required_suffix_sum = target_sum - current_prefix_sum
        # Ensure suffix doesn't overlap with prefix
        if required_suffix_sum in suffix_sum_map and array_length - suffix_sum_map[required_suffix_sum] > index:
            total_steps = (index + 1) + suffix_sum_map[required_suffix_sum]
            minimum_operations = min(minimum_operations, total_steps)

    # Return the result if a valid operation sequence was found
    return minimum_operations if minimum_operations != float('inf') else -1


# --- Input/Output handling ---
if __name__ == "__main__":
    array_length, target_sum = map(int, input().split())
    array = list(map(int, input().split()))
    result = min_operations_to_zero(array_length, target_sum, array)
    print(result)
