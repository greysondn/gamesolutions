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
STATUS.TYPE_UNKNOWN = "XT"

// tile
TILE = {}

// tile.name
TILE.NAME = {}

TILE.NAME.ARTIFACT_SPOT     = "Artifact Spot"
TILE.NAME.BOULDER           = "Boulder"
TILE.NAME.BUILDING          = "Building"
TILE.NAME.BUSH              = "Bush"
TILE.NAME.CHEST             = "Chest"
TILE.NAME.FLOORING          = "Flooring"
TILE.NAME.GRASS             = "Grass"
TILE.NAME.HOE_DIRT          = "HoeDirt"
TILE.NAME.HOLLOW_LOG        = "Hollow Log"
TILE.NAME.SCARECROW         = "Scarecrow"
TILE.NAME.STONE             = "Stone"
TILE.NAME.STUMP             = "Stump"
TILE.NAME.TREE              = "Tree"
TILE.NAME.TWIG              = "Twig"
TILE.NAME.WATER             = "Water"
TILE.NAME.WEEDS             = "Weeds"
TILE.NAME.WOOD_SIGN         = "Wood Sign"
TILE.NAME.WOODEN_PET_BOWL   = "Wooden Pet Bowl"


// tile.type
TILE.TYPE ={}

TILE.TYPE.ARTIFACT_SPOT     = "Artifact Spot"
TILE.TYPE.BASIC             = "Basic"
TILE.TYPE.BUSH              = "Bush"
TILE.TYPE.BUILDING          = "Building"
TILE.TYPE.CHARACTER         = "Character"
TILE.TYPE.CLUMP             = "Clump"
TILE.TYPE.CRAFTING          = "Crafting"
TILE.TYPE.FLOORING          = "Flooring"
TILE.TYPE.GRASS             = "Grass"
TILE.TYPE.HOE_DIRT          = "HoeDirt"
TILE.TYPE.PROPERTY          = "Property"
TILE.TYPE.STONE             = "Stone"
TILE.TYPE.TREE              = "Tree"


// tile.short_type
TILE.SHORT_TYPE = {}

// I had to list my shorthands out to stop conflicting
// I am not proud of it
//
// CG
// CT
// E?
// GH
// HS
// HW
// SA
// SB
// SC
// SD
// SF
// SP
// SS
// RA
// RW
// TS
// TT
// TW

TILE.SHORT_TYPE.ARTIFACT_SPOT       = "TILE_RA" // resource artifact
TILE.SHORT_TYPE.BUSH                = "TILE_SB" // structure bush
TILE.SHORT_TYPE.CHARACTER           = "TILE_E?" // entity unknown
TILE.SHORT_TYPE.CHEST               = "TILE_SA" // Structure chest (c was in use)
TILE.SHORT_TYPE.FLOORING            = "TILE_SF" // structure flooring
TILE.SHORT_TYPE.GRASS               = "TILE_CG" // crop grass
TILE.SHORT_TYPE.HARD_STONE          = "TILE_HS" // hard stone
TILE.SHORT_TYPE.HARD_WOOD           = "TILE_HW" // hard wood
TILE.SHORT_TYPE.HOE_DIRT            = "TILE_GH" // ground hoe
TILE.SHORT_TYPE.PET_BOWL            = "TILE_SD" // structure bowl (B was in use)
TILE.SHORT_TYPE.PERMANENT_STRUCTURE = "TILE_SP" // structure permanent
TILE.SHORT_TYPE.SCARECROW           = "TILE_SC" // structure Crow/"S.carec.row"
TILE.SHORT_TYPE.SIGN                = "TILE_SS" // structure sign
TILE.SHORT_TYPE.STONE               = "TILE_TS" // trash stone
TILE.SHORT_TYPE.TREE                = "TILE_CT" // crop tree
TILE.SHORT_TYPE.TWIG                = "TILE_TT" // trash twig
TILE.SHORT_TYPE.WATER               = "TILE_RW" // resource water
TILE.SHORT_TYPE.WEEDS               = "TILE_TW" // trash weeds

// Helper function
TILE.typeToConstant = function (typeString, nameString)
    ret = STATUS.TYPE_UNKNOWN

    if (typeString == TILE.TYPE.ARTIFACT_SPOT) then
        if (nameString == TILE.NAME.ARTIFACT_SPOT) then
            ret = TILE.SHORT_TYPE.ARTIFACT_SPOT
        end if
    end if

    if (typeString == TILE.TYPE.BASIC) then
        if (nameString == TILE.NAME.STONE) then
            ret = TILE.SHORT_TYPE.STONE
        else if (nameString == TILE.NAME.WEEDS) then
            ret = TILE.SHORT_TYPE.WEEDS
        end if
    end if
    
    if (typeString == TILE.TYPE.BUILDING) then
        if (nameString == TILE.NAME.BUILDING) then
            ret = TILE.SHORT_TYPE.PERMANENT_STRUCTURE
        end if
    end if

    if (typeString == TILE.TYPE.BUSH) then
        if (nameString == TILE.NAME.BUSH) then
            ret = TILE.SHORT_TYPE.BUSH
        end if
    end if

    if (typeString == TILE.TYPE.CHARACTER) then
            // not a typo
            ret = TILE.SHORT_TYPE.CHARACTER
    end if

    if (typeString == TILE.TYPE.CLUMP) then
        if (nameString == TILE.NAME.BOULDER) then
            ret = TILE.SHORT_TYPE.HARD_STONE
        else if (nameString == TILE.NAME.HOLLOW_LOG) then
            ret = TILE.SHORT_TYPE.HARD_WOOD
        else if (nameString == TILE.NAME.STUMP) then
            ret = TILE.SHORT_TYPE.HARD_WOOD
        end if
    end if

    if (typeString == TILE.TYPE.CRAFTING) then
        if (nameString == TILE.NAME.CHEST) then
            ret = TILE.SHORT_TYPE.CHEST
        else if (nameString == TILE.NAME.SCARECROW) then
            ret = TILE.SHORT_TYPE.SCARECROW
        else if (nameString == TILE.NAME.TWIG) then
            ret = TILE.SHORT_TYPE.TWIG
        else if (nameString == TILE.NAME.WOOD_SIGN) then
            ret = TILE.SHORT_TYPE.SIGN
        else if (nameString == TILE.NAME.WOODEN_PET_BOWL) then
            ret = TILE.SHORT_TYPE.PET_BOWL
        end if
    end if

    if (typeString == TILE.TYPE.FLOORING) then
        if (nameString == TILE.NAME.FLOORING) then
            ret = TILE.SHORT_TYPE.FLOORING
        end if
    end if

    if (typeString == TILE.TYPE.GRASS) then
        if (nameString == TILE.NAME.GRASS) then
            ret = TILE.SHORT_TYPE.GRASS
        end if
    end if

    if (typeString == TILE.TYPE.HOE_DIRT) then
        if (nameString == TILE.NAME.HOE_DIRT) then
            ret = TILE.SHORT_TYPE.HOE_DIRT
        end if
    end if

    if (typeString == TILE.TYPE.PROPERTY) then
        if (nameString == TILE.NAME.WATER) then
            ret = TILE.SHORT_TYPE.WATER
        end if
    end if

    if (typeString == TILE.TYPE.STONE) then
        if (nameString == TILE.NAME.STONE) then
            ret = TILE.SHORT_TYPE.STONE
        end if
    end if

    if (typeString == TILE.TYPE.TREE) then
        if (nameString == TILE.NAME.TREE) then
            ret = TILE.SHORT_TYPE.TREE
        end if
    end if

    return ret
end function

// create return for module specifically so that we can manipulate it
moduleRet = {}

moduleRet.ACTION    = ACTION
moduleRet.DIRECTION = DIRECTION
moduleRet.EQUIP     = EQUIP
moduleRet.STATUS    = STATUS
moduleRet.TILE      = TILE
moduleRet.TURTLE    = TURTLE

return moduleRet