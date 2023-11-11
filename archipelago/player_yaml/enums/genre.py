from enum import IntEnum

class Genre(IntEnum):
    IMPLEMENTED                 = 2 **  10
    PLEASE_NO                   = 2 **   9
    
    FARMING_SIMULATOR           = 2 **   8
    FIRST_PERSON_SHOOTER        = 2 **   0
    PLATFORMER                  = 2 **   1
    PUZZLE                      = 2 **   2
    ROGUELITE                   = 2 **   3
    SHOOTER                     = 2 **   4
    RPG                         = 2 **   5
    THIRD_PERSON_SHOOTER        = 2 **   7
    WALKING_SIMULATOR           = 2 **   6