# function to check for the power of 2
def power_of_two(n):
    return n and (not(n & (n - 1)))


# Function to check if the number is a Proth number or not
def proth_number(n):
    k = 1
    while k < (n // k):
        # check if k divides n or not
        if n % k == 0:
            # check if n/k is a power of 2 or not
            if power_of_two(n//k):
                return True
            # move k to the next odd number
        k = k + 2
    return False


# inputting n
n = int(input("Enter Proth Number: "))
# checking if n is a proth number
if proth_number(n - 1):
    print("YES")
else:
    print("NO")