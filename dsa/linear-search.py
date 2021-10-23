"""
Given a list of numbers, find if a number is present or not.
"""

def linear_search(lst, num):
    return num in lst
        


# if linear_search([1, 2, 3, 4], 5):
#     raise Exception("invalid search")

# if not linear_search([1, 2, 3, 4], 4):
#     raise Exception("invalid search")
class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    RESET = '\033[0m'

print("Testing invalid items in list")
if linear_search([1, 2, 3, 4], 5):
    print(bcolors.FAIL + "Failed" + bcolors.RESET)
else:
    print(bcolors.OK + "Passed" + bcolors.RESET)

print("Testing valid items in list")
if not linear_search([1, 2, 3, 4], 4):
    print(bcolors.FAIL + "Failed" + bcolors.RESET)
else:
    print(bcolors.OK + "Passed" + bcolors.RESET)

