def search(l,key):
    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2
        if l[mid] < key:
            low = mid + 1
        elif l[mid] > key:
            high = mid - 1
        else:
            return mid
    return

l = [1,2,3,4,5,6,7,8,9]
print("key index is:",search(l,6))