// -----------------------------------------------------------------------------
// an implementation of some terminal drawing functionality.
//
// ref:
// http://www.roguebasin.com/index.php/Java_Curses_Implementation
//
// greysondn@github
// -----------------------------------------------------------------------------

// we need some tools
globalimport "greysondn.constants"

constants  = globals.dot_get("greysondn.constants")

// eventual return
ret = {}

// data about the cursor
cursor = {
    "fgColor" : text.color,
    "bgColor" : text.backColor,
}

// constants (geometry)
CONSOLE_X = 40
CONSOLE_Y = 20

// proper CLS requires us to draw the entire screen
ret.cls = function()
    // stub/pass
end function

ret.setCursor = function(color)
    // stub/pass
end function

ret.moveCursor = function(x, y)
    // stub/pass
end function

ret.print = function(ch)
    // stub/pass
end function

ret.getch = function()
    // stub/pass
end function

// 