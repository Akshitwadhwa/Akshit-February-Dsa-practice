def find_unique(arr):
    unique = 0
    for num in arr:
        unique ^= num
    return unique

n = int(input())
arr = list(map(int , input().split()))
arr = [4, 1, 2, 1, 2]
print("Unique number:", find_unique(arr))