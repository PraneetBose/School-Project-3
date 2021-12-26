# Python3 Program to
# accept principal , rate , time and print simple interest and amount

# storing the Principal , Time and Rate  in the variables P , T and R respectively
P = float(input("Enter the principle amount: "))
T = float(input("Enter the time in years: "))
R = float(input("Enter the Rate of Interest per annum"))
# calculating the SI
SI = (P * R * T) / 100
# calculation the amount
amount = P + SI
print("The simple interest is", SI, "and the amount is", amount)
