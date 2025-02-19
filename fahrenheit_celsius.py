# In this question we have to find the code for converting the temperature given in (Fahrenheit to Celsius)


# --- to start ---
def Fahrenheit_to_Celsius(f):
    return int((5/9) * (f-32))
    # this is the formula used for converting which is 5/9 multiplied by (f-32)

min_f = int(input())
max_f = int(input())
step = int(input())

for f in range(min_f , max_f +1 , step):
    c = Fahrenheit_to_Celsius(f)
    print(f"{f} {c}")