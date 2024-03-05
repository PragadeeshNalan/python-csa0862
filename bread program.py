a = eval(input("Enter new bread loaves purchased: "))
b = eval(input("Enter old bread loaves purchased: "))
m = 185.00
n = 185 * 0.600
x = m * a
z = n * b

if a > 0:
    print("Amount of new bread loaves:", x)
else:
    print("No new bread loaves purchased")

if b > 0:
    print("Amount of old bread loaves:", z)
else:
    print("No old bread loaves purchased")

total_amount = (x if a > 0 else 0) + (z if b > 0 else 0)
print("Total amount:",total_amount)
