# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

# bog standard main function
def main():
    print("functions")
    hail_friend()

    print("function arguments")
    hail_friend("Operator")

    print("function return values")
    print(f"{add_numbers(45, -1)}")

# functions the tasks demand
def add_numbers(num1, num2):
    return num1 + num2

def hail_friend(name=None):
    # use default value to pass Function challenge
    if (None == name):
        print("Hail, friend!")
    else:
        # use given value to pass argument challenge
        print(f"Hail, {name}!")

# standard main guard
if ("__main__" == __name__):
    main()
