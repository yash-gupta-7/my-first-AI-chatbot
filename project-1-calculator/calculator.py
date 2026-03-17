def calculate(num1,op,num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        if num2 == 0:
            return "invalid"
        else:
            return num1 / num2
    elif op == "*":
        return num1 * num2
    else:
        return "Invalid operator"
    
if __name__ == "__main__":
    print("=== Welcome to our calculator app ==\n")

    while True:
        print("Operators: +,-,*,/, exit ")

        op = input("Enter the operator : ")

        if op == "exit":
            break

        num1 =  int(input("Enter first number : "))
        num2 =  int(input("Enter second number : "))

        sol = calculate(num1,op,num2)
        print(sol)
 

