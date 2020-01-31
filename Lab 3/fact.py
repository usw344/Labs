# CMPT 145 Lab03: Version Control
#
def factorial ( n ):
    """
    Purpose :
    Calculate the factorial of a non - negative integer
    Pre - conditions :
    n : non - negative integer
    Return :
    a non - negative integer
    """
    if n == 0:
        return 1
    else:
        return n * factorial (n -1)

if factorial(5) == 120:
    print("Function is working")
else:
    "this function has a bug"