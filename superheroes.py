import random as r

class Ability:

    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
          name:String
          attack_strength: Integer
       '''
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return r.randint(0, self.attack_strength)

class Armor:
    def __init__(self, name, max_block):
        ''' Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and max_block
        '''
        return r.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
            deaths: Integer
            kills: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

    def add_kill(self, num_kills):
        self.kills += num_kills
    
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
    
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        ''' Calculate the total damage from all ability attacks
            return: total: Integer
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def add_armor(self, armor):
        ''' Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(Armor(armor.name, armor.max_block))
    
    def defend(self):
        ''' Runs 'block' method on each armor.
            Returns sum of all blocks
        '''
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()

        return total_blocked

    def take_damage(self, damage):
        ''' Updates self.current_health to reflect the damage minus defense.
        '''
        damage_taken = damage - self.defend()
        self.current_health -= damage_taken

    def is_alive(self): 
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        '''Current Hero will take turns fighting ther opponent passed in.'''
        while self.is_alive() and opponent.is_alive():
    
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Draw")
                break

            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())


        if self.current_health > opponent.current_health:
            print(f"{self.name} Wins!!!")
            self.add_kill(1)
            opponent.add_deaths(1)
        else:
            print(f"{opponent.name} Wins!!!")
            self.add_deaths(1)
            opponent.add_kill(1)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

class Weapon(Ability):
    def attack(self):
        ''' Returns a random value between one half to the full attack power '''
        return r.randint(self.attack_strength//2, self.attack_strength)

class Team:
    def __init__(self, team_name):
        '''
            team_name: String
            heroes: List
        '''
        self.name = team_name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for i, hero in enumerate(self.heroes):
            if hero.name == name:
                self.heroes.pop(i)
                break
        #Hero not found
        else:
            return 0 

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    #helper function
    def alive_heroes(self):
        alive_heroes = []
        for h in self.heroes:
            if h.is_alive():
                alive_heroes.append(h)
        return alive_heroes

                

    def attack(self, other_team):
        ''' Battle each team against each other.'''

  
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            friend = r.choice(self.alive_heroes())
            foe = r.choice(other_team.alive_heroes())
            friend.fight(foe)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print(hero.kills, hero.deaths)

class Arena:
    def __init__(self):
        '''Instantiate properties
                team_one: Team
                team_two: Team
        '''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")
    
    def create_ability(self):
        '''Prompt for Ability information'''
        name = input("Enter an ability name: ")
        strength = int(input("Enter ability strength: "))
        return Ability(name, strength)

    def create_weapon(self):
        '''Prompt user for Weapon information'''
        name = input("Enter a Weapon Name ")
        strength = int(input("Enter weapon strength: "))
        return Weapon(name, strength)

    def create_armor(self):
        '''Prompt user for Armor information'''
        name = input("Enter a Weapon Name ")
        strength = int(input("Enter armor block: "))
        return Armor(name, strength)

    def create_hero(self):
        name = input("Enter a hero name: ")
        hero = Hero(name)
        hero.add_ability(self.create_ability())
        hero.add_armor(self.create_armor())
        hero.add_weapon(self.create_weapon())
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        count = int(input("Enter # of heroes for team 1: "))

        while(count>0):
            self.team_one.heroes.append(self.create_hero())
            count -= 1

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        count = int(input("Enter # of heroes for team 2: "))
        team_two = Team("Team Two")
        while(count>0):
            team_two.heroes.append(self.create_hero())
            count -= 1

    def team_battle(self):
        '''Battle team_one and team_two together'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal'''
                # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        if len(self.team_one.alive_heroes()) > 0:
            print("Team One Wins!")
        else:
            print("Team Two Wins!")
        self.team_one.stats()
        self.team_two.stats()
        self.team_one.alive_heroes()
        self.team_two.alive_heroes()


    


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
