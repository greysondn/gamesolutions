# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

import argparse

# standard main function
def main():
    # Note that this uses code from a previous lesson as boilerplate.
    parser = argparse.ArgumentParser(
                                description="Twilioquest: Python: Fizzbuzz Challenge"
                                    )
    parser.add_argument(
                            "nums",
                            metavar="number",
                            nargs="+",
                            type=int,
                            help="A number or numbers to fizzbuzz"
                       )
    args = parser.parse_args()

    for num in args.nums:
        # there's a few ways to do this, and I'm just taking one that's semantically
        # clear because I have tutoring students.
        three = False
        five  = False

        # check if it's divisible by either number
        if ((num % 3) == 0):
            three = True
        if ((num % 5) == 0):
            five = True

        # stack conditions in a specific order.
        if (three and five):
            print("fizzbuzz")
        elif(three):
            print("fizz")
        elif(five):
            print("buzz")
        else:
            # note the use of an fstring here!
            print(f"{num}")

# standard main guard
if ("__main__" == __name__):
    main()