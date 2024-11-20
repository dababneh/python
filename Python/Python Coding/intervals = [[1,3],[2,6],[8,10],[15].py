intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x:x[0])
    print(intervals)

    merged_intervals = intervals[0]

    for i in intervals[1:]:
        last_merged = merged_intervals[-1]

        if i[0] <= last_merged[1]:
          last_merged[1] = max(last_merged[1], i[1])

        else:
            # If they don't overlap, simply add the current interval to the merged list
            merged_intervals.append(i)

    return merged_intervals

merge(intervals)