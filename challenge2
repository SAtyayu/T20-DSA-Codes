
#array is given 
#number of ways
#partition into 3 sub arrays 
#  find indices i j where  where 2≤𝑖≤𝑗≤𝑛−1 such that:
def three_part_harmony(array_length, array):
    MOD = 10**9 + 7
    total_sum = sum(array)

    # If total sum is not divisible by 3, no valid partition is possible
…
    return valid_partitions % MOD


if __name__ == "__main__":
    array_length = int(input())
    array = list(map(int, input().split()))
    print(three_part_harmony(array_length, array))
