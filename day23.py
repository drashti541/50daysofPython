#Task 1: Simple Calculator
print("\n*******************Task 1: Simple Calculator*******************")
def calculator():
    while True:
        try:
            op = input("Enter the operator (+, -, *, /) or press 'q'/'Q' for exit: ")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            elif op == 'q' or 'Q':
                break
            else:
                print("Invalid operator Try again.")
                continue

            print("Result:", result)

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
        except NameError:
            print("Error: Only numbers are allowed.")
        except ValueError:
            print("Error: Only numbers are allowed.")

calculator()




#Task 2: Multiply Words
print("\n*******************Task 2: Multiply Words*******************")
def multiply_words(s1):
    mul = 1
    for i in s1.split(" "):
        if i.islower():
            mul = len(i) * mul
    return mul

# s1 = "Hate war love Peace"
# s1 = "love live and laugh"
s1 = input("Enter string: ")
result_multiply = multiply_words(s1)
print(result_multiply)


