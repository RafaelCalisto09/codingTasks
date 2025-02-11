# Read the number of test cases
num_tests = int(input('Enter a number: '))

for _ in range(num_tests):
    try:
        # Read the values of a and b
        a, b = input().split()
        result = int(a) // int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
#
# #Example of usage
# 3
# 1 0
# 2 $
# 3 1