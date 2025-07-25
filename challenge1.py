def min_operations_to_zero(array_length: int, target_sum: int, array: list[int]) -> int:
    # Dictionary to store suffix sums and minimum steps to reach them from the right
    suffix_sum_map = {}
    current_suffix_sum = 0

    # Traverse from right to left to build suffix sum map
    for index in range(array_length - 1, -1, -1):
        current_suffix_sum += array[index]
        # Store the number of steps only for the first occurrence of the suffix sum
        if current_suffix_sum not in suffix_sum_map:
…    array_length, target_sum = map(int, input().split())
    array = list(map(int, input().split()))
    result = min_operations_to_zero(array_length, target_sum, array)
    print(result)
