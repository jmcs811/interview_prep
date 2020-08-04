# TIME: O(lg n)
# SPACE: O(1)
def search_insert_position(arr, target):
    lo = 0
    hi = len(arr) -1

    while lo <= hi:
        mid = int((hi + lo) / 2)
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
        
    return lo

print(search_insert_position([1, 3, 5, 7], 6))