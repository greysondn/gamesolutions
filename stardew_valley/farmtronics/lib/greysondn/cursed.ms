// -----------------------------------------------------------------------------
// an implementation of some terminal drawing functionality.
//
// ref:
// http://www.roguebasin.com/index.php/Java_Curses_Implementation
//
// greysondn @ github
// -----------------------------------------------------------------------------

// we need some tools
globalimport "greysondn.constants"
globalimport "textUtil"

constants  = globals.dot_get("greysondn.constants")

// constants (geometry)
CONSOLE_X = 40
CONSOLE_Y = 20

// eventual return
ret = {}

// data about the cursor and a few utils
cursor = {}

cursor.fgColor = text.color
cursor.bgColor = text.backColor
cursor.x       = text.column
cursor.y       = CONSOLE_Y - (1 + text.row)

cursor.set_x = function(val)
    // clamp
    if (val >= CONSOLE_X) then
        val = CONSOLE_X - 1
    end if
    
    if (val < 0) then
        val = 0
    end if
    
    // set
    cursor.x = val
end function

cursor.set_y = function(val)
    // clamp
    if (val >= CONSOLE_Y) then
        val = CONSOLE_Y - 1
    end if
    
    if (val < 0) then
        val = 0
    end if
    
    // set
    cursor.y = val
end function

cursor.invertX = function()
    return CONSOLE_X - (1 + cursor.x)
end function

cursor.invertY = function()
    return CONSOLE_Y - (1 + cursor.y)
end function

cursor.write = function(val)
    oldcol = text.column
    oldrow = text.row
    oldfg = text.color
    oldbg = text.backColor


    text.column = cursor.x
    text.row    = cursor.invertY()
    
    text.color = cursor.fgColor
    text.backColor = cursor.bgColor
    
    textUtil.printNoCR(val)
    
    text.column = oldcol
    text.row = oldrow
    text.color = oldfg
    text.backColor = oldbg
end function

ret.moveCursor = function(x, y)
    cursor.set_x(x)
    cursor.set_y(y)
end function

// proper CLS requires us to draw the entire screen
ret.cls = function()
    for x in range(0, CONSOLE_X - 1)
        for y in range(0, CONSOLE_Y - 1)
            ret.moveCursor(cursor.x, cursor.y)
            cursor.write("p")
        end for
    end for
end function

ret.print = function(ch)
    cursor.write(ch)
end function

return ret