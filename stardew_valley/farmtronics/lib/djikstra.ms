// *****************************************************************************
// * Stupid Djikstra implementations
// *
// * I'm sure they're terrible. Don't at me, bruh.
// *
// * by greysondn @ github
// *****************************************************************************

// Magic Keys

// ".L"       - means to turn 90 degrees counter-clockwise
// ".R"       - means to turn 90 degrees clockwise
// ".F"       - means to move forwards
// ".B"       - means to move back
// ".U"       - means to use item in hand
// "E+ term"  - means to equip something matching term
// "E0"       - means to equip slot 0
// "E1"       - means to equip slot 1
// "E2"       - means to equip slot 2
// "E3"       - means to equip slot 3
// "E4"       - means to equip slot 4
// "E5"       - means to equip slot 5
// "E6"       - means to equip slot 6
// "E7"       - means to equip slot 7
// "E8"       - means to equip slot 8
// "E9"       - means to equip slot 9
// "EA"       - means to equip slot 10
// "EB"       - means to equip slot 11
// "EH"       - means to equip a hoe
// "EX"       - means to equip an axe
// "EP"       - means to equip a pickaxe
// "ES"       - means to equip a scythe
// "EW"       - means to equip a watering can
// "TN"       - means that the next move should be to turn north
// "TE"       - means that the next move should be to turn east
// "TW"       - means that the next move should be to turn west
// "TS"       - means that the next move should be to turn south
// "MN"       - means that the next move should be north
// "MS"       - means that the next move should be south
// "ME"       - means that the next move should be east
// "MW"       - means that the next move should be w
// "XW"       - means that no work was found


// **
// * Tiles for our implementation.
// *
// * As our pathing can only really do north, south, east, and west, we only ever
// * need to worry about those four directions.
// *
DTile = {}

DTile.x = {}
DTile.y = {}

DTile.visited = False
DTile.parent  = "" 

DTile.directionFromParent = ""
DTile.type                = ""
DTile.passable            = False
DTile.mineable            = False
DTile.axeable             = False
DTile.waterable           = False
DTile.waterSource         = False

DTile.isWork              = False
DTile.hasWorker           = False

DTile.setDirectionFromParent = function(parent)
    if (parent.x < DTile.x) then
        DTile.directionFromParent = "E"
    else if parent.x > DTile.x then
        DTile.directionFromParent = "W"
    else if parent.y < DTile.y then
        DTile.directionFromParent = "S"
    else if parent.y > DTile.y then
        DTile.directionFromParent = "N"
    else
        print "WHAT?!?"
    end if
end function

DTile.reset = function
    DTile.visited = False
    DTile.parent  = DTile 

    DTile.directionFromParent = ""
    DTile.type                = ""
    DTile.passable            = False
    DTile.mineable            = False
    DTile.axeable             = False
    DTile.waterable           = False
    DTile.scytheable          = False
    DTile.isWaterSource       = False

    DTile.isWork              = False
    DTile.hasWorker           = False
end function

DTile.setFromGameTile = function (aTile)
        // examples...
        //
        // fully grown maple tree
        // name: Tree
        // type: Tree
        // treeType: 2
        // growthStage: 7
        // health: 10
        // stump: 0
        // tapped: 0
        // hasSeed: 0
        //
        // fully grown pine tree
        // name: Tree
        // type: Tree
        // treeType: 3
        // growthStage: 5
        // health: 2
        // stump: 0
        // tapped: 0
        // hasSeed: 0
        //
        // tile with crop
        // name: HoeDirt
        // type: HoeDirt
        // dry: 0
        // crop:
        //      phase:          3
        //      maxPhase:       4
        //      mature:         0
        //      dead:           0
        //      harvestMethod:  0
        //      harvestable:    0
        //      name:           Parsnip
    if (aTile == null) then
        // usually passable/blank ground
        // can be the shipping crate, though
        DTile.passable = True
    else if (aTile.type == "Basic") then
        if (aTile.name == "Weeds") then
            // single tile trash plant on map
            DTile.passable   = False
            DTile.isWork     = True
            DTile.mineable   = True
            DTile.scytheable = True
            DTile.axeable    = True
        end if
    else if (aTile.type == "Building") then
        if (aTile.name == "Building") then
            // cliff face
            // farmhouse
            // minecart
            DTile.passable = False
            DTile.isWork   = False
        end if
    else if (aTile.type == "Bush") then
        if (aTile.name == "Bush") then
            // permanent plant on map
            DTile.passable = False
            DTile.isWork   = False
        end if
    else if (aTile.type == "Clump") then
        if (aTile.name == "Boulder") then
            // hard stone
            DTile.passable = False
            DTile.isWork   = False
        else if (aTile.name == "Stump") then
            // hard wood stump
            DTile.passable = False
            DTile.isWork   = False
        end if
        
    else if (aTile.type == "Crafting") then
        if (aTile.name == "Twig") then
            // garbage/litter twig
            DTile.passable = False
            DTile.axeable  = True
            DTile.isWork   = True
        end if
    else if (aTile.type == "Flooring") then
        if (aTile.name == "Flooring") then
            // Stone walkway at least
            DTile.passable = True
            DTile.isWork   = False
        end if
    else if (aTile.type == "Grass") then
        if (aTile.name == "Grass") then
            // hay grass
            DTile.passable   = True
            DTile.scytheable = True
            DTile.isWork     = True
        end if
    else if (aTile.type == "Property") then
        if (aTile.name == "Water") then
            // pond
            DTile.passable      = False
            DTile.isWork        = False
            DTile.isWaterSource = True
        end if
    else if (aTile.type == "Stone") then
        if (aTile.name == "Stone") then
            // single tile rock on map
            DTile.passable      = False
            DTile.isWork        = True
            DTile.mineable      = True
        end if
    else if (aTile.type == "Tree") then
        // TODO: Sort out trees
        DTile.passable = False
    else
        // just for safe measure for now
        // nature only knows what could be destroyed accidentally
        DTile.passable = False
        DTile.isWork   = False
    end if
end function

DTile.updateForBot = function(aBot)
    // pass
end function

/**
 * Map for our implementation.
 *
 * Importantly, this is essentially a copy of all the data that matters from the
 * main game map. Caching this may be wise, but the current implementation is
 * very naive.
 */
DMap = {}

DMap.width  = 0
DMap.height = 0

DMap.tiles = [] // this should be 2d, you know

DMap.getTile = function(x, y)
    return DMap.tiles[x][y]
end function

DMap.reset = function
    for x in range(0, DMap.width)
        for y in range(0, DMap.height)
            DMap.tiles[x][y].reset()
        end for
    end for
end function

DMap.getNearestWorkTo = function(x, y)
    foundWork = False
    ret = []
    checkQueue = [DMap.getTile(x, y)]
    
    // essentially, we floodfill out while maintaining our parent ordering
    // then we'll find the nearest work and be able to route it
    while (not foundWork)
        if (checkQueue.len() > 0) then
            currentTile = checkQueue.pull()
            currentTile.visited = True
            
            if (currentTile.isWork) then
                // done
                foundWork = True
                swpPath = []
                swpTile = currentTile
                
                // unpack parentage
                while (swpTile.parent != swpTile):
                    swpPath.push(swpTile.directionFromParent)
                    swpTile = swpTile.parent
                end while
                
                // reverse
                while (swpPath.len() > 0)
                    ret.push(swpPath.pop())
                end while
                
            else if (currentTile.passable) then
                // we can at least move through it

                // add adjacent tiles
                if ((currentTile.y - 1) >= 0) then
                    swp = DMap.getTile(currentTile.x, currentTile.y - 1)

                    if (not swp.visited) then
                        swp.setDirectionFromParent(currentTile)
                        checkQueue.push(swp)
                    endif
                endif
                
                if ((currentTile.x + 1) < DMap.width) then
                    swp = DMap.getTile(currentTile.x + 1, currentTile.y)

                    if (not swp.visited) then
                        swp.setDirectionFromParent(currentTile)
                        checkQueue.push(swp)
                    endif
                endif

                if ((currentTile.y + 1) < DMap.height) then
                    swp = DMap.getTile(currentTile.x, currentTile.y + 1)

                    if (not swp.visited) then
                        swp.setDirectionFromParent(currentTile)
                        checkQueue.push(swp)
                    endif
                endif
                
                if ((currentTile.x - 1) >= 0) then
                    swp = DMap.getTile(currentTile.x - 1, currentTile.y)

                    if (not swp.visited) then
                        swp.setDirectionFromParent(currentTile)
                        checkQueue.push(swp)
                    endif
                endif
            end if
        else
            foundWork = True
            ret.push("NO_WORK")
        end if
        
    end while
    
    return ret
end function