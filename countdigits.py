# Take the following as input.
# A number
# A digit
# Write a function that returns the number of times digit is found in the number. Print the value returned.

Num = input().strip()
digit = input().strip()
# this is the method to take the input in a python file
# the num will the take the input of the number we need to count

count = 0
# for start we will take the first count to be zero

for digi in Num:
    if digi == digit:
        count += 1
        # if we get the number we are looking for in the array we will plus 1 the num

print(count)

