# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

import argparse

# standard main function
def main():
    # Note that this uses code from a previous lesson as boilerplate.
    parser = argparse.ArgumentParser(
                                description="Twilioquest: Python: List Iteration"
                                    )
    parser.add_argument(
                            "names",
                            metavar="name",
                            type=str,
                            nargs="+",        # how many, here at least one.
                            help="A series of names in line of succession"
                       )
    args = parser.parse_args()

    for i in range(len(args.names)):
        # I'll do this in two steps so it's easier to follow, but a natural solution
        # is something like
        # print(f"{i+1}. {args.names[i]}")
        #
        successionIndex = i + 1
        print(f"{successionIndex}. {args.names[i]}")

# standard main guard
if ("__main__" == __name__):
    main()
