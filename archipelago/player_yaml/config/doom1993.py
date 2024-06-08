from enums import Difficulty
from enums import Game
from enums import Genre
from enums import Machine

from .apcomp import ApComp
from .apcomp import BoolComp
from .apcomp import IntComp
from .apcomp import StrComp
from .apcomp import StrListComp
from .apcomp import PlandoItemListComp

from .apconfig import ApConfig

class Doom1993Base(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # genres
        self.genres.add(Genre.IMPLEMENTED)
        self.genres.add(Genre.FIRST_PERSON_SHOOTER)
        self.genres.add(Genre.SHOOTER)
        
        # machines
        self.machines.add(Machine.STORM_TOWER)
        self.machines.add(Machine.URSINE_LAPTOP)
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.DOOM_1993
        self.apgame = "DOOM 1993"
        self.requires_version = "0.4.6"
        
        self.components.append(self.death_link)

        self.progression_balancing.set(75)

        # standard defaults and docs for game-specific settings
        #
        # read the template for the game for insight into what the settings mean
        # and their legal values
        self.goal:StrComp = StrComp("goal", "complete_all_levels", 4)
        self.components.append(self.goal)

        self.difficulty:StrComp = StrComp("difficulty", "medium", 4)
        self.components.append(self.difficulty)
        
        self.random_monsters:StrComp = StrComp("random_monsters", "shuffle", 4)
        self.components.append(self.random_monsters)

        self.random_pickups:StrComp = StrComp("random_pickups", "shuffle", 4)
        self.components.append(self.random_pickups)

        self.random_music:StrComp = StrComp("random_music", "vanilla", 4)
        self.components.append(self.random_music)

        self.flip_levels:StrComp = StrComp("flip_levels", "vanilla", 4)
        self.components.append(self.flip_levels)

        self.allow_death_logic:BoolComp = BoolComp("allow_death_logic", False, 4)
        self.components.append(self.allow_death_logic)

        self.pro:BoolComp = BoolComp("pro", False, 4)
        self.components.append(self.pro)

        self.start_with_computer_area_maps:BoolComp = BoolComp("start_with_computer_area_maps", False, 4)
        self.components.append(self.start_with_computer_area_maps)

        self.reset_level_on_death:BoolComp = BoolComp("reset_level_on_death", True, 4)
        self.components.append(self.reset_level_on_death)

        self.episode1:BoolComp = BoolComp("episode1", True, 4)
        self.components.append(self.episode1)

        self.episode2:BoolComp = BoolComp("episode2", True, 4)
        self.components.append(self.episode2)
        
        self.episode3:BoolComp = BoolComp("episode3", True, 4)
        self.components.append(self.episode3)
        
        self.episode4:BoolComp = BoolComp("episode4", False, 4)
        self.components.append(self.episode4)

class Doom1993(Doom1993Base):
    def __init__(self):
        # parent
        super().__init__()
        
    def reconfigure_difficulty(self, difficulty:int) -> None:
        # so the starting default should be very easy
        # so we just progressively increase the difficulty with the timer
        if (difficulty == Difficulty.VERY_EASY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
            
            self.checks = 113
            
            # actual config
            # explicitly set all options
            self.goal.set("complete_all_levels")
            self.difficulty.set("baby")
            self.random_monsters.set("vanilla")
            self.random_pickups.set("vanilla")
            self.random_music.set("shuffle_game")
            self.flip_levels.set("vanilla")
            self.allow_death_logic.set(False)
            self.pro.set(False)
            self.start_with_computer_area_maps.set(True)
            self.reset_level_on_death.set(False)
            self.episode1.set(True)     # 113 checks
            self.episode2.set(False)
            self.episode3.set(False)
            self.episode4.set(False)
            
        if (difficulty == Difficulty.EASY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded

            # actual config
            # explicitly set all options
            self.goal.set("complete_all_levels")
            self.difficulty.set("easy")
            self.random_monsters.set("vanilla")
            self.random_pickups.set("vanilla")
            self.random_music.set("shuffle_game")
            self.flip_levels.set("vanilla")
            self.allow_death_logic.set(False)
            self.pro.set(False)
            self.start_with_computer_area_maps.set(True)
            self.reset_level_on_death.set(False)
            self.episode1.set(True)     # 113 checks
            self.episode2.set(False)
            self.episode3.set(False)
            self.episode4.set(False)
            
        
        if (difficulty == Difficulty.NORMAL.value):
            doom1993_normal_records = [
                9296,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(doom1993_normal_records)
        
            # actual config
            # explicitly set all options
            self.goal.set("complete_all_levels")
            self.difficulty.set("medium")
            self.random_monsters.set("vanilla")
            self.random_pickups.set("vanilla")
            self.random_music.set("shuffle_game")
            self.flip_levels.set("vanilla")
            self.allow_death_logic.set(False)
            self.pro.set(False)
            self.start_with_computer_area_maps.set(True)
            self.reset_level_on_death.set(False)
            self.episode1.set(True)     # 113 checks
            self.episode2.set(False)
            self.episode3.set(False)
            self.episode4.set(False)
            
        
        if (difficulty == Difficulty.HARD.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicitly set all options
            self.goal.set("complete_all_levels")
            self.difficulty.set("hard")
            self.random_monsters.set("vanilla")
            self.random_pickups.set("vanilla")
            self.random_music.set("shuffle_game")
            self.flip_levels.set("vanilla")
            self.allow_death_logic.set(False)
            self.pro.set(False)
            self.start_with_computer_area_maps.set(True)
            self.reset_level_on_death.set(False)
            self.episode1.set(True)     # 113 checks
            self.episode2.set(True)
            self.episode3.set(False)
            self.episode4.set(False)
            
        if (difficulty == Difficulty.VERY_HARD.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded            
             
            # actual config
            # explicitly set all options
            self.goal.set("complete_all_levels")
            self.difficulty.set("hard")
            self.random_monsters.set("shuffle")
            self.random_pickups.set("shuffle")
            self.random_music.set("shuffle_game")
            self.flip_levels.set("vanilla")
            self.allow_death_logic.set(False)
            self.pro.set(False)
            self.start_with_computer_area_maps.set(True)
            self.reset_level_on_death.set(False)
            self.episode1.set(True)     # 113 checks
            self.episode2.set(True)
            self.episode3.set(True)
            self.episode4.set(False)
            
        if (difficulty == Difficulty.IMPOSSIBLE.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicitly set all options
            self.goal.set("complete_all_levels")
            self.difficulty.set("nightmare")
            self.random_monsters.set("shuffle")
            self.random_pickups.set("shuffle")
            self.random_music.set("shuffle_game")
            self.flip_levels.set("vanilla")
            self.allow_death_logic.set(False)
            self.pro.set(False)
            self.start_with_computer_area_maps.set(True)
            self.reset_level_on_death.set(False)
            self.episode1.set(True)     # 113 checks
            self.episode2.set(True)
            self.episode3.set(True)
            self.episode4.set(False)


        if (difficulty == Difficulty.HATE_ME_TODAY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicitly set all options
            self.goal.set("complete_all_levels")
            self.difficulty.set("nightmare")
            self.random_monsters.set("random_balanced")
            self.random_pickups.set("random_balanced")
            self.random_music.set("shuffle_game")
            self.flip_levels.set("vanilla")
            self.allow_death_logic.set(False)
            self.pro.set(False)
            self.start_with_computer_area_maps.set(True)
            self.reset_level_on_death.set(False)
            self.episode1.set(True)     # 113 checks
            self.episode2.set(True)
            self.episode3.set(True)
            self.episode4.set(False)
    
    def print_goal(self, difficulty:int) -> None:
        out:str = "\n\n"
        
        if (difficulty == Difficulty.VERY_EASY): # baby 1
            out = out + f"Doomguy is too young to die Knee-deep in the Dead"
        elif (difficulty == Difficulty.EASY): # easy 12
            out = out + f"Doomguy hopes it's not too rough being Knee-deep in the Dead "
        elif (difficulty == Difficulty.NORMAL): # medium 12
            out = out + f"Doomguy is going to hurt plenty Knee-deep in the Dead"
        elif (difficulty == Difficulty.HARD): # hard 123
            out = out + f"Doomguy is ultra-violent in the Inferno"
        elif (difficulty == Difficulty.VERY_HARD): # hard 1234
            out = out + f"Doomguy is ultra-violent with his flesh consumed"
        elif (difficulty == Difficulty.IMPOSSIBLE): # nightmare 1234
            out = out + f"Doomguy is having that same nightmare about his flesh being consumed again"
        elif (difficulty == Difficulty.HATE_ME_TODAY): # nightmare 1234 randomized
            out = out + f"Doomguy is having unfamilar nightmares about his flesh being consumed"

        out = out + "\n\n"
        
        print(out)