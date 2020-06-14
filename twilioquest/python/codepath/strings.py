# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

import argparse

# standard main function
def main():
    parser = argparse.ArgumentParser(
                                description="Twilioquest: Python: Strings"
                                    )
    parser.add_argument(
                            "incoming",
                            metavar="string",
                            type=str,
                            help="String to get psyched about"
                       )
    args = parser.parse_args()

    out = args.incoming.upper() + "!!!"
    print(f"{out}")

# standard main guard
if ("__main__" == __name__):
    main()
