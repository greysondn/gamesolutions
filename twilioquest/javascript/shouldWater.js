// TwilioQuest 3.1.26
// Works in:
//   - 3.1.26
//
// Fun fact: I walk into this good at Python, but terrible at JS.
// Let's see if basic competency can be established just using
// TwilioQuest and what I already know from Python/C++
//
const lifeStatus = Number(process.argv[2])
const dryness    = Number(process.argv[3])

if ((lifeStatus === 0) && (dryness > 10))
{
    // I'm so tired, I tried to write this as
    // print("WATER")
    // and then spent ten minutes debugging it.
    // Really thinking maybe I should stick to Python.
    console.log("WATER")
}
