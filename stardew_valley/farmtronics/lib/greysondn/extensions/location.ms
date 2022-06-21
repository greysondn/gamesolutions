// imports
globalimport "greysondn.constants"
globalimport "greysondn.tile"

// aliases
constants  = globals.dot_get("greysondn.constants")
STATUS = constants.STATUS
SYSTEM = constants.SYSTEM

if ((SYSTEM.CURRENT == SYSTEM.FARMTRONICS_COMPUTER) or (SYSTEM.CURRENT == SYSTEM.FARMTRONICS_BOT)) then
    // -----------------------------------------------------------------------------
    // Extensions to the builtin location class
    // because tiles should be their own class and I want to do pathfinding besides
    // -----------------------------------------------------------------------------

    // we have to protect the user from themselves here, because we're overriding
    // a builtin function
    if (not Location.hasIndex("loaded_gdn_location")) then
        Location.loaded_gdn_location = true
        Location._tile = @Location.tile
    end if

    // redefine builtin tile function
    Location.tile = function(x=0, y=0)
        return self._tile(x, y)
    end function

    // check for unknown tiles
    Location.checkForUnknownTiles = function()
        res = "No unknown tiles found"
        keepLooking = true
        
        for x in range(0, self.width)
            for y in range(0, self.height)
                if (keepLooking) then
                    swp = self.tile(x, y)
                    if (swp) then
                        test = constants.TILE.typeToConstant(swp.type, swp.name)
                        if (test == STATUS.TYPE_UNKNOWN) then
                            keepLooking = false
                            res = swp
                        end if
                    end if
                end if
            end for
        end for
        
        pprint(res)
    end function
end if

return {"imported": true}