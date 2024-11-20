intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge(intervals):
    # If the list of intervals is empty, return an empty list
    if not intervals:
        return []

    # Sort the intervals by the start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the merged intervals list with the first interval
    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        # Get the last interval in the merged_intervals
        last_merged = merged_intervals[-1]

        # If the current interval overlaps with the last merged interval
        if current[0] <= last_merged[1]:
            # Merge them by updating the end of the last merged interval
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # If they don't overlap, simply add the current interval to the merged list
            merged_intervals.append(current)

    return merged_intervals

print(merge(intervals))
