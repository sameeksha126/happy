number = []
print("enter 10 numbers:")
for i in range (10):
    user_input = input("enter the number:")
    number.append(float(user_input))
total_sum = sum(number)
print("the sum of all elements is",total_sum)
