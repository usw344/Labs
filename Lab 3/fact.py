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
    prod = 1
    for i in range (1 , n ):
        prod = prod * i
    return prod


if factorial(5) == 120:
    print("Function is working")
else:
    print("this function has a bug")
    print("expecting 120 instead got",factorial(5))