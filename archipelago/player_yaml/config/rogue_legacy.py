from .apcomp import ApComp
from .apcomp import BoolComp
from .apcomp import IntComp
from .apcomp import StrComp
from .apcomp import StrEnumRandomizableComp
from .apcomp import StrListComp
from .apcomp import PlandoItemListComp
from .apconfig import ApConfig
from enums import Difficulty
from enums import Game

import math
import random



class RogueLegacyBase(ApConfig):
    def __init__(self):
        # reconfigure non-difficulty parts of base class
        self.game = Game.ROGUE_LEGACY
        self.apgame = "Rogue Legacy"
        self.requires_version = "0.4.4"
        
        self.progression_balancing.set(50)
        
        self.components.append(self.death_link)
        
        # standard defaults and docs for game-specific settings
        #
        # read the template for the game for insight into what the settings mean
        # and their legal values
        self.starting_gender:StrComp = StrComp("starting_gender", "random", 4)
        self.components.append(self.starting_gender)
        
        _classes:list[str] = [
            "Barbarian",
            "Dragon",
            "Knave",
            "Knight",
            "Lich",
            "Mage",
            "Miner",
            "Shinobi",
            "Spellthief",
            "Traitor",
        ]
        
        self.starting_class:StrEnumRandomizableComp  = StrEnumRandomizableComp("starting_class", "knight", _classes, 4)
        self.components.append(self.starting_class)
        
        self.available_classes:StrListComp = StrListComp("available_classes", _classes, 4)
        self.components.append(self.available_classes)
        
        self.new_game_plus:StrComp = StrComp("new_game_plus", "normal", 4)
        self.components.append(self.new_game_plus)
        
        self.fairy_chests_per_zone:IntComp = IntComp("fairy_chests_per_zone", 1, 4)
        self.components.append(self.fairy_chests_per_zone)

        self.chests_per_zone:IntComp = IntComp("chests_per_zone", 20, 4)
        self.components.append(self.chests_per_zone)
        
        self.universal_fairy_chests:BoolComp = BoolComp("universal_fairy_chests", False, 4)
        self.components.append(self.universal_fairy_chests)
         
        self.universal_chests:BoolComp = BoolComp("universal_chests", False, 4)
        self.components.append(self.universal_chests)
        
        self.vendors:StrComp = StrComp("vendors", "early", 4)
        self.components.append(self.vendors)

        self.architect:StrComp = StrComp("architect", "anywhere", 4)
        self.components.append(self.architect)

        self.architect_fee:IntComp = IntComp("architect_fee", 40, 4)
        self.components.append(self.architect_fee)
        
        self.disable_charon:BoolComp = BoolComp("disable_charon", False, 4)
        self.components.append(self.disable_charon)
        
        self.require_purchasing:BoolComp = BoolComp("require_purchasing", True, 4)
        self.components.append(self.require_purchasing)
        
        self.progressive_blueprints:BoolComp = BoolComp("progressive_blueprints", False, 4)
        self.components.append(self.progressive_blueprints)
        
        self.gold_gain_multiplier:StrComp = StrComp("gold_gain_multiplier", "normal", 4)
        self.components.append(self.gold_gain_multiplier)
        
        self.number_of_children:IntComp = IntComp("number_of_children", 3, 4)
        self.components.append(self.number_of_children)
        
        self.free_diary_on_generation:BoolComp = BoolComp("free_diary_on_generation", True, 4)
        self.components.append(self.free_diary_on_generation)
        
        self.khidr:StrComp = StrComp("khidr", "vanilla", 4)
        self.components.append(self.khidr)
        
        self.alexander:StrComp = StrComp("alexander", "vanilla", 4)
        self.components.append(self.alexander)
        
        self.leon:StrComp = StrComp("leon", "vanilla", 4)
        self.components.append(self.leon)
        
        self.herodotus:StrComp = StrComp("herodotus", "vanilla", 4)
        self.components.append(self.herodotus)
        
        self.health_pool:IntComp = IntComp("health_pool", 15, 4)
        self.components.append(self.health_pool)
        
        self.mana_pool:IntComp = IntComp("mana_pool", 15, 4)
        self.components.append(self.mana_pool)
        
        self.attack_pool:IntComp = IntComp("attack_pool", 15, 4)
        self.components.append(self.attack_pool)
        
        self.magic_damage_pool:IntComp = IntComp("magic_damage_pool", 15, 4)
        self.components.append(self.magic_damage_pool)
        
        self.armor_pool:IntComp = IntComp("armor_pool", 10, 4)
        self.components.append(self.armor_pool)
        
        self.equip_pool:IntComp = IntComp("equip_pool", 10, 4)
        self.components.append(self.equip_pool)
        
        self.crit_chance_pool:IntComp = IntComp("crit_chance_pool", 5, 4)
        self.components.append(self.crit_chance_pool)
        
        self.crit_damage_pool:IntComp = IntComp("crit_damage_pool", 5, 4)
        self.components.append(self.crit_damage_pool)
        
        self.allow_default_names:BoolComp = BoolComp("allow_default_names", True, 4)
        self.components.append(self.allow_default_names)
        
        self.additional_lady_names:StrListComp = StrListComp("additional_lady_names", [], 4)
        self.components.append(self.additional_lady_names)

        self.additional_sir_names:StrListComp = StrListComp("additional_sir_names", [], 4)
        self.components.append(self.additional_sir_names)

class RogueLegacy(RogueLegacyBase):
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
            
            self.checks = 0
            # unrecorded
            
            # actual config
            self.starting_gender.set("lady")
            self.starting_class.set("lich")
            
            _classes:list[str] = [
                "Barbarian",
                "Dragon",
                "Knave",
                "Knight",
                "Lich",
                "Mage",
                "Miner",
                "Shinobi",
                "Spellthief",
                "Traitor",
            ]
            self.available_classes.set(_classes)
            
            self.new_game_plus.set("normal")
            self.fairy_chests_per_zone.set(1)
            self.chests_per_zone.set(25)
            self.universal_fairy_chests.set(True)
            self.universal_chests.set(True)
            self.vendors.set("start_unlocked")
            self.architect.set("start_unlocked")
            self.architect_fee.set(0)
            self.disable_charon.set(True)
            self.require_purchasing.set(False)
            self.progressive_blueprints.set(False)
            self.gold_gain_multiplier.set("quadruple")
            self.number_of_children.set(5)
            self.free_diary_on_generation.set(True)
            self.khidr.set("vanilla")
            self.alexander.set("vanilla")
            self.leon.set("vanilla")
            self.herodotus.set("vanilla")
            self.health_pool.set(15)
            self.mana_pool.set(15)
            self.attack_pool.set(15)
            self.magic_damage_pool.set(15)
            self.armor_pool.set(10)
            self.equip_pool.set(10)
            self.crit_chance_pool.set(5)
            self.crit_damage_pool.set(5)
            self.allow_default_names.set(True)
            self.additional_lady_names.set([])
            self.additional_sir_names.set([])
        
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
            self.starting_gender.set("lady")
            self.starting_class.set("lich")
            
            _classes:list[str] = [
                "Barbarian",
                "Dragon",
                "Knave",
                "Knight",
                "Lich",
                "Mage",
                "Miner",
                "Shinobi",
                "Spellthief",
                "Traitor",
            ]
            self.available_classes.set(_classes)
            
            self.new_game_plus.set("normal")
            self.fairy_chests_per_zone.set(1)
            self.chests_per_zone.set(25)
            self.universal_fairy_chests.set(True)
            self.universal_chests.set(True)
            self.vendors.set("start_unlocked")
            self.architect.set("start_unlocked")
            self.architect_fee.set(0)
            self.disable_charon.set(True)
            self.require_purchasing.set(True)
            self.progressive_blueprints.set(False)
            self.gold_gain_multiplier.set("quadruple")
            self.number_of_children.set(5)
            self.free_diary_on_generation.set(True)
            self.khidr.set("vanilla")
            self.alexander.set("vanilla")
            self.leon.set("vanilla")
            self.herodotus.set("vanilla")
            self.health_pool.set(15)
            self.mana_pool.set(15)
            self.attack_pool.set(15)
            self.magic_damage_pool.set(15)
            self.armor_pool.set(10)
            self.equip_pool.set(10)
            self.crit_chance_pool.set(5)
            self.crit_damage_pool.set(5)
            self.allow_default_names.set(True)
            self.additional_lady_names.set([])
            self.additional_sir_names.set([])
        
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
            self.starting_gender.set("lady")
            self.starting_class.set("lich")
            
            _classes:list[str] = [
                "Barbarian",
                "Dragon",
                "Knave",
                "Knight",
                "Lich",
                "Mage",
                "Miner",
                "Shinobi",
                "Spellthief",
                "Traitor",
            ]
            self.available_classes.set(_classes)
            
            self.new_game_plus.set("normal")
            self.fairy_chests_per_zone.set(1)
            self.chests_per_zone.set(25)
            self.universal_fairy_chests.set(True)
            self.universal_chests.set(True)
            self.vendors.set("start_unlocked")
            self.architect.set("start_unlocked")
            self.architect_fee.set(0)
            self.disable_charon.set(True)
            self.require_purchasing.set(True)
            self.progressive_blueprints.set(False)
            self.gold_gain_multiplier.set("double")
            self.number_of_children.set(5)
            self.free_diary_on_generation.set(True)
            self.khidr.set("vanilla")
            self.alexander.set("vanilla")
            self.leon.set("vanilla")
            self.herodotus.set("vanilla")
            self.health_pool.set(15)
            self.mana_pool.set(15)
            self.attack_pool.set(15)
            self.magic_damage_pool.set(15)
            self.armor_pool.set(10)
            self.equip_pool.set(10)
            self.crit_chance_pool.set(5)
            self.crit_damage_pool.set(5)
            self.allow_default_names.set(True)
            self.additional_lady_names.set([])
            self.additional_sir_names.set([])
        
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
            self.starting_gender.set("lady")
            self.starting_class.set("random")
            
            _classes:list[str] = [
                "Barbarian",
                "Dragon",
                "Knave",
                "Knight",
                "Lich",
                "Mage",
                "Miner",
                "Shinobi",
                "Spellthief",
                "Traitor",
            ]
            self.available_classes.set(_classes)
            
            self.new_game_plus.set("normal")
            self.fairy_chests_per_zone.set(1)
            self.chests_per_zone.set(25)
            self.universal_fairy_chests.set(False)
            self.universal_chests.set(False)
            self.vendors.set("start_unlocked")
            self.architect.set("start_unlocked")
            self.architect_fee.set(0)
            self.disable_charon.set(True)
            self.require_purchasing.set(True)
            self.progressive_blueprints.set(False)
            self.gold_gain_multiplier.set("normal")
            self.number_of_children.set(5)
            self.free_diary_on_generation.set(True)
            self.khidr.set("vanilla")
            self.alexander.set("vanilla")
            self.leon.set("vanilla")
            self.herodotus.set("vanilla")
            self.health_pool.set(15)
            self.mana_pool.set(15)
            self.attack_pool.set(15)
            self.magic_damage_pool.set(15)
            self.armor_pool.set(10)
            self.equip_pool.set(10)
            self.crit_chance_pool.set(5)
            self.crit_damage_pool.set(5)
            self.allow_default_names.set(True)
            self.additional_lady_names.set([])
            self.additional_sir_names.set([])
            
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
            self.starting_gender.set("lady")
            self.starting_class.set("knight")
            
            _classes:list[str] = [
                "Barbarian",
                "Dragon",
                "Knave",
                "Knight",
                "Lich",
                "Mage",
                "Miner",
                "Shinobi",
                "Spellthief",
                "Traitor",
            ]
            self.available_classes.set(_classes)
            
            self.new_game_plus.set("normal")
            self.fairy_chests_per_zone.set(1)
            self.chests_per_zone.set(25)
            self.universal_fairy_chests.set(False)
            self.universal_chests.set(False)
            self.vendors.set("early")
            self.architect.set("early")
            self.architect_fee.set(0)
            self.disable_charon.set(True)
            self.require_purchasing.set(True)
            self.progressive_blueprints.set(False)
            self.gold_gain_multiplier.set("normal")
            self.number_of_children.set(5)
            self.free_diary_on_generation.set(True)
            self.khidr.set("vanilla")
            self.alexander.set("vanilla")
            self.leon.set("vanilla")
            self.herodotus.set("vanilla")
            self.health_pool.set(15)
            self.mana_pool.set(15)
            self.attack_pool.set(15)
            self.magic_damage_pool.set(15)
            self.armor_pool.set(10)
            self.equip_pool.set(10)
            self.crit_chance_pool.set(5)
            self.crit_damage_pool.set(5)
            self.allow_default_names.set(True)
            self.additional_lady_names.set([])
            self.additional_sir_names.set([])
            
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
            self.starting_gender.set("lady")
            self.starting_class.set("knight")
            
            _classes:list[str] = [
                "Barbarian",
                "Dragon",
                "Knave",
                "Knight",
                "Lich",
                "Mage",
                "Miner",
                "Shinobi",
                "Spellthief",
                "Traitor",
            ]
            self.available_classes.set(_classes)
            
            self.new_game_plus.set("normal")
            self.fairy_chests_per_zone.set(1)
            self.chests_per_zone.set(25)
            self.universal_fairy_chests.set(False)
            self.universal_chests.set(False)
            self.vendors.set("early")
            self.architect.set("early")
            self.architect_fee.set(40)
            self.disable_charon.set(False)
            self.require_purchasing.set(True)
            self.progressive_blueprints.set(True)
            self.gold_gain_multiplier.set("normal")
            self.number_of_children.set(3)
            self.free_diary_on_generation.set(True)
            self.khidr.set("vanilla")
            self.alexander.set("vanilla")
            self.leon.set("vanilla")
            self.herodotus.set("vanilla")
            self.health_pool.set(15)
            self.mana_pool.set(15)
            self.attack_pool.set(15)
            self.magic_damage_pool.set(15)
            self.armor_pool.set(10)
            self.equip_pool.set(10)
            self.crit_chance_pool.set(5)
            self.crit_damage_pool.set(5)
            self.allow_default_names.set(True)
            self.additional_lady_names.set([])
            self.additional_sir_names.set([])
            
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
            self.starting_gender.set("lady")
            self.starting_class.set("knight")
            
            _classes:list[str] = [
                "Barbarian",
                "Dragon",
                "Knave",
                "Knight",
                "Lich",
                "Mage",
                "Miner",
                "Shinobi",
                "Spellthief",
                "Traitor",
            ]
            self.available_classes.set(_classes)
            
            self.new_game_plus.set("normal")
            self.fairy_chests_per_zone.set(1)
            self.chests_per_zone.set(25)
            self.universal_fairy_chests.set(False)
            self.universal_chests.set(False)
            self.vendors.set("early")
            self.architect.set("early")
            self.architect_fee.set(40)
            self.disable_charon.set(False)
            self.require_purchasing.set(True)
            self.progressive_blueprints.set(True)
            self.gold_gain_multiplier.set("normal")
            self.number_of_children.set(3)
            self.free_diary_on_generation.set(True)
            self.khidr.set("vanilla")
            self.alexander.set("vanilla")
            self.leon.set("vanilla")
            self.herodotus.set("vanilla")
            self.health_pool.set(15)
            self.mana_pool.set(15)
            self.attack_pool.set(15)
            self.magic_damage_pool.set(15)
            self.armor_pool.set(10)
            self.equip_pool.set(10)
            self.crit_chance_pool.set(5)
            self.crit_damage_pool.set(5)
            self.allow_default_names.set(True)
            self.additional_lady_names.set([])
            self.additional_sir_names.set([])

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
        
        # now, we divide that by 21 * 4 = 84 and round up to know how many fairy chests we need
        fairyChestsPerZone:int = int(math.ceil(targetChecks / 84))
        runningTotal = runningTotal + (fairyChestsPerZone * 4)
        
        # and now we just divide by 4... right?
        chestsPerZone:int = int(math.ceil((targetChecks - runningTotal) / 4))
        
        # set relevant values
        self.chests_per_zone.set(chestsPerZone)
        self.fairy_chests_per_zone.set(fairyChestsPerZone)
        
    # self.reconfigure_duration(duration)
    # self.reconfigure_extra(extra)
    # self.reconfigure_end()

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