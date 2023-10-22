def main():
        
    def get_num1():
        while True:
            try:
                num1 = int(input("What's the number 1? "))
            except ValueError:
                print("Not a number!")
            else: 
                return num1

    def get_num2():
        while True:
            try:
                num2 = int(input("What's the number 2? "))
            except ValueError:
                print("Not a number!")
            else:
                return num2

    def get_operator():
        while True:
            try:
                operator = str(input("What's the operator (+, -, *, /)? "))
                if operator in ['+', '-', '*', '/']:
                    return operator
            except:
                break        

    def get_result(num1, operator, num2):
        if operator == "+":
            result = num1 + num2
            return result
        elif operator == "-":
            result = num1 - num2
            return result
        elif operator == "*":
            result = num1 * num2
            return result
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
                return result
            else:
                return "Division by zero is not allowed."


    num1 = get_num1()
    operator = get_operator()
    num2 = get_num2()
    result = get_result(num1, operator, num2)

    print(result)

main()