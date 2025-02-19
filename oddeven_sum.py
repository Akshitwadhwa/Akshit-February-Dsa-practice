#Take N as input. Print the sum of its odd placed digits and sum of its even placed digits.
N = input().strip()
N = N[::-1]
odd_sum = 0
even_sum = 0

for i in range(len(N)):
    digit = int(N[i])
    if i % 2 ==0:
        odd_sum += digit
    else:
        even_sum += digit
    
print(odd_sum)
print(even_sum)


