#Given an input array nums,
def find_peak(arr):
    if not arr:
        return None
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < arr[mid+1]:
            lo = mid+1
        else:
            hi = mid
    return arr[lo]

#follow up, if the condidate nums[i] != nums[i+1] does not meet
def find_peak_in_arbitary_arrary(arr):
    if not arr:
        return None
    lo = 0
    n = len(arr)
    hi = len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < arr[mid+1]:
            lo = mid + 1
        elif arr[mid] == arr[mid+1]:
            if arr[mid] > arr[mid-1]:
                return arr[mid]
            else:
                return find_peak_in_arbitary_arrary(arr[:mid] + arr[mid+1:])
        else:
            hi = mid
    return arr[lo]

arr1 = [1,2,3,4,7,4]
arr2 = [1,1,1,1,1,1,2]
arr5 = [1,1,1]
arr6 = [1,2,1,1,1]
arr3 = [1]
arr4 = [1,3]
print find_peak(arr1) == find_peak_in_arbitary_arrary(arr1),find_peak(arr3) == find_peak_in_arbitary_arrary(arr3), find_peak(arr4) == find_peak_in_arbitary_arrary(arr4)
print find_peak_in_arbitary_arrary(arr2),find_peak_in_arbitary_arrary(arr5),find_peak_in_arbitary_arrary(arr6)

