Sets up globals for other scripts

import string
-------------

```
fY5BCoMwEEXvMmuRSEsXbnqQKiUmgwTjTMgkiIh36V16sWKKmy66eXw+b/E2EBNdSALtYwNtkmM6NnRZqaYZPQ/a15bz4LEWTN1gmCRpSoegrkW7jRFXYbJULxwnjE8JiPbHvRSq/3y/7tBXYJisO1v6CtwcshcsZYueMIfDIj0jtPCNFKggaDPpsXxnEez9/gE=
```

Script
------

```
; -----------------------------------------------------------------------------
; globals
; @author greysondn
;
; made to set up globals for other scripts
;
; Remember to run this early as possible, and to configure the values in it
; -----------------------------------------------------------------------------

:name greysondn:globals
:global double greysondn.worker_speed

; -----------------------------------------------------------------------------
; start impulse and conditions
; -----------------------------------------------------------------------------
wakeup() ; when facility ai is turned on

; -----------------------------------------------------------------------------
; Set this to how fast your workers work.
; default: Max worker speed "Very Fast" (0.5)
; -----------------------------------------------------------------------------
gds("greysondn.worker_speed", 0.5)
```

TODO
----

N/A
