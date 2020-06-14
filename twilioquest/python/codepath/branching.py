# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

import argparse

# standard main function
def main():
    # Note that this uses code from a previous lesson as boilerplate.
    parser = argparse.ArgumentParser(
                                description="Twilioquest: Python: Conditional Logic"
                                    )
    parser.add_argument(
                            "nums",
                            metavar="number",
                            nargs=2,
                            type=int,
                            help="Numbers to add."
                       )
    args = parser.parse_args()

    # finally, camelCase!
    total = args.nums[0] + args.nums[1]

    if (total <= 0):
        print("You have chosen the path of destitution")
    elif (total <= 100):
        print("You have chosen the path of plenty.")
    elif (total > 100):
        print("You have chosen the path of excess.")
    else:
        # this is literally just a protective branch. It shouldn't ever be reached.
        raise ValueError("How did you even get to this branch?")

# standard main guard
if ("__main__" == __name__):
    main()