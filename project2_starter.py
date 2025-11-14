"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Kami Strain
Date: 11/14

AI Usage: - Improving stamina logic with attacks
          - Assisting with debugging method
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================
import random

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        # TODO: Set the character's name, health, strength, and magic
        # These should be stored as instance variables
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        # TODO: Implement basic attack
        damage = self.strength # Damage should be based on self.strength
        print(f"\n{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage) # Use target.take_damage(damage) to apply damage

        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        # TODO: Implement taking damage
        self.health -= damage# Reduce self.health by damage amount
        if self.health < 0:
            self.health = 0 # Make sure health doesn't go below 0
        print(f"\n{self.name} takes {damage} damage! (Health: {self.health})")

        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        print(f"\n{self.name} current stats:")
        print(f"\tHealth: {self.health} | Strength: {self.strength} | Magic: {self.magic}")

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        # Call super().__init__() with the basic character info
        super().__init__(name, health, strength, magic)
        # Store the character_class (like "Warrior", "Mage", etc.)
        self.character_class = character_class
        # Add any other player-specific attributes (level, experience, etc.)
        self.level = 1 # Player level starts at 1
        self.experience = 0 # Player experience starts at 0
        self.stamina = 100 # Player stamina starts at 100 (decreases per attack)

    def gain_experience(self, amount):
        """
        Increase player's experience by a certain amount.
        Automatically handles leveling up every 100 XP.
        """
        self.experience += amount
        print(f"{self.name} gains {amount} XP! (Total XP: {self.experience})")
        # Level up
        while self.experience >= 100:
            self.experience -= 100
            self.level += 1
            print(f"🎉 {self.name} leveled up! Now level {self.level}!")

        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        # Call the parent's display_stats method using super()
        # Print additional stats
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | XP: {self.experience} | Stamina: {self.stamina}")


class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        # Call super().__init__() with warrior-appropriate stats
        super().__init__(name, "Warrior", 120, 15, 5)

        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # Checks if character isn't too tired to attack
        if self.stamina <= 0:
            print(f" {self.name} is too exhausted to attack!")
            return
        stamina_cost = 5
        # This character class does more damage than basic attack ( +5 bonus damage)
        damage = self.strength + 5

        print(f"\n{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

        # Updates and displays stamina
        self.stamina = max(0, self.stamina - stamina_cost)
        print(f"{self.name}'s stamina decreases by {stamina_cost}. (Remaining: {self.stamina})")

        # Player gains experience when attacking.
        self.gain_experience(25)

        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        # The power strike does significantly more damage than regular attack
        stamina_cost = 15    # It also takes more stamina than a regular attack
        if self.stamina < stamina_cost:
            print(f"{self.name} does not have enough stamina forPower Strike!")
            return

        damage = self.strength + 20
        print(f"\n{self.name} uses POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)

        # Update and displays stamina
        self.stamina = max(0, self.stamina - stamina_cost)
        print(f"{self.name}'s stamina decreases by {stamina_cost}. (Remaining: {self.stamina})")

        # Player gains experience when attacking. (Special attack gives extra experience)
        self.gain_experience(35)

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        # Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        super().__init__(name, "Mage", 80, 8, 20)
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        # Uses self.magic for damage calculation instead of strength
        if self.stamina <= 0:
            print(f" {self.name} is too exhausted to cast spells!")
            return

        stamina_cost = 8
        damage = self.magic
        print(f"\n{self.name} casts a magic spell on {target.name} for {damage} damage!")
        target.take_damage(damage)

        # Update and display stamina
        self.stamina = max(0, self.stamina - stamina_cost)
        print(f"{self.name}'s stamina decreases by {stamina_cost}. (Remaining: {self.stamina})")

        # Player gains experience when attacking.
        self.gain_experience(17)
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        # Does magic-based damage with bonus
        stamina_cost = 20
        if self.stamina < stamina_cost:
            print(f" {self.name} doesn't have enough stamina for Fireball!")
            return

        damage = self.magic + 10
        print(f"{self.name} hurls a Fireball at {target.name} for {damage} damage!")
        target.take_damage(damage)

        self.stamina = max(0, self.stamina - stamina_cost)
        print(f"{self.name}'s stamina decreases by {stamina_cost}. (Remaining: {self.stamina})")

        # Player gains experience when attacking. (Special attack gives extra experience)
        self.gain_experience(30)

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        # Suggested stats: health=90, strength=12, magic=10
        super().__init__(name, "Rogue", 90, 12, 10)
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        if self.stamina <= 0:
            print(f" {self.name} is too exhausted to attack!")
            return

        stamina_cost = 7
        damage = self.strength
        if random.randint(1,10) <= 3:
            damage *= 2
            print(f"CRITICAL HIT! {self.name} strikes {target.name} for {damage} damage!")
        else:
            print(f"{self.name} charges at {target.name} for {damage} damage!")
        target.take_damage(damage)

        # Update and display stamina
        self.stamina = max(0, self.stamina - stamina_cost)
        print(f"{self.name}'s stamina decreases by {stamina_cost}. (Remaining: {self.stamina})")

        # Player gains experience when attacking.
        self.gain_experience(15)
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        # Always does critical damage
        stamina_cost = 20
        if self.stamina < stamina_cost:
            print(f" {self.name} doesn't have enough stamina for Fireball!")
            return

        damage = self.strength * 2
        print(f"{self.name} performs a swift Sneak Attack on {target.name} for {damage} damage!")
        target.take_damage(damage)

        self.stamina = max(0, self.stamina - stamina_cost)
        print(f"{self.name}'s stamina decreases by {stamina_cost}. (Remaining: {self.stamina})")

        # Player gains experience when attacking. (Special attack gives extra experience)
        self.gain_experience(27)


class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        # Store weapon name and damage bonus
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        # Print weapon name and damage bonus
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)

    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    axe = Weapon("Heavy Axe", 12)
    crossbow = Weapon("Single-Shot Crossbow", 15)

    sword.display_info()
    staff.display_info()
    dagger.display_info()
    axe.display_info()
    crossbow.display_info()
    
    # TODO: Test the battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
