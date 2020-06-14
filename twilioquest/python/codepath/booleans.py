# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

import argparse

# I didn't write a main guard because you can't for this one.

# Note that this uses code from a previous lesson as boilerplate.
parser = argparse.ArgumentParser(
                            description="Twilioquest: Python: List Iteration"
                                )
parser.add_argument(
                        "greeting",
                        metavar="greeting",
                        # by omitting nargs we encourage it to eat all arguments
                        type=str,
                        help="An attempt at greeting the script"
                   )
args = parser.parse_args()

# still upset at the lack of camelCase, but let's just do this in the meantime.
python_is_glorious = True
failure_is_option  = False
proper_greeting    = False

if ("For the glory of Python!" == args.greeting):
    proper_greeting = True
