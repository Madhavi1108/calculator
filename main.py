import math

def calculator():
    try:
        input_function = input().strip().upper()
        num1 = int(input().strip())

        if input_function == "PRIME CHECK":
            if num1 < 1:
                print("INVALID INPUT")
                return

            # Check if a number is prime
            def check_prime(num):
                if num < 2:
                    return False
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        return False
                return True

            if check_prime(num1):
                print("PRIME")
            else:
                print("NOT PRIME")

        elif input_function == "NEXT PRIME":
            # If the number is negative, it's an invalid input
            if num1 < 0:
                print(2)
                return

            # Get the next prime number
            num = num1 + 1
            def check_prime(num):
                if num < 2:
                    return False
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        return False
                return True

            while True:
                if check_prime(num):
                    print(num)
                    break
                num += 1

        elif input_function == "PREV PRIME":
            # If the number is negative, it's an invalid input
            if num1 <= 2:
                print("INVALID INPUT")
                return

            # Get the previous prime number
            num = num1 - 1
            def check_prime(num):
                if num < 2:
                    return False
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        return False
                return True

            while num > 1:
                if check_prime(num):
                    print(num)
                    break
                num -= 1
            else:
                print("INVALID INPUT")

        elif input_function in ["LCM", "HCF", "PRODUCT", "SUM", "DIVISION"]:
            num2 = int(input().strip())  # Read second number

            if input_function == "LCM":
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a

                a, b = num1, num2
                gcd_value = gcd(a, b)
                lcm = abs(num1 * num2) // gcd_value
                print(lcm)

            elif input_function == "HCF":
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a

                a, b = num1, num2
                print(gcd(a, b))

            elif input_function == "PRODUCT":
                print(num1 * num2)

            elif input_function == "SUM":
                print(num1 + num2)

            elif input_function == "DIVISION":
                if num2 != 0:
                    print(num1 // num2)
                else:
                    print("INVALID INPUT")

        else:
            print("INVALID INPUT")

    except:
        print("INVALID INPUT")


calculator()
