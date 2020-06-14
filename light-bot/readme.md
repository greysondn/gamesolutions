Light Bot
---------

A game where you program a robot. AFAIK there's 12 stages.

https://www.kongregate.com/games/Coolio_Niato/light-bot

I've tried to make these as clean as possible. I might do some playaround ones
later.

Operators
---------

The language is comprised of 7 operators. I've written it with 8 operators. In
order on the screen, they are:

```
F - Forward
R - Rotate Right
L - Rotate Left
J - Jump
C - Light ("color")
1 - Function 1
2 - Function 2

And I've added, for consistency:
0 - NOP / Empty cell
```

Programs
--------

Programs are arranged into three functions - a main function with 12 operations
and two functions (function 1 and function 2) with 8 operations a piece. The
program's execution starts with the first operation in main and ends when there
is not another operation to queue from the program's code. (Due to the lack of
conditional execution, this means that recursion doesn't seem to be viable.)

Operations are displayed in rows of four functions. The initial program state
before anything is entered looks like this:

```
Main:
[0][0][0][0]
[0][0][0][0]
[0][0][0][0]

Func 1:
[0][0][0][0]
[0][0][0][0]

Func 2:
[0][0][0][0]
[0][0][0][0]
```

This Folder
-----------

I've written these as basic markdown files. So enjoy!
