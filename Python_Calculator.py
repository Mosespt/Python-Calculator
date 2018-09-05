print("Python Calculator by Moses")

while True:
  print("Options:")
  print("Enter 'add' to add two numbers")
  print("Enter 'subtract' to subtract two numbers")
  print("Enter 'multiply' to multiply two numbers")
  print("Enter 'divide' to divide two numbers")
  print("Enter 'exist' to end program")
  user_input = input(": ")

  if user_input == "exist":
    break
  elif user_input == "add":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = str(num1 + num2)
    print("The answer is " + result)
  elif user_input == "subtract":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = str(num1 - num2)
    print("The answer is " + result)
  elif user_input == "multiply":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = str(num1 * num2)
    print("The answer is " + result)
  elif user_input == "divide":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = str(num1 / num2)
    print("The answer is " + result)
  else:
    print("Unknown input.")

