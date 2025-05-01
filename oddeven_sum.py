def max_complete_rows(n):
    low, high = 0, n
    result = 0

    while low <= high:
        mid = (low + high) // 2
        coins_needed = mid * (mid + 1) // 2
        
        if coins_needed == n:
            return mid
        elif coins_needed < n:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result

# Input
n = int(input())
print(max_complete_rows(n))