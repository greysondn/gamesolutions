// -----------------------------------------------------------------------------
// JoeStrout's functions
// https://github.com/JoeStrout/Farmtronics/wiki/Bot-Code-Examples
// -----------------------------------------------------------------------------


// **
// * tills the tile in front of the bot
// *
bot.till = function
    bot.use "Hoe"
    bot.useTool
end function

// **
// * waters the tile in front of the bot
// *
bot.water = function
    bot.use "Watering Can"
    bot.useTool
end function

// **
// * plants a seed by seedname
// * 
bot.plant = function(seedName)
    bot.use seedName
    bot.placeItem
end function