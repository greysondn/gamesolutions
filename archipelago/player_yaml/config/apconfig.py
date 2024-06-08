from enums import Game

from .apcomp import ApComp
from .apcomp import BoolComp
from .apcomp import IntComp
from .apcomp import StrComp
from .apcomp import StrListComp
from .apcomp import PlandoItemListComp

from enums import Genre
from enums import Machine

from typing import Any

class ApGenre():
    def __init__(self):
        self.genres:list[Genre] = []
    
    def has(self, genre:Genre):
        return (genre in self.genres)
    
    def add(self, genre:Genre):
        if (not self.has(genre)):
            self.genres.append(genre)
    
    def toNumber(self):
        ret:int = 0
        for genre in self.genres:
            ret = ret + genre.value
        return ret
    
    def overlapsWith(self, other:"ApGenre"):
        ret:bool = False
        for genre in self.genres:
            if (other.has(genre)):
                ret = True
        return ret
    
    def fromNumber(self, val:int):
        enums:list[Genre] = [
            Genre.FARMING_SIMULATOR,
            Genre.FIRST_PERSON_SHOOTER,
            Genre.JOKE,
            Genre.PLATFORMER,
            Genre.PUZZLE,
            Genre.ROGUELITE,
            Genre.SHOOTER,
            Genre.RPG,
            Genre.THIRD_PERSON_SHOOTER,
            Genre.WALKING_SIMULATOR,
        ]
        
        for enum in enums:
            if (val & enum.value):
                self.genres.append(enum)

class ApMachine():
    def __init__(self):
        self.machines:list[Machine] = []
    
    def has(self, machine:Machine):
        return (machine in self.machines)
    
    def add(self, machine:Machine):
        if (not self.has(machine)):
            self.machines.append(machine)

    def toNumber(self):
        ret:int = 0
        for machine in self.machines:
            ret = ret + machine.value
        return ret
    
    def fromNumber(self, val:int):
        enums:list[Machine] = [
            Machine.STORM_TOWER,
            Machine.URSINE_LAPTOP,
        ]
        
        for enum in enums:
            if (val & enum.value):
                self.machines.append(enum)

    def overlapsWith(self, other:"ApMachine"):
        ret:bool = False
        for machine in self.machines:
            if (other.has(machine)):
                ret = True
        return ret

class ApConfig():
    def __init__(self):
        # enum fields, I guess
        self.genres:ApGenre = ApGenre()
        self.machines:ApMachine = ApMachine()
        
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
        self.components:list[ApComp] = []
        """Internal list of components. Should probably not touch this so directly."""
        
        self.accessibility:StrComp = StrComp("accessibility", "items", 4)
        '''Archipelago accessibility setting. Probably want to leave this alone.'''
        self.components.append(self.accessibility)
        
        self.progression_balancing:IntComp = IntComp("progression_balancing", 50, 4)
        '''Archipelago progression balancing - probably want to leave this alone'''
        self.components.append(self.progression_balancing)
        
        self.triggers:str = "IGNORED."
        '''Archipelago triggers. This var and feature is currently unused in this config generator.'''
        # not appended
        
        self.local_items:StrListComp = StrListComp("local_items", [], 4)
        '''Items from the item pool to guarantee are available locally'''
        self.components.append(self.local_items)
        
        self.non_local_items:StrListComp = StrListComp("non_local_items", [], 4)
        '''Items from the item pool to guarantee are not available locally'''
        self.components.append(self.non_local_items)
        
        self.start_inventory:StrListComp = StrListComp("start_inventory", [], 4)
        '''Items to give to player at start.'''
        self.components.append(self.start_inventory)
        
        self.start_hints:StrListComp = StrListComp("start_hints", [], 4)
        '''hints to guarantee are available for free out of the gate'''
        self.components.append(self.start_hints)
        
        self.start_location_hints:StrListComp = StrListComp("start_location_hints", [], 4)
        '''location hints to guarantee are available for free out of the gate'''
        self.components.append(self.start_location_hints)
        
        self.exclude_locations:StrListComp = StrListComp("exclude_locations", [], 4)
        '''checks to guarantee DO NOT have a progression item in them, making them generally skippable'''
        self.components.append(self.exclude_locations)
        
        self.priority_locations:StrListComp = StrListComp("priority_locations", [], 4)
        '''checks to guarantee DO have a progression item in them, making them generally mandatory to complete'''
        self.components.append(self.priority_locations)
        
        self.item_links:str = "IGNORED."
        '''Don't really get this. Ignored in this config generator for now.'''
        # not appended
        
        self.death_link:BoolComp = BoolComp("death_link", False, 4)
        '''Death link. Anyone with death link enabled dies together. This isn't added to the internal components list for output by default as it's not in every game.'''
        # not appended. Append manually
    
    def __repr__(self):
        return f"ApConfig({self.apgame})"
    
    # Some stuff to override for difficulty
    def reconfigure_checks(self, checks:int) -> None:
        pass
    
    def reconfigure_deathLink(self, deathLink:str) -> None:
        if (deathLink.lower() == "true"):
            self.death_link.set(True)
        elif (deathLink.lower() == "false"):
            self.death_link.set(False)
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
    
    def reconfigure_player(self, player:int) -> None:
        pass
    
    def reconfigure_end(self) -> None:
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
        self.reconfigure_slot(name)
        self.reconfigure_difficulty(difficulty)
        self.reconfigure_checks(checks)
        self.reconfigure_duration(duration)
        self.reconfigure_deathLink(deathLink)
        self.reconfigure_extra(extra)
        self.reconfigure_player(abs(hash(name.lower())) % (10 ** 4))
        self.reconfigure_end()
    
    # output prep functions
    def _makeIndent(self, width:int):
        return " " * width
    
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
    
    def prep_name(self) -> str:
        return self.prep_simple("name", self.name)
    
    def prep_game(self) -> str:
        return self.prep_simple("game", self.apgame)
    
    def prep_description(self) -> str:
        return self.prep_simple("description", self.description)
    
    def prep_requires_version(self) -> str:
        return self.prep_simple("version", self.requires_version, 4)
    
    def prep_requires_plando(self) -> str:
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
    
    
    def prep_gameSettings(self) -> str:
        ret = ""
        ret = ret + f"{self.apgame}:"
        
        for i in self.components:
            ret = ret + "\n" + f"{i}"
        
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