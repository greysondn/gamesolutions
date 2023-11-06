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
        self.game:str = "ERR"
        '''Which game this is for'''
        
        self.description:str = "Generated by greysondn's person config generator"
        '''Description used as metadata for generator'''
        
        self.name:str = "ERR"
        '''Name for player slot'''
        
        self.game:str = "ERR"
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
    
    # Some stuff to override
    def reconfigure(self, checks:int, deathLink:bool, duration:int, difficulty:int):
        """Override this to reconfigure the game before prepping output.

        Args:
            checks (int): Approximate target number of checks for game to have.
            deathLink (bool): whether or not to enable death link
            duration (int): approximate max duration of play in seconds
            difficulty (int): how hard the game is meant to be
        """        
        pass
    
    # output prep functions
    def prep_name(self) -> str:
        return f"name: {self.name}\n"
    
    def prep_game(self) -> str:
        return f"game: {self.game}\n"
    
    def prep_description(self) -> str:
        return f"description: {self.description}\n"
    
    def prep_requires_version(self):
        return f"    version: {self.requires_version}\n"
    
    def prep_requires_plando(self):
        ret = ""
        
        if (len(self.requires_plando) > 0):
            ret = f"    plando: {self.requires_plando}\n"
            
        return ret
    
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
        return f"    accessibility: {self.accessibility}\n"
    
    def prep_progression_balancing(self) -> str:
        return f"    progression_balancing: {self.progression_balancing}\n"
    
    def prep_local_items(self) -> str:
        ret = ""
        
        if (len(self.local_items) > 0):
            ret = ret + "    "
        
        return ret
        
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
    
    
    def prep_game_specific_settings(self) -> str:
        '''override this function to provide game specific settings.'''
        return ""
    
    def prep_gameSettings(self) -> str:
        ret = ""
        ret = ret + f"{self.game}:\n"
        ret = ret + self.prep_accessibility()
        ret = ret + self.prep_progression_balancing()
        
        return ret
        
        
class Doom1993(ApConfig):
    pass

class RiskOfRain2(ApConfig):
    pass

class RogueLegacy(ApConfig):
    pass

class SonicAdventure2Battle(ApConfig):
    pass

class SuperMarioWorld(ApConfig):
    pass

