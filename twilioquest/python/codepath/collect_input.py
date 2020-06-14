# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

import argparse

# I didn't write a main guard because you don't have functions yet in twilioquest.
# if that makes no sense to you, you're fine, just carry on and ignore it.

# Note that this could be written as:
#
# parser = argparse.ArgumentParser(description="Twilioquest: Python: Script Arguments")
# parser.add_argument("inputs", metavar="string", type=str, nargs="+", help="A series of strings to echo back, one per line")
#
# and so on
#
# I've broken it up by argument just for neatness's sake
# you don't necessarily have to this early on
# but in general a 78 or 80 column width is preferred for code most places
# (And I'd encourage an 80 column width)
#
parser = argparse.ArgumentParser(
                            description="Twilioquest: Python: Script Arguments"
                                )
parser.add_argument(
                        "inputs",         # actual name
                        metavar="string", # name shown in help text
                        type=str,         # type for inputs
                        nargs=3,        # how many, here three.
                        help="A series of strings to echo back, one per line"
                   )
args = parser.parse_args()

# I think the problem here is that you don't know variables or lists yet, but
# they need you to be able to do this specific thing to make a simple tester
# give your code input and check outputs. Otherwise you could just print the
# expected output by guessing the input to output without writing any code
# which would be bad. (Many places famously have been gamed during their
# hackathons like this due to their awful automatic testers.)
#
# Anyway... So a variable is like x, y, or z. There's rules but that's later.
# a list is just a variable with multiple entries. (They actually used one!)
# we use a list variable called inputs inside of another called args, populated
# by parser. For now don't worry too much about what these do or really mean,
# just know that *not all variables are the same and not all can do the same
# things done here*. Specifically, parser is an ArgumentParser, which leads to
# much of the rest one step at a time.
#
# They used argv, which is part of sys (argparse parses argv nicely for us).
# on top of this, argv is just a variable, a list variable. Just like our
# inputs variable is. But argparse can filter by type and provide help text
# nearly for free in a standard, readable format! Argparse clearly is better.
#
# But it's also more complicated. So instead of wasting time they just roll on.
#
# ... and they don't explain fstrings well AT ALL.
# so we're not playing their game here much.
# We'll use a more robust argument parser
# and still use a list
# and I guess still use fstrings, because why not?
# explaining them is a task for some other time
# or you can read the pep here:
# https://www.python.org/dev/peps/pep-0498/
#
print(f"{args.inputs[0]}")
print(f"{args.inputs[1]}")
print(f"{args.inputs[2]}")
