# Start coding here
#array is given 
#number of ways
#partition into 3 sub arrays 
#  find indices i j where  where 2≤𝑖≤𝑗≤𝑛−1 such that:
def three_part_harmony(array_length, array):
    MOD = 10**9 + 7
    total_sum = sum(array)

    # If total sum is not divisible by 3, no valid partition is possible
    if total_sum % 3 != 0:
        return 0

    target_sum = total_sum // 3
    current_prefix_sum = 0
    count_first_cut_positions = 0
    valid_partitions = 0

    # We go only up to array_length - 1 to ensure third part is non-empty
    for index in range(array_length - 1):
        current_prefix_sum += array[index]

        # If the current prefix sum is 2 * target, we can make the second cut here.
        # The number of valid first cuts (where sum == target) is already counted.
        if current_prefix_sum == 2 * target_sum:
            valid_partitions = (valid_partitions + count_first_cut_positions) % MOD

        # Count the number of times we can make the first cut (prefix sum == target)
        if current_prefix_sum == target_sum:
            count_first_cut_positions += 1

    return valid_partitions % MOD


if __name__ == "__main__":
    array_length = int(input())
    array = list(map(int, input().split()))
    print(three_part_harmony(array_length, array))
