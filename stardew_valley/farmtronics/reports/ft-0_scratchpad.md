Farmtronic scratchpad
=====================

A scratchpad is just a file to toss useless and/or random notes.

<!-- ####################################################################### -->

Demo: Create Factorial Calculator
---------------------------------

Didn't create factorials calculator
https://discord.com/channels/646000428441534474/910679364335730718/915301832593670216

<!-- ####################################################################### -->

Demo: Create farm map
---------------------

Didn't create farm map
https://discord.com/channels/646000428441534474/910679364335730718/915302069852835860

<!-- ####################################################################### -->

Demo: Create Hangman
--------------------

Didn't create Hangman
https://discord.com/channels/646000428441534474/910679364335730718/915301832593670216

<!-- ####################################################################### -->

Documentation: Make sure /usr/startup.ms is documented
------------------------------------------------------

Seems first mention is:
https://discord.com/channels/646000428441534474/910679364335730718/915314175834726400

<!-- ####################################################################### -->

Documentation: History
----------------------

MiniScript was originally a Unity plugin
https://discord.com/channels/646000428441534474/910679364335730718/931212689173254234

1/13/2022 - farmtronics 1.01
https://discord.com/channels/646000428441534474/910679364335730718/931281274767810570


<!-- ####################################################################### -->

Documentation: Make sure api is documented
-----------------------------------------------

How to poke this:
https://discord.com/channels/646000428441534474/910679364335730718/915407950502301749

> Also added bot.energy, which shows you how much stamina (energy) your bot has left.
https://discord.com/channels/646000428441534474/910679364335730718/929769628668944536

delete file via `file.delete`, owenwilson.gif "wow"
https://discord.com/channels/646000428441534474/910679364335730718/931292342114201652


<!-- ####################################################################### -->

Documentation: Make sure weird tricks are documented
----------------------------------------------------

Files can be edited on-disk outside game:
https://discord.com/channels/646000428441534474/910679364335730718/931302302193692683

Function-in-function:
https://discord.com/channels/646000428441534474/910679364335730718/931211173951598624

<!-- ####################################################################### -->

Documentation: Standard reference style and intent guide
--------------------------------------------------------

Piece: Don't put parens around function args
cf: > So instead of `bot.equip("Hoe")`, please just write `bot.equip "Hoe"`
cf: > It works fine with multiple arguments, too.
https://discord.com/channels/646000428441534474/910679364335730718/920739760551645204
https://discord.com/channels/646000428441534474/910679364335730718/932051626762579989

Piece: Not a kitchen sink
cf: > we take great care in choosing what goes in and what *doesn't* go in
cf: > so it doesn't end up being yet another kitchen-sink environment with a manual 6 inches thick.
https://discord.com/channels/646000428441534474/910679364335730718/931211997893263380

Piece: You NEVER need empty parens in MiniScript
cf: > You never need empty () in MiniScript.
https://discord.com/channels/646000428441534474/910679364335730718/931229896821309532

<!-- ####################################################################### -->

Feature: App For Mobile Phone Mod
---------------------------------

Mentioned: https://discord.com/channels/646000428441534474/910679364335730718/916354395308949514

<!-- ####################################################################### -->

Feature: Mod config file
------------------------

For fuck's sake.

Esentially this here:
https://discord.com/channels/646000428441534474/910679364335730718/928038352790364170

<!-- ####################################################################### -->

Feature: App For Mobile Phone Mod

Mentioned: https://discord.com/channels/646000428441534474/910679364335730718/916354395308949514


<!-- ####################################################################### -->

Feature: Creative and game modes for bot settings
-------------------------------------------------

Mentioned:
https://discord.com/channels/646000428441534474/910679364335730718/915411137556787260

<!-- ####################################################################### -->

Feature: Email/IM NPCS
----------------------
Mentioned: 
https://discord.com/channels/646000428441534474/910679364335730718/916341809263820800

But why? The phone does actually exist, after all. 

<!-- ####################################################################### -->

Feature: Package manager and `/opt` folder
------------------------------------------
I'd like to ship code. So this makes sense to me.

I may have the wrong one in mind.

My WSL install shows:
```
bin
boot
dev
etc
home
init
lib
lib64
media
mnt
opt
proc
root
run
sbin
snap
srv
sys
tmp
usr
var
```

Getting a basic posix standard going would be nice. He has sort of started
already.

<!-- ####################################################################### -->

Feature: Properly network bots
------------------------------

Didn't create proper bot network
https://discord.com/channels/646000428441534474/910679364335730718/915302207782551574

<!-- ####################################################################### -->

Feature: Provide access to passability knowledge
------------------------------------------------

Mentioned need for implementing:
https://discord.com/channels/646000428441534474/910679364335730718/915407659316949052

<!-- ####################################################################### -->

Feature: Scroll the console log
-------------------------------

Mentioned here:
https://discord.com/channels/646000428441534474/910679364335730718/916530093990494259

<!-- ####################################################################### -->

Feature: Shittier version of Gnu Man
------------------------------------

The mod does feature the `help` function, but I've been thinking about this for
a minute anyway.

Requested-ish:
https://discord.com/channels/646000428441534474/910679364335730718/923609986792321064

JoeStrout has doubts (https://discord.com/channels/646000428441534474/910679364335730718/923610329819279360):
> there is the `help` command
> but it only covers high-level topics
> I don't really see how we could include a detailed manual in-game

<!-- ####################################################################### -->

Feature: Some kind of "wait until machine ui closed" function
-------------------------------------------------------------

Joe seems to need essentially this here:
https://discord.com/channels/646000428441534474/910679364335730718/916529531110699039

Probably better is just some way to check if bot/machine ui is open. A player
could theoretically do that "and more" for themselves with such functionality.

<!-- ####################################################################### -->

Hype: Multiplayer
-----------------

All the times people mention wanting multiplayer support

Zaxablock:
https://discord.com/channels/646000428441534474/910679364335730718/931235183775084574

<!-- ####################################################################### -->

Improve: Ahead function
-----------------------

Defines it here
https://discord.com/channels/646000428441534474/910679364335730718/915311611810545744

Seems to pointlessly rely on "here" function
https://discord.com/channels/646000428441534474/910679364335730718/915311696480960542

<!-- ####################################################################### -->

Improve: Clearahead Demo/function
---------------------------------
 
Clearahead created:
https://discord.com/channels/646000428441534474/910679364335730718/914582673064886322

Improved:
https://discord.com/channels/646000428441534474/910679364335730718/915408914932203571

<!-- ####################################################################### -->

Improve: Editor
---------------

Fucking really, Joe?

> I haven't decided if I'm going to go for a nano/pico editor style, where you
> hit ^K to cut lines and ^U to uncut (paste) them....
>
> or a more modern style where you select with the mouse (once we have mouse
> support) and then cut/copy/paste.
https://discord.com/channels/646000428441534474/910679364335730718/931297448188575834

Mode-based editing died for a reason, and the desktop metaphor took over for a
reason.

Fix Joe's janky ass editor.


<!-- ####################################################################### -->

Improve: Provide user configuration in Farmtronics env for basic tools
----------------------------------------------------------------------

There have been requests that basically amount to this. Joe - repeatedly - has
said "you can just edit the code for the editor yourself!" ... but this isn't
really a good way to ship integrated software. Instead, we should provide it
as a configuration file.

Text editor arrow keys, please?
https://discord.com/channels/646000428441534474/910679364335730718/931228767198777374

<!-- ####################################################################### -->

Issue: Check mod can read all possible typable keys on a standard QWERTY keyboard
---------------------------------------------------------------------------------

This has been an issue in the past for users
https://discord.com/channels/646000428441534474/910679364335730718/931229104857042985

Joe provided the short method to read a key back
> fire up any Farmtronics computer (home computer or bot)
> and then enter
> `print key.get.code`
> and then press one of those numpad arrows.  What does it print?
https://discord.com/channels/646000428441534474/910679364335730718/931229350966202388

The expected error is "got Unknown( )" for keys the mod can't read out.

<!-- ####################################################################### -->

Issue: It's possible to cause Pierre's to close as part of the game's story
---------------------------------------------------------------------------

By siding with JojaMart.

This may make it impossible to purchase bots.

Zaxablock first mentioned this in the #farmtronics logs.

https://discord.com/channels/646000428441534474/910679364335730718/931213392641933312

<!-- ####################################################################### -->

ZZZ: Random things Joe has said
-------------------------------

https://discord.com/channels/646000428441534474/910679364335730718/915313590687395900

> here's a good first script to try (on a bot)...
>
> ```
> for i in range(5)
>    forward
> end for
>```
> 
> or even
> 
> ```
> for i in range(5)
>    forward; forward; left
> end for
> ```

11/30/2021: https://discord.com/channels/646000428441534474/910679364335730718/915315508398673970

> hang on
>
> here's my complete `startup.ms`
>
```
here = function()
    return position.area
end function

scan = function()
    here = position.area
    for x in range(0, here.width-1)
        for y in range(0, here.height-1)
            t = here.tile(x,y)
            if not t then continue
            print x+","+y + ": " + t
        end for
    end for
end function

ahead = function()
    f = facing
    pos = position
    if f == 0 then return here.tile(pos.x, pos.y-1)
    if f == 1 then return here.tile(pos.x+1, pos.y)
    if f == 2 then return here.tile(pos.x, pos.y+1)
    if f == 3 then return here.tile(pos.x-1, pos.y)
end function

equip = function(toolName)
    inv = inventory
    toolName = toolName.lower
    for i in inv.indexes
        if inv[i] and inv[i].name.lower == toolName then
            globals.currentToolIndex = i
            print "Equipped " + inv[i].name + " (index " + i + ")"
            return
        end if
    end for
    print "No tool found matching: " + toolName
end function

clearAhead = function()
    obstacle = ahead
    if not obstacle then return
    what = obstacle.type
    if obstacle.hasIndex("name") then what = obstacle.name
    print "Clearing: " + what
    if what == "Grass" or what == "Weed" then
        globals.statusColor = "#66FF66"
        equip "Scythe"
    else if what == "Stone" then
        globals.statusColor = "#8888FF"
        equip "Pickaxe"
    else
        globals.statusColor = "#FF8800"
        equip "Axe"
    end if
    useTool
end function

clearAndMove = function(dist=1)
    for i in range(dist-1)
        pos = position
        while position == pos
            clearAhead
            forward
        end while
    end for
end function

clearGrid = function(width, height)
    for h in range(0, height-1)
        clearAndMove width
        if h % 2 then
            right; clearAndMove; right
        else
            left; clearAndMove; left
        end if
    end for
end function

screenColor = "#333399"
print
print "Ready."
print
```
> end quote

12/15/2021 - More startup:
https://discord.com/channels/646000428441534474/910679364335730718/920777999601778778

12/23/2021 - JoeStrout decides on the ToDo quest:
https://discord.com/channels/646000428441534474/910679364335730718/923601890065907842

1/3/2022 - JoeStrout has chicken tortellini for dinner:
https://discord.com/channels/646000428441534474/910679364335730718/927714285411512342

1/3/2022 - Wall-E alternate sprite joke. JoeStrout seems amused.
https://discord.com/channels/646000428441534474/910679364335730718/927734333270261810

1/13/2022 - "also see: Autonauts"
https://discord.com/channels/646000428441534474/910679364335730718/931208345208107070

1/13/2022 - might help Joe to find a way to register numpad keys, home island, etc
https://discord.com/channels/646000428441534474/910679364335730718/931230673757417502

1/13/2022 - Joe shows off his keyboard, which he designed himself
https://discord.com/channels/646000428441534474/910679364335730718/931232295833194497

1/13/2022 - Joe is one of those DVORAK users
https://discord.com/channels/646000428441534474/910679364335730718/931233010274144307

1/13/2022 - Is multi reading files non-blocking?
https://discord.com/channels/646000428441534474/910679364335730718/931235881719832606

1/13/2022 - "evil farmbots" joke image, Joe seemed to like it, maybe alt skin?
https://discord.com/channels/646000428441534474/910679364335730718/931287342533185566

1/13/2022 - StarWars gon droid joke, another alt skin?
https://discord.com/channels/646000428441534474/910679364335730718/931288054952501321

1/13/2022 - TODO in startup presented
https://discord.com/channels/646000428441534474/910679364335730718/931317089938067466

1/13/2022 - Joe wants games for demos
https://discord.com/channels/646000428441534474/910679364335730718/931322760213463100

1/13/2022 - error repro - make sure bots aren't still a chest?
https://discord.com/channels/646000428441534474/910679364335730718/931333386465857587

1/13/2022 - outstanding known errors v1.01, double check
https://discord.com/channels/646000428441534474/910679364335730718/931334122079666176
OK, I've fixed the editor.
[6:49 PM]
So here's my known-issues list...
[6:49 PM]
- The command line cursor gets misplaced if, at the bottom of the screen, you type a command longer than 40 characters (so that it wraps) and then back up with the left arrow key to the previous line.
- If you pick up a bot by repeatedly left-clicking it with empty hands, it leaves a "ghost" image behind until you put it down again.
- If you use a hoe on a bot, it turns into a chest.  (Work-around for this and the previous issue: pick up a bot with axe or pickaxe only.)

1/15/2022 - Todd Howard (no, not that one) code snippet, no license given
https://discord.com/channels/646000428441534474/910679364335730718/932031472615977011

<!-- ####################################################################### -->

The rest
--------

1/15/2022

Doc API
> @bot.indexes will list all the bot commands.
https://discord.com/channels/646000428441534474/910679364335730718/932035126441938944

Doc Caveat Emptor
> btw don't use pprint for printing strings... just use ordinary print for that.
https://discord.com/channels/646000428441534474/910679364335730718/932062623732740117

Doc Style Guide
> Ah, for that you do need parentheses
> otherwise the grammar is ambiguous.
> So if it's a function that returns a value, use parens.
https://discord.com/channels/646000428441534474/910679364335730718/932093229233487932
... The fuck?

1/16/2022

Request: Check watering can water level
> https://discord.com/channels/646000428441534474/910679364335730718/932151418075373630

Request: Check ground wet
https://discord.com/channels/646000428441534474/910679364335730718/932294256939397221

Docs: Changing globals
https://discord.com/channels/646000428441534474/910679364335730718/932311880003891240
https://discord.com/channels/646000428441534474/910679364335730718/932323281300770856
https://discord.com/channels/646000428441534474/910679364335730718/932323361328103544

Check err
https://discord.com/channels/646000428441534474/910679364335730718/932337753088213072

Std: Folder structure
https://discord.com/channels/646000428441534474/910679364335730718/932340651478110208

Std: package
> well you can do that, though since "package" means "file" in Mini Micro, it
> seems like you're going to have a bunch of folders containing one file each.
https://discord.com/channels/646000428441534474/910679364335730718/932341063677534209
Goddamnit, Joe.

Std: Intents
> Even older-school than that, really.  Think DOS or Apple II.
> Except, of course, with a much more modern language & support infrastructure.
https://discord.com/channels/646000428441534474/910679364335730718/932341486320771112
Nostalgia is understood but should be tempered with what we've learned since
then. We don't tell kids to get excited about programming in assembly for the
gameboy - we teach kids C++, C#, and Java and get them excited about programming
modern machinery. Why not find a hella way to mash these two things up instead
of willfully doing things the hard way because "well, you see, back in my
day..."

STD: Intents
> close to the metal!
> (though it's virtual metal)
https://discord.com/channels/646000428441534474/910679364335730718/932341613320093836

Check issues:
https://discord.com/channels/646000428441534474/910679364335730718/932342142901288970

Bots made to stop working when you leave the farm:
https://discord.com/channels/646000428441534474/910679364335730718/932363226593767454
Maybe fucking don't? What's the use if you have to babysit them? Appears to be
a non-fix to a different bug in the behavior, regarding breakage.

1/17/2022

Multiplayer bug?
https://discord.com/channels/646000428441534474/910679364335730718/932655343677349938

API: File
https://discord.com/channels/646000428441534474/910679364335730718/932660866095153213

Intent: Bots need correct tool, mod is not THAT cheaty
https://discord.com/channels/646000428441534474/910679364335730718/932664651727122472

Multiplayer unsupported
https://discord.com/channels/646000428441534474/910679364335730718/933184007645048893

Joe is married, to his wife
https://discord.com/channels/646000428441534474/910679364335730718/933184791870865418

Joe and his wife watche "Kim's Conveinience" together
https://discord.com/channels/646000428441534474/910679364335730718/933184791870865418

19 Jan 2022

1.0.3 version of the mod published
https://discord.com/channels/646000428441534474/910679364335730718/933460077875195934

24 Jan 2022

Mod is noticed by PCGamer
https://discord.com/channels/646000428441534474/910679364335730718/935279270505381899

Docs? Community is meant to be here to help, even with todo tasks, for newcomers
https://discord.com/channels/646000428441534474/910679364335730718/935281362569662474

Docs - tools for MiniScript
https://discord.com/channels/646000428441534474/910679364335730718/935370296683294800

Std - no function parenthesises
https://discord.com/channels/646000428441534474/910679364335730718/935374129970966539

Check - bot on Ginger Island
https://discord.com/channels/646000428441534474/910679364335730718/935376529746169886

Check - bot in mines
... waaaaay earlier.

Joe doesn't get to play much due to his development habit
https://discord.com/channels/646000428441534474/910679364335730718/935377289888276481

Joe's debug workflow makes him feel like Phil Connors in Groundhog Day
https://discord.com/channels/646000428441534474/910679364335730718/935378159304585257

Joe quote moment
> Just think of your Robot Minions doing your bidding when fully programmed!
https://discord.com/channels/646000428441534474/910679364335730718/935378344885768193

Feature request: Bot fishing
https://discord.com/channels/646000428441534474/910679364335730718/935378393925566494

Std: Line indentations don't "really" matter
https://discord.com/channels/646000428441534474/910679364335730718/935379701055234088

Joe groundhog day: Mommalisa replies:
> you don't have to Groundhog Day... just water the crops and then go to sleep!  who cares if it's 7 am!
https://discord.com/channels/646000428441534474/910679364335730718/935382478875660380

Joe and his wife, "Kim's Conveinience"
https://discord.com/channels/646000428441534474/910679364335730718/935385805021663332

Request: Proper bot networking
https://discord.com/channels/646000428441534474/910679364335730718/935386040691200010

BeerWineSpirits - farm maintenance script
https://discord.com/channels/646000428441534474/910679364335730718/935386463430914119

25 Jan 2022

STd: Spaces don't "really" matter in function params
https://discord.com/channels/646000428441534474/910679364335730718/935549766589374546

idea: make a special command parser for the command line
https://discord.com/channels/646000428441534474/910679364335730718/935550223546208307

Priorities - check to make sure they were fulfilled
https://discord.com/channels/646000428441534474/910679364335730718/935553624849932328

Coding streams are mondays
https://discord.com/channels/646000428441534474/910679364335730718/935562109020934204

Joe strout's twitch is https://www.twitch.tv/joestrout/videos
https://discord.com/channels/646000428441534474/910679364335730718/935562148229304360

feature request: git/pastebin import
https://discord.com/channels/646000428441534474/910679364335730718/935560460525240390

STD: function ref
https://discord.com/channels/646000428441534474/910679364335730718/935573533671690342

Quotable moment: BearWineSpirits
> lmao... fun fact i don't drink
https://discord.com/channels/646000428441534474/910679364335730718/935577077367861279

Demo Idea: Script to make bots follow specific tile as a "highway"
https://discord.com/channels/646000428441534474/910679364335730718/935579722421792838
... how would they know to turn around?
... command bots to move using specific tiles?

Quotable Joe:
> Guru (n): Someone who has had their computer longer than you.
https://discord.com/channels/646000428441534474/910679364335730718/935615351822098443

STD: intent:
> But it's a game, it's not meant to feel like work.  So you do you!
https://discord.com/channels/646000428441534474/910679364335730718/935618204515065880

Quotable Joe:
> But it's a game, it's not meant to feel like work.  So you do you!
https://discord.com/channels/646000428441534474/910679364335730718/935618204515065880

Farmtronics 1.0.4 released:
https://discord.com/channels/646000428441534474/910679364335730718/935651003011833938

Request: Reliable bot use in mines
https://discord.com/channels/646000428441534474/910679364335730718/935678629948555274

Joe eats squash soup
https://discord.com/channels/646000428441534474/910679364335730718/935679065170538546

Possible bug, check:
https://discord.com/channels/646000428441534474/910679364335730718/935679988357824513

Intents: Bug reports:
> (P.S. pics/video or it didn’t happen)
https://discord.com/channels/646000428441534474/910679364335730718/935748016500015104

Bug check: Bots maintain inventory or drop when mined?
https://discord.com/channels/646000428441534474/910679364335730718/935748582210936952

Bug check: Possible duplication
https://discord.com/channels/646000428441534474/910679364335730718/935756620045090866

26 January 2022

Docs - joe had meant to do it. Did he? ... fuck knows. Not Joe's fault. Typical
life story - the docs are always out of date. We need a way to introspect
documentation consistently. Can we force direct reference calls to be a child
of a function member and use the function's body to declare a docstring somehow?
https://discord.com/channels/646000428441534474/910679364335730718/935961208203403314

Bug re:Ginger Farm, plus workaround
https://discord.com/channels/646000428441534474/910679364335730718/935961637263904859

Does Joe not trust Pierre?
https://discord.com/channels/646000428441534474/910679364335730718/935962682429931550

Demo work?
https://discord.com/channels/646000428441534474/910679364335730718/935979339764363284

API: Secret function
https://discord.com/channels/646000428441534474/910679364335730718/935985209634086922

Joe would like a photo of a crow on a bot
https://discord.com/channels/646000428441534474/910679364335730718/936099171163861012

Joe struggles just like any programmer
https://discord.com/channels/646000428441534474/910679364335730718/936102898914451557

Joe keeps a known issues list... in his roadmap.
> https://discord.com/channels/646000428441534474/910679364335730718/936105568735735809
Goddamnit Joe, use your fucking issue tracker and github's tools for this

Internals
https://discord.com/channels/646000428441534474/910679364335730718/936106963819966526

STD: lingua - () are "parens"
https://discord.com/channels/646000428441534474/910679364335730718/936110131517734952

Std: lingua - [] are "brackets"
https://discord.com/channels/646000428441534474/910679364335730718/936110172877758495

std: code - 0-based indexing
https://discord.com/channels/646000428441534474/910679364335730718/936112077360222229

Intent: only side effects in /usr
https://discord.com/channels/646000428441534474/910679364335730718/936291388243456050

API?
https://discord.com/channels/646000428441534474/910679364335730718/936322851387080704

27 January 2022

1.05 released
https://discord.com/channels/646000428441534474/910679364335730718/936375843280801825

Joe is taking dance lessons?!?
https://discord.com/channels/646000428441534474/910679364335730718/936454696707715143

Quotable Joe
> This plot has too many twists and turns for me.  I need the crib notes.
https://discord.com/channels/646000428441534474/910679364335730718/936475342670004254
That's an old term, incidentally. Like, 1960s kind of old.

Feature: Bot smokes if frustrated
https://discord.com/channels/646000428441534474/910679364335730718/936477624908251157

28 January 2022

Joe's coding style is inconsistent.
https://discord.com/channels/646000428441534474/910679364335730718/936637900865556581
```
pos = [15,34]  // or maybe pos = [bot.position.x, bot.position.y]
counts[pos] = 1
```

Sysdisk - I've been looking for this fucking thing!
https://discord.com/channels/646000428441534474/910679364335730718/936639422831656991
https://github.com/JoeStrout/Farmtronics/tree/main/M1/assets/sysdisk

User of Vortex:
https://discord.com/channels/646000428441534474/910679364335730718/936651002684252270

API - mneumonic
https://discord.com/channels/646000428441534474/910679364335730718/936651340556419103
> pprint stands for "pretty print" and is a handy command to know.

Docs - tricks
https://discord.com/channels/646000428441534474/910679364335730718/936652601678782544
> other good console tricks:
> • at the command prompt, press up-arrow to recall earlier commands.
> • control-A jumps to the beginning of the input line
> • control-E jumps to the end of the line
> • holding alt or control with arrow keys should move by word
> • use clear to clear the screen.
> • if you need to reset/reboot your bot, pick him up and put him back down again.

API reference intents:
https://discord.com/channels/646000428441534474/910679364335730718/936725906322497596

std: style - array declaration
counts = [0] * bot.inventory.len
just type that into the console.
Then call your modified clearGrid function.
Or if you prefer, just do counts = [0,0,0,0,0,0,0]
https://discord.com/channels/646000428441534474/910679364335730718/936729754516742207

Quotable Joe moment
https://discord.com/channels/646000428441534474/910679364335730718/936736548743946360
> ...when you try to pet the dog, and accidentally water him instead. :flushed:

Joe wants screenshots and videos for nexus
https://discord.com/channels/646000428441534474/910679364335730718/936753837321109586

Feature request: Bot speed upgrade
https://discord.com/channels/646000428441534474/910679364335730718/936765116035264563

Alt sprite: Wallace and Gromit
https://discord.com/channels/646000428441534474/910679364335730718/936767741292081152

Sprite influence
https://discord.com/channels/646000428441534474/910679364335730718/936768776819580998

Alt Sprite: C64 Monitor
https://discord.com/channels/646000428441534474/910679364335730718/936773354789146655

29 January 2022

Docs - sticky wicket and intents
> though they all share the same /usr disk.
> (Think of it like a network drive.)
https://discord.com/channels/646000428441534474/910679364335730718/936962316107399188

STD: format - indentation is for readability
> I'd indent the code a bit to make it easier to read, but otherwise it looks good.
https://discord.com/channels/646000428441534474/910679364335730718/936963139587686400

Quotable Joe: FEAR YOUR ROBOT MINIONS!!!
https://discord.com/channels/646000428441534474/910679364335730718/936964846568755241

Things to check:
https://discord.com/channels/646000428441534474/910679364335730718/937043394872623134

Error to check
https://discord.com/channels/646000428441534474/910679364335730718/937057786838282322

Tricks: Yield motherfucker
> You can put a yield into your big loops; that will probably help.
> yield basically says "I'm done for now; continue on the next frame"
https://discord.com/channels/646000428441534474/910679364335730718/937062251083493446

Joe's wife caught him taking dancing lessons. It was meant to be a surprise for her.
https://discord.com/channels/646000428441534474/910679364335730718/937063106008481796

check if lifting and dropping a bot still refills its energy.
https://discord.com/channels/646000428441534474/910679364335730718/937064481895354488

future: networking
https://discord.com/channels/646000428441534474/910679364335730718/937064888264720435

future: autostart each day
> https://discord.com/channels/646000428441534474/910679364335730718/937064994636451840

Suggestion: Bots without energy shouldn't be able to move themselves
https://discord.com/channels/646000428441534474/910679364335730718/937065413823570011
Seconded: https://discord.com/channels/646000428441534474/910679364335730718/937065431498375198

tricks: 2d Array
https://discord.com/channels/646000428441534474/910679364335730718/937066132714692659

Ginger island bug to check:
https://discord.com/channels/646000428441534474/910679364335730718/937118017232453663

Term for repeated day/groundhog day: reDay
https://discord.com/channels/646000428441534474/910679364335730718/937118535824592966

1 Feb 2022

Bug to check
https://discord.com/channels/646000428441534474/910679364335730718/938092190922604554

Bug to check
https://discord.com/channels/646000428441534474/910679364335730718/938092902586912848

1.06 released
https://discord.com/channels/646000428441534474/910679364335730718/938198367534743553

5 Feb 2022

API: Get location (?)
https://discord.com/channels/646000428441534474/910679364335730718/939626623718809600

Check breakage when stacking bots
https://discord.com/channels/646000428441534474/910679364335730718/939637396063019048

Joe wants videos of bots doing cool things
https://discord.com/channels/646000428441534474/910679364335730718/939642971001860097

docs
https://discord.com/channels/646000428441534474/910679364335730718/939648825507868673

issue - sometimes game gets stuck on saving screen (multiplayer only?)
https://discord.com/channels/646000428441534474/910679364335730718/939670904252805152

Joe code startup.ms
https://discord.com/channels/646000428441534474/910679364335730718/939676177675722832

Joe code startup.ms
https://discord.com/channels/646000428441534474/910679364335730718/939676742145163264

Feature request: bot emote
https://discord.com/channels/646000428441534474/910679364335730718/939723925720559668

6 Feb 2022

Joe named himself "Testy2" in game
https://discord.com/channels/646000428441534474/910679364335730718/939899422907703297

Test if swords damage enemies
https://discord.com/channels/646000428441534474/910679364335730718/939919734214910003

7 feb 2022

Joke that joe liked
https://discord.com/channels/646000428441534474/910679364335730718/940208289558433812

doc - file read/write
https://discord.com/channels/646000428441534474/910679364335730718/940309736904093716

bug - bots move while time is frozen (joe willfully ignores it)
https://discord.com/channels/646000428441534474/910679364335730718/940362084833693726

Farmtronics 1.0.7 released
https://discord.com/channels/646000428441534474/910679364335730718/940447741295853639

8 Feb 2022

Bug to test
https://discord.com/channels/646000428441534474/910679364335730718/940749841963831347

Joe really hates parens
https://discord.com/channels/646000428441534474/910679364335730718/940779972652585010

STD style: No parens around conditions of `if` and `while`
https://discord.com/channels/646000428441534474/910679364335730718/940780173656195123

Quotable joe:
> (C has warped everyone's minds!)
https://discord.com/channels/646000428441534474/910679364335730718/940780227699830785

behavior:
https://discord.com/channels/646000428441534474/910679364335730718/940781564969754644

9 Feb 2022

bug to test giant plants
https://discord.com/channels/646000428441534474/910679364335730718/941102572821942382
dat for that - 3x3 fully watered mature crops = 1% giant crop each day

quotes
https://discord.com/channels/646000428441534474/910679364335730718/941113329735311390

bug to test - or maybe misfeature
https://discord.com/channels/646000428441534474/910679364335730718/941145000085966868

Farmtronics 1.08 released
https://discord.com/channels/646000428441534474/910679364335730718/941178482568867841

10 Feb 2022

request: emacs controls in editor
https://discord.com/channels/646000428441534474/910679364335730718/941199131819507782

challenge: implement pathfinding for bots
https://discord.com/channels/646000428441534474/910679364335730718/941453334181724261

wanted: passable attribute
https://discord.com/channels/646000428441534474/910679364335730718/941462362018443285

11 Feb 2022

Doc: short circuit
https://discord.com/channels/646000428441534474/910679364335730718/941827908631158865

14 Feb 2022

Tag repos "miniscript" and "farmtronics"
https://discord.com/channels/646000428441534474/910679364335730718/942976205823545375

20 Feb 2022

idea: stardew valley api emulation within mini micro
https://discord.com/channels/646000428441534474/910679364335730718/944973027400122420

22 Feb 2022

Issue and std style: Lists can't be used as defaults?
https://discord.com/channels/646000428441534474/910679364335730718/945766207657762896
https://discord.com/channels/646000428441534474/910679364335730718/945771637238804541

25 Feb 2022

possibe error to check:
https://discord.com/channels/646000428441534474/910679364335730718/946900684471693362

26 Feb 2022

Epiphaner/Renezaal's scripts
https://discord.com/channels/646000428441534474/910679364335730718/947084145740353536
https://github.com/renezaal/farmtronics-scripts/

28 Feb 2022

Intents: Examples should be simple
https://discord.com/channels/646000428441534474/910679364335730718/947902475749453824

1 March 2022

Error - bot loses upgraded items
https://discord.com/channels/646000428441534474/910679364335730718/948294912858783824

10 April 2022

Farmtronics 1.0.9 released
https://discord.com/channels/646000428441534474/910679364335730718/962724734825545728

29 May 2022

Joe's general advice
https://discord.com/channels/646000428441534474/910679364335730718/980517844691329094

1 June 2022

Bug to check
https://discord.com/channels/646000428441534474/910679364335730718/981652564380647437

2 June 2022

Import doesn't know subdirectories exist
https://discord.com/channels/646000428441534474/910679364335730718/981911327712878643

3 June 2022

Miniscript doesn't do backslash escaping
https://discord.com/channels/646000428441534474/910679364335730718/982304882541355080

Why the fuck not? Well...
https://discord.com/channels/646000428441534474/910679364335730718/982308601471316028
Joe must not have been a game dev; he seems to have not used double quote much
Escaping it is a double double quote... specifically to avoid the standard
escape character, a backslash. [...] if Joe wants to teach people to write code,
he's building shittons of pitfalls for people to fall headlong into later, when
they try to generalize their understanding to other languages.

His justification seems to be extreme situations that can arise in C-family
languges.
https://discord.com/channels/646000428441534474/910679364335730718/982309513602424902
Apparently, Joe never was introduced to the idea of raw strings in Python.

Intent: escape's context awareness
https://discord.com/channels/646000428441534474/910679364335730718/982491019595620372

4 June 2022

Do the crazy bitch method of networking - pass information through a global var
since the interpreter isn't isolating context for globals per machine
https://discord.com/channels/646000428441534474/910679364335730718/982498806681731093

Quotable Joe
> The Farmtronics company has been doing some very sketchy space-time-continuum
> research, I think.
https://discord.com/channels/646000428441534474/910679364335730718/982499915370467378

docs: api: world
https://discord.com/channels/646000428441534474/910679364335730718/982501485214580786

7 June 2022

check that the bot understands steps
https://discord.com/channels/646000428441534474/910679364335730718/983869464418340925

8 June 2022

Feature - interact with chests damnit
https://discord.com/channels/646000428441534474/910679364335730718/984301131243094016

10 June 2022

Do you know Else Heart Break?
https://discord.com/channels/646000428441534474/910679364335730718/984865972261367868

nother vortex user
https://discord.com/channels/646000428441534474/910679364335730718/984993752655478795

13 June 2022

Feature request: STDERR redirection
https://discord.com/channels/646000428441534474/910679364335730718/986115074445959189

14 June 2022

At the risk of narcissism, quotable greysondn moment
https://discord.com/channels/646000428441534474/910679364335730718/986332700262674522
> "... and it was when I found myself writing code to just let me type a few
> words to sync my git repo with all my save folders simultaneously that I
> raised my hands to the sky and shouted CURSE YOU JOE STROUT!"
The code in question also lets me write the config file I use on my farmtronics
machines in YAML and autoconverts it to JSON ;)

