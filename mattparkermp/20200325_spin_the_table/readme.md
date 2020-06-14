Given a table of 7 people, find a configuration where you can set number packets
in order on the table and yet not have more than 1 match to people sitting at
seats by rotation of the table itself.

Imagine the table as a list. Imagine the place settings as a list. If they both
matched perfectly, it would look like this:

```
Table:  0, 1, 2, 3, 4, 5, 6
People: 0, 1, 2, 3, 4, 5, 6
```
The people cannot be rotated, and the people may sit in random order. The table
can be rotated, however.

--------------------------------------------------------------------------------

Parker offers an open problem, which is to describe a formula for the worst case
given some number of people at the correct seats to start at tables of arbitrary
sizes.

```
Table 1
Must always match

Table 2
If it starts with any matches, it must have 2 matches

Table 3

