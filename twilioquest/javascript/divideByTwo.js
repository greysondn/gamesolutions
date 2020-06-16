// TwilioQuest 3.1.26
// Works in:
//   - 3.1.26
//
// Fun fact: I walk into this good at Python, but terrible at JS.
// Let's see if basic competency can be established just using
// TwilioQuest and what I already know from Python/C++
//

// Divide by two is... ugh.

// Is there no argparse for Node? Really?
// Didn't I complain about this in Python, too?
// https://github.com/greysondn/gamesolutions/blob/master/twilioquest/python/codepath/collect_input.py

// if you'd prefer the pythonic argparse and you're here, there is a node package.
// https://www.npmjs.com/package/argparse

// let's do what they say as it's native. (Does Node not ship batteries included?)

const dividend = Number(process.argv[2])
const divisor  = 2
const result   = dividend / divisor
console.log(result)
