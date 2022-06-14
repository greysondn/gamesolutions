if (bot) then
    import "greysondn_bot"
    import "joestrout_bot"
end if

import "greysondn_location"

import "textUtil"

// -----------------------------------------------------------------------------
// A very simple custom bootrom for the sake of my own sanity
// Mostly sets up everything I care about and prints conf data
// -----------------------------------------------------------------------------


// ****************************
// replacement: cd
// ****************************

_cd = @cd

cd = function(dirPath="")
    _cd(dirPath)
    prefix = "com"
    
    if (bot) then
        prefix = "bot"
    end if
    
    endPath = pwd
    
    if (endPath.len > 0) then
        if (endPath[endPath.len - 1] != "/") then
            endPath = endPath + "/"
        end if 
    else
        endPath = endPath + "/"
    end if
    
    env.prompt = prefix + ":" + endPath + "> "
end function

// *******************
// extra globals
// *******************

// permit us to reboot the system... but not really.
// just reloads the bootrom.
globals.reboot = function
    import "greysondn_bootrom"
end function

// ls as alternative to dir
globals.ls = function(dirPath=null)
    if (not dirPath) then
        dirPath = pwd
    end if
    
    strt = pwd
    _cd(dirPath)
    dir
    _cd(strt)
end function

// cls as alternative to clear
globals.cls = function()
    clear
end function

// ***************
// actual bootrom
// ***************

_bootrom = {}

// configure things here at boot
_bootrom.bootconf = function
    text.color = color.silver
    text.backColor = color.black
    env.morePrompt = " .... > "
end function

// and so on
_bootrom.drawEmptyScreen = function()
    for y in range(1, 20)
        print ("                                        ")
    end for
end function

_bootrom.drawBlock = function(x, y, aColor)
    prevBackcolor = text.backColor
    
    text.row    = 19 - y
    text.column = x
    text.backColor = aColor
    textUtil.printNoCR(" ")
    
    text.backColor = prevBackcolor
end function

_bootrom.flashFullScreen = function(aColor)
    prevBackcolor = text.backColor
    
    clear
    text.backColor = aColor
    _bootrom.drawEmptyScreen()
    wait(0.25)
    
    text.backColor = prevBackcolor
end function

_bootrom.drawFilledBox = function(fromX, fromY, toX, toY, aColor)
    prevBackcolor = text.backColor
    
    for x in range(fromX, toX)
        for y in range(fromY, toY)
            _bootrom.drawBlock(x, y, aColor)
        end for
    end for
    
    text.backColor = prevBackcolor
end function

_bootrom.drawHollowBox = function(fromX, fromY, toX, toY, aColor)
    prevBackcolor = text.backColor
    
    // first row
    _bootrom.drawFilledBox(fromX, fromY, toX, fromY, aColor)
    
    // second row
    _bootrom.drawFilledBox(fromX, toY, toX, toY, aColor)
    
    // first column
    _bootrom.drawFilledBox(fromX, fromY, fromX, toY, aColor)
    
    // second column
    _bootrom.drawFilledBox(toX, fromY, toX, toY, aColor)
    
    text.backColor = prevBackcolor
end function

_bootrom.writeText = function(x, y, fg, bg, txt)
    prevBackcolor = text.backColor
    prevTextcolor = text.color
    
    text.color = fg
    text.backColor = bg
    
    text.row    = 19 - y
    text.column = x
    
    textUtil.printNoCR(txt)
    
    text.backColor = prevBackcolor
    text.color = prevTextcolor
end function

_bootrom.writeTextWithDelay = function(ts, x, y, fg, bg, txt)
    wait(ts)
    _bootrom.writeText(x, y, fg, bg, txt)
end function


// give us a nice bootsplash
_bootrom.bootsplash = function()

    hn = "unknown"
    
    if (version.hostName =="Farmtronics Home Computer") then
        hn = "Home Comp"
    end if

    if (bot) then
        hn = "Bot"
    end if


    splashTextColor = color.white
    
    _bootrom.flashFullScreen(color.black)
    _bootrom.flashFullScreen(color.gray)
    _bootrom.flashFullScreen(color.black)
    _bootrom.flashFullScreen(color.navy)

    wait(1)
    _bootrom.drawFilledBox(1, 1, 38, 18, color.blue)
    
    wait(1)
    _bootrom.drawFilledBox(1, 1, 38, 1, color.black)
    
    
    
    _bootrom.writeTextWithDelay(1, 8, 1, splashTextColor, color.black, "GDN Farmtronic Bootrom")
    
    _bootrom.writeTextWithDelay(1, 3,  3, splashTextColor, color.blue, "miniscript")
    _bootrom.writeTextWithDelay(1, 5,  4, splashTextColor, color.blue, ("version    : " + version.miniscript))
    _bootrom.writeTextWithDelay(1, 5,  5, splashTextColor, color.blue, ("build date : " + version.buildDate))
    _bootrom.writeTextWithDelay(1, 5,  6, splashTextColor, color.blue, ("host       : " + version.host))
    _bootrom.writeTextWithDelay(1, 5,  7, splashTextColor, color.blue, ("env        : " + "Farmtronics"))
    _bootrom.writeTextWithDelay(1, 5,  8, splashTextColor, color.blue, ("             " + hn))
    
    _bootrom.writeTextWithDelay(1, 3, 10, splashTextColor, color.blue, ("extra libs"))
    
    exLibs = false
    nextRow = 11
    
    if (bot) then
        exLibs = true
        _bootrom.writeTextWithDelay(1, 5, nextRow, splashTextColor, color.blue, ("bot"))
        nextRow = nextRow + 1
    end if
    
    if (not exLibs) then
        _bootrom.writeTextWithDelay(1, 5, nextRow, splashTextColor, color.blue, ("none found"))
    end if
    
    wait(1)
    _bootrom.drawFilledBox(1, 18, 38, 18, color.black)
    
    if (bot) then
        _bootrom.writeTextWithDelay(1,  5, 18, splashTextColor, color.black, "Automatically starting in 9")
        _bootrom.writeTextWithDelay(1, 31, 18, splashTextColor, color.black, "8")
        _bootrom.writeTextWithDelay(1, 31, 18, splashTextColor, color.black, "7")
        _bootrom.writeTextWithDelay(1, 31, 18, splashTextColor, color.black, "6")
        _bootrom.writeTextWithDelay(1, 31, 18, splashTextColor, color.black, "5")
        _bootrom.writeTextWithDelay(1, 31, 18, splashTextColor, color.black, "4")
        _bootrom.writeTextWithDelay(1, 31, 18, splashTextColor, color.black, "3")
        _bootrom.writeTextWithDelay(1, 31, 18, splashTextColor, color.black, "2")
        _bootrom.writeTextWithDelay(1, 31, 18, splashTextColor, color.black, "1")
        wait(1)
    else
        _bootrom.writeTextWithDelay(1, 5, 18, splashTextColor, color.black, "Press any key to load prompt")
        key.get()
    end if

end function

_bootrom.bootconf()
// _bootrom.bootsplash()
// clear