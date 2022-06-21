// imports
globalimport "greysondn.constants"

// aliases
constants  = globals.dot_get("greysondn.constants")
DIR = constants.DIRECTION

// -----------------------------------------------------------------------------
// greysondn's bot extensions and overrides
// because they're not that great, let's be real
// -----------------------------------------------------------------------------

// bots need a move queue, right?
bot.moveQueue = []

// turn to face a certain direction
bot.turnToFace = function(direction)
    while (bot.facing != direction)
        // so the facings are actually integers
        // which means we can do...
        if (((bot.facing + 1) % 4) == direction) then
            bot.right()
        else
            bot.left()
        end if
    end while
end function

// find nearest work to do
bot.findWork = function
    // pass
end function

// plan routing
bot.route = function(x, y)
    startX = bot.position.x
    startY = bot.position.y
    maxX   = bot.area.position.width
    maxY   = bot.area.position.height
end function

// and now just doing the next move
bot.doNextMove = function
    if (bot.moveQueue.len() > 0) then
        nMove = bot.moveQueue.pull()
        
        // TODO: Do anything with queue here.
    end if
end function


// the bot needs to be able to tick
bot.tick = function
    if (bot.moveQueue.len() == 0) then
    
    end if
end function

// -----------------------------------------------------------------------------
// greysondn's temporary, awful functions
// -----------------------------------------------------------------------------

// probably similar to or same as his clearrect but I wrote it myself so whatever.
bot.clearArea = function(width, height)
    bot.turnToFace(EAST)
    
    for y in range(0, height)
        for x in range(0, width)
            if (bot.energy > 0) then
                bot.clearAndMove(1)
            end if
        end for
        if (bot.energy > 0) then
            if ((y % 2) == 0) then
                bot.turnToFace(DIR.SOUTH)
                bot.clearAndMove(1)
                bot.turnToFace(DIR.WEST)
            else
                bot.turnToFace(DIR.SOUTH)
                bot.clearAndMove(1)
                bot.turnToFace(DIR.EAST)
            end if
        end if
    end for
end function

// helper function so I don't have to remember this nonsense
bot.examine = function()
    pprint(farm.tile(bot.position.x+1, bot.position.y))
end function

// return a map just to make this happy
return {"imported": true}