from enums import Game

class ApConfig():
    def __init__(self):
        # details about duration
        self.duration_max:int = 0
        '''longest this has taken to get goal in seconds'''
        self.duration_avg:int = 0
        '''average time this has taken to get goal in seconds'''
        self.duration_min:int = 0
        '''shortest time this has taken to get goal in seconds'''
        
        # details about checks etc
        self.checks:int = 0
        '''number of checks we expect the game to have for this configuration'''
        
        # main settings
        self.game:Game = Game.NONE
        '''Which game this is for'''
        
        self.description:str = "Generated by greysondn's personal config generator"
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
        
        self.death_link:bool = False
        '''Death link. Anyone with death link enabled dies together. This isn't output by default as it's not in every game.'''
    
    def __repr__(self):
        return f"ApConfig({self.apgame})"
    
    # Some stuff to override for difficulty
    def reconfigure_checks(self, checks:int) -> None:
        pass
    
    def reconfigure_deathLink(self, deathLink:str) -> None:
        if (deathLink.lower() == "true"):
            self.death_link = True
        elif (deathLink.lower() == "false"):
            self.death_link = False
        else:
            raise ValueError("Invalid deathlink value!")
    
    def helper_duration(self, durations:list[int]) -> tuple[int, int, int]:
        """Finds the mn, max, and average of a list of durations

        Args:
            durations (list[int]): list of durations, in seconds

        Returns:
            tuple[int, int, int]: (min, max, avg) of durations
        """        
        _min:int = min(durations)
        _max:int = max(durations)
        _avg:int = int(round(sum(durations) / len(durations)))
        return (_min, _max, _avg)
        
    def reconfigure_duration(self, duration:int) -> None:
        pass

    def reconfigure_difficulty(self, difficulty:int) -> None:
        pass
    
    def reconfigure_extra(self, extra:int) -> None:
        pass
    
    def reconfigure_end(self) -> None:
        pass
    
    def reconfigure_start(self) -> None:
        """Override this to match all basic settings for the game, set for the 
        shortest conceivable game on Difficulty.VERY_EASY
        """        
        pass
    
    def reconfigure_slot(self, name:str) -> None:
        self.name = name
    
    def reconfigure(self, name:str, checks:int, deathLink:str, duration:int, difficulty:int, extra:int) -> None:
        """Override this to reconfigure the game before prepping output.

        Args:
            slotname (str): name to give the slot in Archipelago
            checks (int): Approximate target number of checks for game to have.
            deathLink (bool): whether or not to enable death link
            duration (int): approximate max duration of play in seconds
            difficulty (int): how hard the game is meant to be
            extra(int): any extra setting flags
        """        
        self.reconfigure_start()
        self.reconfigure_slot(name)
        self.reconfigure_difficulty(difficulty)
        self.reconfigure_checks(checks)
        self.reconfigure_duration(duration)
        self.reconfigure_deathLink(deathLink)
        self.reconfigure_extra(extra)
        self.reconfigure_end()
    
    # output prep functions
    def _makeIndent(self, width:int):
        ret = ""
        
        for i in range(width):
            ret = ret + " "
        
        return ret
    
    def prep_simple(self, name:str, value:str, indent:int = 0) -> str:
        ret = ""
        ret = ret + self._makeIndent(indent)
        ret = ret + f"{name}: {value}\n"
        
        return ret
    
    def prep_optional(self, name:str, value:str, indent:int = 0) -> str:
        ret = ""
        
        if (len(value) > 0):
            ret = self.prep_simple(name, value, indent)
        
        return ret
    
    def prep_bool(self, name:str, value:bool, indent:int = 0) -> str:
        ret = ""
        
        swp = ""
        
        if (value == True):
            swp = "'true'"
        elif (value == False):
            swp = "'false'"
        
        ret = self.prep_simple(name, swp, indent)
        
        return ret
    
    def prep_int(self, name:str, value:int, indent = 0) -> str:
        return self.prep_simple(name, f"{value}", indent)
    
    def prep_list(self, name:str, value:list[str], indent:int = 0) -> str:
        ret = ""
        
        if (len(value) > 0):
            prefix = self._makeIndent(indent)
            ret = ret + prefix + f"{name}:\n"
            
            for i in value:
                ret = ret + prefix + f"    - {i}\n"
        
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
        ret = ""
        
        if (len(self.start_inventory) > 0):
            prefix = self._makeIndent(4)
            ret = ret + prefix + f"start_inventory:\n"
            
            for i in self.start_inventory:
                ret = ret + prefix + f"    {i}: 1\n"
        
        return ret
    
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
        ret = ret + f"{self.apgame}:\n"
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
    
    def print_goal(self, difficulty:int) -> None:
        """Override to output the objective note for whatever the game is.
        """        
        pass