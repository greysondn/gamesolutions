#!/usr/bin/env python
#expect python >= 3.10

from enum import IntEnum

# This is just a quick and dirty python script to manage my archipelago settings
# because the conditionals got too weird over time.

# settings

# which machine?
# In the mood for a certain game?
# how many checks?
# death link?
# how long?
# how hard?

class Difficulty(IntEnum):
    VERY_EASY       = 0
    EASY            = 1
    NORMAL          = 2
    HARD            = 3
    VERY_HARD       = 4
    IMPOSSIBLE      = 5
    HATE_ME_TODAY   = 6

class Game(IntEnum):
    ALL                                     = 281474976710655
    NONE                                    = 0
    ADVENTURE                               = 2 **   0
    BLASPHEMOUS                             = 2 **   1
    BUMPER_STICKERS                         = 2 **   2
    CHECKSFINDER                            = 2 **   3
    CLIQUE                                  = 2 **   4
    DARK_SOULS_III                          = 2 **   5
    DLCQUEST                                = 2 **   6
    DONKEY_KONG_COUNTRY_3                   = 2 **   7
    DOOM_1993                               = 2 **   8
    FACTORIO                                = 2 **   9
    FINAL_FANTASY                           = 2 **  10
    HOLLOW_KNIGHT                           = 2 **  11
    HYLICS_2                                = 2 **  12
    KINGDOM_HEARTS_2                        = 2 **  13
    THE_LEGEND_OF_ZELDA                     = 2 **  14
    A_LINK_TO_THE_PAST                      = 2 **  15
    LINKS_AWAKENING_DX                      = 2 **  16
    LUFIA_II_ANCIENT_CAVE                   = 2 **  17
    MEGAMAN_BATTLE_NETWORK_3                = 2 **  18
    MERITOUS                                = 2 **  19
    THE_MESSENGER                           = 2 **  20
    MINECRAFT                               = 2 **  21
    MUSE_DASH                               = 2 **  22
    NOITA                                   = 2 **  23
    OCARINA_OF_TIME                         = 2 **  24
    OVERCOOKED_2                            = 2 **  25
    POKEMON_RED_AND_BLUE                    = 2 **  26
    RAFT                                    = 2 **  27
    RISK_OF_RAIN_2                          = 2 **  28
    ROGUE_LEGACY                            = 2 **  29
    SECRET_OF_EVERMORE                      = 2 **  30
    SLAY_THE_SPIRE                          = 2 **  31
    SMZ3                                    = 2 **  32
    SONIC_ADVENTURE_2_BATTLE                = 2 **  33
    STARCRAFT_2_WINGS_OF_LIBERTY            = 2 **  34
    STARDEW_VALLEY                          = 2 **  35
    SUBNAUTICA                              = 2 **  36
    SUDOKU                                  = 2 **  37
    SUPER_MARIO_64                          = 2 **  38
    SUPER_MARIO_WORLD                       = 2 **  39
    SUPER_METROID                           = 2 **  40
    TERRARIA                                = 2 **  41
    TIMESPINER                              = 2 **  42
    UNDERTALE                               = 2 **  43
    VVVVVV                                  = 2 **  44
    WARGROOVE                               = 2 **  45
    THE_WITNESS                             = 2 **  46
    ZILLION                                 = 2 **  47

class Genre(IntEnum):
    FARMING_SIMULATOR           = 2 **   8
    FIRST_PERSON_SHOOTER        = 2 **   0
    PLATFORMER                  = 2 **   1
    PUZZLE                      = 2 **   2
    ROGUELITE                   = 2 **   3
    SHOOTER                     = 2 **   4
    RPG                         = 2 **   5
    THIRD_PERSON_SHOOTER        = 2 **   7
    WALKING_SIMULATOR           = 2 **   6

class Machine(IntEnum):
    ALL           = 3
    STORM_TOWER   = 2 ** 0
    URSINE_LAPTOP = 2 ** 1
    
MACHINES_TO_GAMES:dict[Machine, int] = {
    Machine.STORM_TOWER     :   Game.DOOM_1993.value + 
                                Game.RISK_OF_RAIN_2.value + 
                                Game.ROGUE_LEGACY.value +
                                Game.SONIC_ADVENTURE_2_BATTLE.value +
                                Game.STARDEW_VALLEY.value +
                                Game.SUPER_MARIO_WORLD.value,
                                
    Machine.URSINE_LAPTOP   :   Game.DOOM_1993.value +
                                Game.SUPER_MARIO_WORLD.value,
}

GAMES_TO_GENRES:dict[Game, int] = {
    Game.DOOM_1993 :    Genre.FIRST_PERSON_SHOOTER.value +
                        Genre.SHOOTER.value,
    
    Game.RISK_OF_RAIN_2 :   Genre.ROGUELITE.value +
                            Genre.SHOOTER.value +
                            Genre.THIRD_PERSON_SHOOTER.value,
    
    Game.ROGUE_LEGACY : Genre.PLATFORMER.value +
                        Genre.ROGUELITE.value,
    
    Game.SONIC_ADVENTURE_2_BATTLE : Genre.PLATFORMER.value,
    
    Game.STARDEW_VALLEY :   Genre.FARMING_SIMULATOR.value +
                            Genre.ROGUELITE.value +
                            Genre.RPG.value,
    
    Game.SUPER_MARIO_WORLD :    Genre.PLATFORMER.value,
}

class ApConfig():
    def __init__(self):
        # details about duration
        self.duration_max:int = 0
        '''longest this has taken to get goal in seconds'''
        self.duration_avg:int = 0
        '''average time this has taken to get goal in seconds'''
        self.duration_min:int = 0
        '''shortest time this has taken to get goal in seconds'''
        
        # main settings
        self.game:Game = Game.NONE
        '''Which game this is for'''
        
        self.description:str = "Generated by greysondn's person config generator"
        '''Description used as metadata for generator'''
        
        self.name:str = "ERR"
        '''Name for player slot'''
        
        self.apgame:str = "ERR"
        '''Name of game this is for, as goes in an archipelago config'''
        
        self.requires_version:str = "ERR"
        '''Version of Archipelago this config requires'''
        
        self.requires_plando:str = ""
        '''Plando settings this config requires'''

        # game settings
        self.accessibility:str = "items"
        '''Archipelago accessibility setting. Probably want to leave this alone.'''
        
        self.progression_balancing:str = "50"
        '''Archipelago progression balancing - probably want to leave this alone'''
        
        self.triggers:str = "IGNORED."
        '''Archipelago triggers. This var and feature is currently unused in this config generator.'''
        
        self.local_items:list[str] = []
        '''Items from the item pool to guarantee are available locally'''
        
        self.non_local_items:list[str] = []
        '''Items from the item pool to guarantee are not available locally'''
        
        self.start_inventory:list[str] = []
        '''Items to give to player at start.'''
        
        self.start_hints:list[str] = []
        '''hints to guarantee are available for free out of the gate'''
        
        self.start_location_hints:list[str] = []
        '''location hints to guarantee are available for free out of the gate'''
        
        self.exclude_locations:list[str] = []
        '''checks to guarantee DO NOT have a progression item in them, making them generally skippable'''
        
        self.priority_locations:list[str] = []
        '''checks to guarantee DO have a progression item in them, making them generally mandatory to complete'''
        
        self.item_links:str = "IGNORED."
        '''Don't really get this. Ignored in this config generator for now.'''
    
    # Some stuff to override for difficulty
    def reconfigure_checks(self, checks:int) -> None:
        pass
    
    def reconfigure_deathLink(self, deathLink:bool) -> None:
        pass
    
    def reconfigure_duration(self, duration:int) -> None:
        pass

    def reconfigure_difficulty(self, difficulty:int) -> None:
        pass
    
    def reconfigure_end(self) -> None:
        pass
    
    def reconfigure_start(self) -> None:
        pass
    
    def reconfigure(self, checks:int, deathLink:bool, duration:int, difficulty:int) -> None:
        """Override this to reconfigure the game before prepping output.

        Args:
            checks (int): Approximate target number of checks for game to have.
            deathLink (bool): whether or not to enable death link
            duration (int): approximate max duration of play in seconds
            difficulty (int): how hard the game is meant to be
        """        
        self.reconfigure_start()
        self.reconfigure_difficulty(difficulty)
        self.reconfigure_checks(checks)
        self.reconfigure_duration(duration)
        self.reconfigure_deathLink(deathLink)
        self.reconfigure_end()
    
    # output prep functions
    def prep_simple(self, name:str, value:str, indent:int = 0) -> str:
        ret = ""
        
        for i in range(indent):
            ret = ret + " "

        ret = ret + f"{name}: {value}\n"
        
        return ret
    
    def prep_optional(self, name:str, value:str, indent:int = 0) -> str:
        ret = ""
        
        if (len(value) > 0):
        
            for i in range(indent):
                ret = ret + " "

            ret = ret + f"{name}: {value}\n"
        
        return ret
    
    def prep_list(self, name:str, value:list[str], indent:int = 0) -> str:
        ret = ""
        
        if (len(value) > 0):
            prefix = ""
            
            for i in range(indent):
                prefix = prefix + " "
            
            ret = ret + prefix + f"{name}:\n"
            
            for i in value:
                ret = ret + prefix + "    - {i}\n"
        
        return ret
    
    def prep_name(self) -> str:
        return self.prep_simple("name", self.name)
    
    def prep_game(self) -> str:
        return self.prep_simple("game", self.apgame)
    
    def prep_description(self) -> str:
        return self.prep_simple("description", self.description)
    
    def prep_requires_version(self):
        return self.prep_simple("version", self.requires_version, 4)
    
    def prep_requires_plando(self):
        return self.prep_optional("plando", self.requires_plando, 4)
    
    def prep_requires(self) -> str:
        ret = "requires:\n"
        ret = ret + self.prep_requires_version()
        ret = ret + self.prep_requires_plando()
        return ret
    
    def prep_mainSettings(self) -> str:
        ret = ""
        ret = ret + self.prep_name()
        ret = ret + self.prep_game()
        ret = ret + self.prep_description()
        ret = ret + self.prep_requires()
        return ret
    
    def prep_accessibility(self) -> str:
        return self.prep_simple("accessibility", self.accessibility, 4)
    
    def prep_progression_balancing(self) -> str:
        return self.prep_simple("progression_balancing", self.progression_balancing, 4)
    
    def prep_local_items(self) -> str:
        return self.prep_list("local_items", self.local_items, 4)
        
    def prep_nonlocal_items(self) -> str:
        return self.prep_list("non_local_items", self.non_local_items, 4)

    def prep_start_inventory(self) -> str:
        return self.prep_list("start_inventory", self.start_inventory, 4)

    def prep_start_hints(self) -> str:
        return self.prep_list("start_hints", self.start_hints, 4)
        
    def prep_start_location_hints(self) -> str:
        return self.prep_list("start_location_hints", self.start_location_hints, 4)
    
    def prep_exclude_locations(self) -> str:
        return self.prep_list("exclude_locations", self.exclude_locations, 4)
        
    def prep_priority_locations(self) -> str:
        return self.prep_list("priority_locations", self.priority_locations, 4)
    
    def prep_game_specific_settings(self) -> str:
        '''override this function to provide game specific settings.'''
        return ""
    
    def prep_gameSettings(self) -> str:
        ret = ""
        ret = ret + f"{self.game}:\n"
        ret = ret + self.prep_accessibility()
        ret = ret + self.prep_progression_balancing()
        ret = ret + self.prep_local_items()
        ret = ret + self.prep_nonlocal_items()
        ret = ret + self.prep_start_inventory()
        ret = ret + self.prep_start_hints()
        ret = ret + self.prep_start_location_hints()
        ret = ret + self.prep_exclude_locations()
        ret = ret + self.prep_priority_locations()
        ret = ret + self.prep_game_specific_settings()
        
        return ret
    
    def prep_output(self) -> str:
        ret = ""
        
        ret = ret + self.prep_mainSettings()
        ret = ret + self.prep_gameSettings()
        
        return ret
        
class Doom1993(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.DOOM_1993
        self.apgame = "DOOM 1993"
        
        raise NotImplementedError()

class RiskOfRain2(ApConfig):
    pass

class RogueLegacy(ApConfig):
    pass

class SonicAdventure2Battle(ApConfig):
    pass

class StardewValley(ApConfig):
    pass

class SuperMarioWorld(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.SUPER_MARIO_WORLD
        self.apgame = "Super Mario World"
        self.requires_version = "0.4.3"
    
    def reconfigure_start(self) -> None:
        pass