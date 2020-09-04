def max_subarray_sum(arr):
    current_max = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            current_max = max(current_max, sum(arr[i:j]))
    return current_max


def max_subarray_sum_fast(arr):
     max_ending_here = max_so_far = 0
     for x in arr:
         max_ending_here = max(x, max_ending_here + x)
         max_so_far = max(max_so_far, max_ending_here)
     return max_so_far
