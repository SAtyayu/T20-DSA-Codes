# Start coding here
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    num_lamps = int(data[0])
    genies_house_index = int(data[1])
    lamp_info = []

    # Reading lamp positions and their ranges
    index = 2
    for _ in range(num_lamps):
        lamp_position = int(data[index])
        lamp_range = int(data[index + 1])
        lamp_info.append((lamp_position, lamp_range))
        index += 2

    # Difference array to efficiently update light coverage
    diff_array = [0] * (genies_house_index + 3)  # Extra buffer space for safety

    # Marking light coverage from each lamp
    for position, radius in lamp_info:
        left = max(0, position - radius)
        right = min(genies_house_index, position + radius)
        diff_array[left] += 1
        diff_array[right + 1] -= 1  # Marking end of range +1

    # Building lamp coverage count at each position
    light_coverage = [0] * (genies_house_index + 2)
    active_lamps = 0
    for i in range(genies_house_index + 1):
        active_lamps += diff_array[i]
        light_coverage[i] = active_lamps

    # Calculating maximum dark stretch (where no light or overlapping light)
    max_dark_length = 0
    current_dark_stretch = 0
    for i in range(genies_house_index + 1):
        if light_coverage[i] == 1:
            # Lit by exactly one lamp, so it's considered lit
            current_dark_stretch = 0
        else:
            # Either unlit or overlapped, so it's dark
            current_dark_stretch += 1
            max_dark_length = max(max_dark_length, current_dark_stretch)

    print(max_dark_length)


# Entry point
if __name__ == "__main__":
    solve()
