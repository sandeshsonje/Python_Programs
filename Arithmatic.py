def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1//num2

def main():
    num1 = eval(input("Enter number 1 = "))
    num2 = eval(input("Enter number 2 = "))
    print("Addition = ",add(num1,num2))
    print("Subtraction = ",sub(num1,num2))
    print("Multiplication = ",mul(num1,num2))
    print("Division = ",div(num1,num2))

if __name__ == '__main__':
    main()
