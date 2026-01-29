This script manages the mines by itself.

requires
--------

[globals](globals.md) - uses variables from there

import string
-------------

```
1VRLbsMgEL0Ly9ZCduN2EVVqL9AT1FGE8ZiOjAcEWFEU5V7d92IVzkdWgqVU7aabEQzD8N7jwY556dAGz5bvOyZkQENxzCqnjRSaIwXuIVS1NOSDoFANeZ6XVW0crMPWwsXKwxjz68gyFgfFYmNcB85z4T0q4iT6yx7lGNsgfMd7JOCNQ61vPSjZ7PENCVzE0CogcCj5RuBYURTCYfjoIaDkjRlqDYe00qYW+pjiKiFCLHtSDrbeUEP8wGztLUCTRFHcXaQXsyQm8evz5UfihbNw00tM4Z+7xP+vWfkacd/s4TiHCSWk8DvtivukXYvZd5HDSWNlgsE2ub2coQvS9FY49Ib+APrz1dltGnY7hXwz31XGpKEGT1/NKmPY20F7GD+ejehgsLEqmpstWX90oRWyEypmzu5h+9X+Gw==
```

Script
------

```
; -----------------------------------------------------------------------------
; miner
; @author greysondn
;
; made to handle the mines (naturally)
; anyway, enjoy that
;
; Name workers "Miner" to have them assigned to the task
; -----------------------------------------------------------------------------

:name greysondn:miner
:global double greysondn.worker_speed
:local  int    ore_type

; -----------------------------------------------------------------------------
; start impulse and conditions
; -----------------------------------------------------------------------------
wakeup() ; when facility ai is turned on

; -----------------------------------------------------------------------------
; script start
; -----------------------------------------------------------------------------
start:
    ore_type = 0

; -----------------------------------------------------------------------------
; 1st floor - drill restart
;
; I consider this a good idea.
; -----------------------------------------------------------------------------
drill_earth:
    worker.assignName("task.mine.drill", 0, "Miner")
    wait(greysondn.worker_speed * 1.5) ; sleep long enough to be sure we did it

; -----------------------------------------------------------------------------
; 1st floor - ore mining process
;
; This is the first floor of the mines
; You are expected to still trade in manually if you want that
; -----------------------------------------------------------------------------
mine_ore:
    worker.assignName("task.mine", ore_type, "Miner")
    wait(greysondn.worker_speed * 20.0) ; enough to generate a layer and mine it out, hopefully
    ore_type += 1
    gotoif(mine_ore, ore_type < 12)

; -----------------------------------------------------------------------------
; 2nd floor - everything
; -----------------------------------------------------------------------------
; TODO

; -----------------------------------------------------------------------------
; restart the script
; -----------------------------------------------------------------------------
goto(start)
```

TODO
----

[ ] Work out why the wait for layers to exhaust isn't working
[x] Set up a global for worker speed and calculate a single layer from it
[ ] The entire second floor
