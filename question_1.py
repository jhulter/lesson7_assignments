# Task 1

try:
    temp = input("Please enter the temperature in degrees Fahrenheit: ")
    celsius = (int(temp) - 32) * 5/9

# Task 2

except ValueError:
    if temp != int:
        print("The temperature must be a digit...")

# Task 3
else:
    print(f"The temperature in degrees Celsius is {celsius}")

# Task 4
finally:
    print("Thank you for using our handy dandy temperature converter!")
