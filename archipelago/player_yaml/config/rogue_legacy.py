from .apconfig import ApConfig
from enums import Difficulty
from enums import Game

import math
import random

class RogueLegacy(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.ROGUE_LEGACY
        self.apgame = "Rogue Legacy"
        self.requires_version = "0.4.4"
        
        # standard defaults and docs for game-specific settings
        #
        # read the template for the game for insight into what the settings mean
        # and their legal values
        self.starting_gender:str = "random"
        self.starting_class:str  = "knight"
        self.available_classes:list[str] = [
            "Lich",
            "Dragon",
            "Traitor",
            "Miner",
            "Knight",
            "Barbarian",
            "Mage",
            "Shinobi",
            "Spellthief",
            "Knave",
        ]
        self.new_game_plus:str = "normal"
        self.fairy_chests_per_zone:int = 1
        self.chests_per_zone:int = 20
        self.universal_fairy_chests:bool = False
        self.universal_chests:bool = False
        self.vendors:str = "early"
        self.architect:str = "anywhere"
        self.architect_fee:int = 40
        self.disable_charon:bool = False
        self.require_purchasing:bool = True
        self.progressive_blueprints:bool = False
        self.gold_gain_multiplier:str = "normal"
        self.number_of_children:int = 3
        self.free_diary_on_generation:bool = True
        self.khidr:str = "vanilla"
        self.alexander:str = "vanilla"
        self.leon:str = "vanilla"
        self.herodotus:str = "vanilla"
        self.heath_pool:int = 15
        self.mana_pool:int = 15
        self.attack_pool:int = 15
        self.magic_damage_pool:int = 15
        self.armor_pool:int = 10
        self.equip_pool:int = 10
        self.crit_chance_pool:int = 5
        self.crit_damage_pool:int = 5
        self.allow_default_names:bool = True
        self.additional_lady_names:list[str] = []
        self.additional_sir_names:list[str] = []
    
    def reconfigure_start(self) -> None:
        # explicit is better than implicit
        self.progression_balancing  = "50"
        self.accessibility          = "items" # I never use locations, so...
        self.death_link = False
        
        # actual config
        self.starting_gender = "lady"
        self.starting_class  = "lich"
        self.available_classes:list[str] = [
            "Lich",
            "Dragon",
            "Traitor",
            "Miner",
            "Knight",
            "Barbarian",
            "Mage",
            "Shinobi",
            "Spellthief",
            "Knave",
        ]
        self.new_game_plus = "normal"
        self.fairy_chests_per_zone = 1
        self.chests_per_zone = 25
        self.universal_fairy_chests = True
        self.universal_chests = True
        self.vendors = "start_unlocked"
        self.architect = "start_unlocked"
        self.architect_fee = 0
        self.disable_charon = True
        self.require_purchasing = False
        self.progressive_blueprints = False
        self.gold_gain_multiplier = "quadruple"
        self.number_of_children = 5
        self.free_diary_on_generation = True
        self.khidr = "vanilla"
        self.alexander = "vanilla"
        self.leon = "vanilla"
        self.herodotus = "vanilla"
        self.heath_pool = 15
        self.mana_pool = 15
        self.attack_pool = 15
        self.magic_damage_pool = 15
        self.armor_pool = 10
        self.equip_pool = 10
        self.crit_chance_pool = 5
        self.crit_damage_pool = 5
        self.allow_default_names = True
        self.additional_lady_names = []
        self.additional_sir_names = []

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
            
            self.checks = 0
            # unrecorded
            
            # actual config
            self.starting_gender = "lady"
            self.starting_class  = "lich"
            self.available_classes:list[str] = [
                "Lich",
                "Dragon",
                "Traitor",
                "Miner",
                "Knight",
                "Barbarian",
                "Mage",
                "Shinobi",
                "Spellthief",
                "Knave",
            ]
            self.new_game_plus = "normal"
            self.fairy_chests_per_zone = 1
            self.chests_per_zone = 25
            self.universal_fairy_chests = True
            self.universal_chests = True
            self.vendors = "start_unlocked"
            self.architect = "start_unlocked"
            self.architect_fee = 0
            self.disable_charon = True
            self.require_purchasing = False
            self.progressive_blueprints = False
            self.gold_gain_multiplier = "quadruple"
            self.number_of_children = 5
            self.free_diary_on_generation = True
            self.khidr = "vanilla"
            self.alexander = "vanilla"
            self.leon = "vanilla"
            self.herodotus = "vanilla"
            self.heath_pool = 15
            self.mana_pool = 15
            self.attack_pool = 15
            self.magic_damage_pool = 15
            self.armor_pool = 10
            self.equip_pool = 10
            self.crit_chance_pool = 5
            self.crit_damage_pool = 5
            self.allow_default_names = True
            self.additional_lady_names = []
            self.additional_sir_names = []
        
        if (difficulty == Difficulty.EASY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
            
            self.checks = 0
            # unrecorded
            
            # actual config
            self.starting_gender = "lady"
            self.starting_class  = "lich"
            self.available_classes:list[str] = [
                "Lich",
                "Dragon",
                "Traitor",
                "Miner",
                "Knight",
                "Barbarian",
                "Mage",
                "Shinobi",
                "Spellthief",
                "Knave",
            ]
            self.new_game_plus = "normal"
            self.fairy_chests_per_zone = 1
            self.chests_per_zone = 25
            self.universal_fairy_chests = True
            self.universal_chests = True
            self.vendors = "start_unlocked"
            self.architect = "start_unlocked"
            self.architect_fee = 0
            self.disable_charon = True
            self.require_purchasing = True
            self.progressive_blueprints = False
            self.gold_gain_multiplier = "quadruple"
            self.number_of_children = 5
            self.free_diary_on_generation = True
            self.khidr = "vanilla"
            self.alexander = "vanilla"
            self.leon = "vanilla"
            self.herodotus = "vanilla"
            self.heath_pool = 15
            self.mana_pool = 15
            self.attack_pool = 15
            self.magic_damage_pool = 15
            self.armor_pool = 10
            self.equip_pool = 10
            self.crit_chance_pool = 5
            self.crit_damage_pool = 5
            self.allow_default_names = True
            self.additional_lady_names = []
            self.additional_sir_names = []
        
        if (difficulty == Difficulty.NORMAL.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
            
            self.checks = 0
            # unrecorded
            
            # actual config
            self.starting_gender = "lady"
            self.starting_class  = "lich"
            self.available_classes:list[str] = [
                "Lich",
                "Dragon",
                "Traitor",
                "Miner",
                "Knight",
                "Barbarian",
                "Mage",
                "Shinobi",
                "Spellthief",
                "Knave",
            ]
            self.new_game_plus = "normal"
            self.fairy_chests_per_zone = 1
            self.chests_per_zone = 25
            self.universal_fairy_chests = True
            self.universal_chests = True
            self.vendors = "start_unlocked"
            self.architect = "start_unlocked"
            self.architect_fee = 0
            self.disable_charon = True
            self.require_purchasing = True
            self.progressive_blueprints = False
            self.gold_gain_multiplier = "double"
            self.number_of_children = 5
            self.free_diary_on_generation = True
            self.khidr = "vanilla"
            self.alexander = "vanilla"
            self.leon = "vanilla"
            self.herodotus = "vanilla"
            self.heath_pool = 15
            self.mana_pool = 15
            self.attack_pool = 15
            self.magic_damage_pool = 15
            self.armor_pool = 10
            self.equip_pool = 10
            self.crit_chance_pool = 5
            self.crit_damage_pool = 5
            self.allow_default_names = True
            self.additional_lady_names = []
            self.additional_sir_names = []
        
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
            self.starting_gender = "lady"
            self.starting_class  = "random"
            self.available_classes:list[str] = [
                "Lich",
                "Dragon",
                "Traitor",
                "Miner",
                "Knight",
                "Barbarian",
                "Mage",
                "Shinobi",
                "Spellthief",
                "Knave",
            ]
            self.new_game_plus = "normal"
            self.fairy_chests_per_zone = 1
            self.chests_per_zone = 25
            self.universal_fairy_chests = False
            self.universal_chests = False
            self.vendors = "start_unlocked"
            self.architect = "start_unlocked"
            self.architect_fee = 0
            self.disable_charon = True
            self.require_purchasing = True
            self.progressive_blueprints = False
            self.gold_gain_multiplier = "normal"
            self.number_of_children = 5
            self.free_diary_on_generation = True
            self.khidr = "vanilla"
            self.alexander = "vanilla"
            self.leon = "vanilla"
            self.herodotus = "vanilla"
            self.heath_pool = 15
            self.mana_pool = 15
            self.attack_pool = 15
            self.magic_damage_pool = 15
            self.armor_pool = 10
            self.equip_pool = 10
            self.crit_chance_pool = 5
            self.crit_damage_pool = 5
            self.allow_default_names = True
            self.additional_lady_names = []
            self.additional_sir_names = []
            
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
            self.starting_gender = "lady"
            self.starting_class  = "knight"
            self.available_classes:list[str] = [
                "Lich",
                "Dragon",
                "Traitor",
                "Miner",
                "Knight",
                "Barbarian",
                "Mage",
                "Shinobi",
                "Spellthief",
                "Knave",
            ]
            self.new_game_plus = "normal"
            self.fairy_chests_per_zone = 1
            self.chests_per_zone = 25
            self.universal_fairy_chests = False
            self.universal_chests = False
            self.vendors = "early"
            self.architect = "early"
            self.architect_fee = 0
            self.disable_charon = True
            self.require_purchasing = True
            self.progressive_blueprints = False
            self.gold_gain_multiplier = "normal"
            self.number_of_children = 5
            self.free_diary_on_generation = True
            self.khidr = "vanilla"
            self.alexander = "vanilla"
            self.leon = "vanilla"
            self.herodotus = "vanilla"
            self.heath_pool = 15
            self.mana_pool = 15
            self.attack_pool = 15
            self.magic_damage_pool = 15
            self.armor_pool = 10
            self.equip_pool = 10
            self.crit_chance_pool = 5
            self.crit_damage_pool = 5
            self.allow_default_names = True
            self.additional_lady_names = []
            self.additional_sir_names = []
            
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
            self.starting_gender = "lady"
            self.starting_class  = "knight"
            self.available_classes:list[str] = [
                "Lich",
                "Dragon",
                "Traitor",
                "Miner",
                "Knight",
                "Barbarian",
                "Mage",
                "Shinobi",
                "Spellthief",
                "Knave",
            ]
            self.new_game_plus = "normal"
            self.fairy_chests_per_zone = 1
            self.chests_per_zone = 25
            self.universal_fairy_chests = False
            self.universal_chests = False
            self.vendors = "early"
            self.architect = "early"
            self.architect_fee = 40
            self.disable_charon = False
            self.require_purchasing = True
            self.progressive_blueprints = True
            self.gold_gain_multiplier = "normal"
            self.number_of_children = 3
            self.free_diary_on_generation = True
            self.khidr = "vanilla"
            self.alexander = "vanilla"
            self.leon = "vanilla"
            self.herodotus = "vanilla"
            self.heath_pool = 15
            self.mana_pool = 15
            self.attack_pool = 15
            self.magic_damage_pool = 15
            self.armor_pool = 10
            self.equip_pool = 10
            self.crit_chance_pool = 5
            self.crit_damage_pool = 5
            self.allow_default_names = True
            self.additional_lady_names = []
            self.additional_sir_names = []

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
            self.starting_gender = "lady"
            self.starting_class  = "knight"
            self.available_classes:list[str] = [
                "Lich",
                "Dragon",
                "Traitor",
                "Miner",
                "Knight",
                "Barbarian",
                "Mage",
                "Shinobi",
                "Spellthief",
                "Knave",
            ]
            self.new_game_plus = "normal"
            self.fairy_chests_per_zone = 1
            self.chests_per_zone = 25
            self.universal_fairy_chests = False
            self.universal_chests = False
            self.vendors = "early"
            self.architect = "early"
            self.architect_fee = 40
            self.disable_charon = False
            self.require_purchasing = True
            self.progressive_blueprints = True
            self.gold_gain_multiplier = "normal"
            self.number_of_children = 3
            self.free_diary_on_generation = True
            self.khidr = "vanilla"
            self.alexander = "vanilla"
            self.leon = "vanilla"
            self.herodotus = "vanilla"
            self.heath_pool = 15
            self.mana_pool = 15
            self.attack_pool = 15
            self.magic_damage_pool = 15
            self.armor_pool = 10
            self.equip_pool = 10
            self.crit_chance_pool = 5
            self.crit_damage_pool = 5
            self.allow_default_names = True
            self.additional_lady_names = []
            self.additional_sir_names = []

    def reconfigure_checks(self, checks:int) -> None:
        # aight, so hopefully I've got this right
        # The game has the following checks no matter what I do...
        # Journals     25
        # Jukebox       1
        # Painting      1
        # Carnival      1
        # Cheapskate    1
        # Bosses        4
        #
        # For a total of 33 checks. I don't know how many are on the mansion.
        #
        # TODO: Factor in mansion checks
        #
        IMMUTABLE_CHECKS:int = 33
        runningTotal:int = IMMUTABLE_CHECKS
        targetChecks:int = checks - IMMUTABLE_CHECKS
        
        # now, we divide that by 21 and round up to know how many fairy chests we need
        fairyChestsPerZone:int = int(math.ceil(targetChecks / 21))
        runningTotal = runningTotal + (fairyChestsPerZone * 4)
        
        # and now we just divide by 4... right?
        chestsPerZone:int = int(math.ceil((targetChecks - runningTotal) / 4))
        
        # set relevant values
        self.chests_per_zone = chestsPerZone
        self.fairy_chests_per_zone = fairyChestsPerZone
        
    # self.reconfigure_duration(duration)
    # self.reconfigure_extra(extra)
    
    def reconfigure_end(self) -> None:
        # handle randomizing starting class
        if (self.starting_class == "random"):
            self.starting_class = random.choice(self.available_classes).lower()
    
    def prep_game_specific_settings(self) -> str:
        ret:str = ""
        
        ret = ret + self.prep_simple("starting_gender", self.starting_gender, 4)
        ret = ret + self.prep_simple("starting_class", self.starting_class, 4)
        ret = ret + self.prep_list("available_classes", self.available_classes, 4)
        ret = ret + self.prep_simple("new_game_plus", self.new_game_plus, 4)
        ret = ret + self.prep_int("fairy_chests_per_zone", self.fairy_chests_per_zone, 4)
        ret = ret + self.prep_int("chests_per_zone", self.chests_per_zone, 4)
        ret = ret + self.prep_bool("universal_fairly_chests", self.universal_fairy_chests, 4)
        ret = ret + self.prep_bool("universal_chests", self.universal_chests, 4)
        ret = ret + self.prep_simple("vendors", self.vendors, 4)
        ret = ret + self.prep_simple("architect", self.architect, 4)
        ret = ret + self.prep_int("architect_fee", self.architect_fee, 4)
        ret = ret + self.prep_bool("disable_charon", self.disable_charon, 4)
        ret = ret + self.prep_bool("require_purchasing", self.require_purchasing, 4)
        ret = ret + self.prep_bool("progressive_blueprints", self.progressive_blueprints, 4)
        ret = ret + self.prep_simple("gold_gain_multiplier", self.gold_gain_multiplier, 4)
        ret = ret + self.prep_int("number_of_children", self.number_of_children, 4)
        ret = ret + self.prep_bool("free_diary_on_generation", self.free_diary_on_generation, 4)
        ret = ret + self.prep_simple("khidr", self.khidr, 4)
        ret = ret + self.prep_simple("alexander", self.alexander, 4)
        ret = ret + self.prep_simple("leon", self.leon, 4)
        ret = ret + self.prep_simple("herodotus", self.herodotus, 4)
        ret = ret + self.prep_int("health_pool", self.heath_pool, 4)
        ret = ret + self.prep_int("mana_pool", self.mana_pool, 4)
        ret = ret + self.prep_int("attack_pool", self.attack_pool, 4)
        ret = ret + self.prep_int("magic_damage_pool", self.magic_damage_pool, 4)
        ret = ret + self.prep_int("armor_pool", self.armor_pool, 4)
        ret = ret + self.prep_int("equip_pool", self.equip_pool, 4)
        ret = ret + self.prep_int("crit_chance_pool", self.crit_chance_pool, 4)
        ret = ret + self.prep_int("crit_damage_pool", self.crit_damage_pool, 4)
        ret = ret + self.prep_bool("allow_default_names", self.allow_default_names, 4)
        ret = ret + self.prep_list("additional_lady_names", self.additional_lady_names, 4)
        ret = ret + self.prep_list("additional_sir_names", self.additional_sir_names, 4)
        
        return ret

    def print_goal(self, difficulty:int) -> None:
        out:str = "\n\n"
        
        if (difficulty == Difficulty.VERY_EASY):
            out = out + f"Johannes' decendants should have a very easy time finding the fountain."
        elif (difficulty == Difficulty.EASY):
            out = out + f"Johannes' decendants should have an easy time finding the fountain."
        elif (difficulty == Difficulty.NORMAL):
            out = out + f"Johannes' decendants should have a normal time finding the fountain."
        elif (difficulty == Difficulty.HARD):
            out = out + f"Johannes' decendants should have a hard time finding the fountain."
        elif (difficulty == Difficulty.VERY_HARD):
            out = out + f"Johannes' decendants should have a very hard time finding the fountain."
        elif (difficulty == Difficulty.IMPOSSIBLE):
            out = out + f"Johannes' decendants should find finding the fountain to be impossible."
        elif (difficulty == Difficulty.HATE_ME_TODAY):
            out = out + f"Johannes' decendants are about to learn that the world hates a traitor on the way to the fountain."

        out = out + "\n\n"
        
        print(out)