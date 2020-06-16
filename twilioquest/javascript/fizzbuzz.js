// TwilioQuest 3.1.26
// Works in:
//   - 3.1.26
//
// Fun fact: I walk into this good at Python, but terrible at JS.
// Let's see if basic competency can be established just using
// TwilioQuest and what I already know from Python/C++
//

// I have no idea how to do a compound else/if (pythonically, an elif) so...
// Guess I'm down to nesting these :/

// convert inputValue to number
const inputValue = Number(process.argv[2])

// and now default to outputting that
var output = String(inputValue)

// and now, our feature presentation :(

if (((inputValue % 3) === 0) && ((inputValue % 5) === 0))
{
    output = "JavaScript"
}
else
{
    if ((inputValue % 3) === 0)
    {
        output = "Java"
    }
    else
    {
        if ((inputValue % 5) === 0)
        {
            output = "Script"
        }
    }
}

console.log(output)
