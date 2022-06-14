import "greysondn_constants"

// aliases
constants  = greysondn_constants
DIR        = constants.DIRECTION
NAME       = constants.TILE.NAME
SHORT_TYPE = constants.TILE.SHORT_TYPE
STATUS     = constants.STATUS
TYPE       = constants.TILE.TYPE

// -----------------------------------------------------------------------------
// some tile extensions
// ... why isn't there a proper type so this is extensible? But really?
// -----------------------------------------------------------------------------
Tile = {}

//
// same as default, just always exist now
//
Tile.type               = null
Tile.name               = null
Tile.dry                = null
Tile.displayName        = null
Tile.health             = null
Tile.quality            = null
Tile.harvestable        = null
Tile.minutesTillReady   = null
Tile.value              = null
Tile.description        = null
Tile.treeType           = null
Tile.growthStage        = null
Tile.stump              = null
Tile.tapped             = null
Tile.hasSeed            = null
Tile.crop               = null // this would normally be a dict


//
// new
//

// tile coordinates on native map
Tile.x = 0
Tile.y = 0

// tile's map
Tile.map = null

// tile's shortened type
Tile.shortType = null

// pathfinding: is this a valid target?
Tile.isPathfindingTarget = false

// pathfinding: have we visited this during our attempt?
Tile.visited = false

// pathfinding: what tile came before this?
Tile.parent = null

// pathfinding: what tile comes after this?
Tile.next = null

// pathfinding: what direction is it to our next tile?
Tile.dirToNext = null

// pathfinding: sometimes useful flags
Tile.passable       = false // may not always be right, oh no
Tile.mineable_easy  = false
Tile.mineable_hard  = false
Tile.choppable_easy = false
Tile.choppable_hard = false
Tile.waterable      = false
Tile.waterSource    = false

// let's set up constants for the tile type
Tile.typeToConstant = function(self, name, type)
    ret = STATUS.TYPE_UNKNOWN
end function

Tile.updatePassableFromShortType = function(self)
    // pass
end function