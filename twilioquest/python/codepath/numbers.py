# TwilioQuest version 3.1.26
# Works in:
#    3.1.26

import argparse

# I didn't write a main guard because that would break checking for this one.

parser = argparse.ArgumentParser(
                            description="Twilioquest: Python: Numbers and Math"
                                )
parser.add_argument(
                        "nums",         # actual name
                        metavar="number", # name shown in help text
                        type=float,         # type for inputs
                        nargs=2,        # how many, here two.
                        help="A pair of numbers to work with"
                   )
args = parser.parse_args()

first_number = args.nums[0]
second_number = args.nums[1]

result_sum        = first_number + second_number
result_difference = first_number - second_number
result_product    = first_number * second_number
result_quotient   = first_number / second_number
