// -----------------------------------------------------------------------------
// constants
// ... so we can stop slinging magic values around without a reference point
// -----------------------------------------------------------------------------

// actions
ACTION = {}
ACTION.USE_HELD       = "AU"
ACTION.FACE           = "AF"
ACTION.MOVE           = "AM"
ACTION.MOVE_AND_CLEAR = "AC"


// directions are defined as part of bot's values, so don't look at me over
// inconsistency or anything.
DIRECTION = {}
DIRECTION.NORTH = 0
DIRECTION.EAST  = 1
DIRECTION.SOUTH = 2
DIRECTION.WEST  = 3

// keys for turtle movement
TURTLE = {}
TURTLE.LEFT      = "TL"
TURTLE.RIGHT     = "TR"
TURTLE.FORWARDS  = "TF"
TURTLE.BACKWARDS = "TB"

// keys for equipping stuff
EQUIP = {}

EQUIP.SLOT_00 = "E0"
EQUIP.SLOT_01 = "E1"
EQUIP.SLOT_02 = "E2"
EQUIP.SLOT_03 = "E3"
EQUIP.SLOT_04 = "E4"
EQUIP.SLOT_05 = "E5"
EQUIP.SLOT_06 = "E6"
EQUIP.SLOT_07 = "E7"
EQUIP.SLOT_08 = "E8"
EQUIP.SLOT_09 = "E9"
EQUIP.SLOT_10 = "EA"
EQUIP.SLOT_11 = "EB"

EQUIP.TERM    = "E+" // expected to be followed by term in next cell for logic

EQUIP.TOOL_HOE          = "EH" // ostensibly [E+, "Hoe"] 
EQUIP.TOOL_AXE          = "EX" // and so on
EQUIP.TOOL_PICKAXE      = "EP"
EQUIP.TOOL_SCYTHE       = "ES"
EQUIP.TOOL_WATERING_CAN = "EW"

// statuses
STATUS = {}

// errors/negatives
STATUS.NO_WORK = "XW"