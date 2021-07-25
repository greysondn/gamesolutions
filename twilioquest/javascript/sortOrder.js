// TwilioQuest 3.1.26
// Works in:
//   - 3.1.26
//
// Fun fact: I walk into this good at Python, but terrible at JS.
// Let's see if basic competency can be established just using
// TwilioQuest and what I already know from Python/C++
//
const first = process.argv[2].toLowerCase()
const second = process.argv[3].toLowerCase()

if (first < second)
{
    console.log("-1")
}
else if (first === second)
{
    console.log("0")
}
else
{
    console.log("1")
}
