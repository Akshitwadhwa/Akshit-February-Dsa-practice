# In this question we have to replace the 0 with 5 in the no given to us

def replace_zero_with_five(n):
    return int(str(n).replace('0' , '5'))
N = int(input())
new_num = replace_zero_with_five(N)

print(new_num)
