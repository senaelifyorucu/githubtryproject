name= input("What is your name?:")
surname= input("What is your surname?:")
id_number= input("What is your id number?:")
print("\nName:", name)
print("Surname:", surname)
print("ID:", id_number)
# Ask the user for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Print the original values
print("\nOriginal values:")
print("Number 1:", number1)
print("Number 2:", number2)

# Swap the values using a temporary variable
temp = number1
number1 = number2
number2 = temp

# Print the values after swapping
print("\nValues after swapping:")
print("Number 1:", number1)
print("Number 2:", number2)

