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

    def attack(self, other_team):
        ''' Battle each team against each other.'''

  
        while len([h for h in self.heroes if h.is_alive()]) > 0 and len([h for h in other_team.heroes if h.is_alive()]) > 0:
            friend = r.choice([h for h in self.heroes if h.is_alive()])
            foe = r.choice([h for h in other_team.heroes if h.is_alive()])
            friend.fight(foe)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print(hero.kills, hero.deaths)

    


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