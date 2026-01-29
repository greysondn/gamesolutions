This script manages the mines by itself.

import string
-------------

```
rVNbasNADLzL/tYsdpNCCf3oAdoT1KYoG9kRtrVmJRNCyN3LOrgExwGH9mcQ7I40o8fJiAvUqZjN18mAU/IcY5OHxjtoLLFaQc23zrMosOZ9mqbrfOsDfuuxw8nL84DpLZrExCBbHXyoMYgFEarYMrTTHOsBSwWpbUuMdheoaZYWmk328kmMIWooK2QM5OwBaGprdTfnBLPX94f86K+X675WD/R1aiOWzq6t9KzUXFywv3BwaN4e5AOOGCTSFk914EMg3beo5CLjb9Kzp9kBZnc3JcXRXuXVUzlLX9+ZEjrfdhBIPP+D9Leb2uW87PJa8mK/RWKc5x2Nx1ckhtqubwSHUzxAjX0Xf8XdMhtTBTyK5x3bcR06cDVU8c2ci/MP
```

Script
------

```
; -----------------------------------------------------------------------------
; greysondn.Miner
; made to handle the mines (naturally)
; anyway, enjoy that
;
; Name workers "Miner" to have them assigned to the task
; -----------------------------------------------------------------------------

:name greysondn.Miner
:local int ore_type

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
    wait(6.0) ; sleep long enough to be sure we did it

; -----------------------------------------------------------------------------
; 1st floor - ore mining process
;
; This is the first floor of the mines
; You are expected to still trade in manually if you want that
; -----------------------------------------------------------------------------
mine_ore:
    worker.assignName("task.mine", ore_type, "Miner")
    waituntil(not(hasLayers()))
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
[ ] Set up a global for worker speed and calculate a single layer from it
[ ] The entire second floor
