// TwilioQuest 3.1.26
// Works in:
//   - 3.1.26
//
// Fun fact: I walk into this good at Python, but terrible at JS.
// Let's see if basic competency can be established just using
// TwilioQuest and what I already know from Python/C++
//
const lifeStatus = Number(process.argv[2])

if (lifeStatus === 0)
{
    console.log("alive")
}
else if (lifeStatus == 1)
{
    console.log("flowering")
}
else if (lifeStatus == 2)
{
    console.log("shedding")
}
else
{
    console.log("other")
}
