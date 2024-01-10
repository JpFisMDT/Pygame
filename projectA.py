class Hero:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.mana = 100
        self.point = 0

    def __str__(self):
        return f" {self.name} : {self.hp} Health Point, {self.atk} Attack Point, {self.mana} Mana Point and {self.defense} Defense Point."

    def heavy_attack(self, other):
        self.mana -= 50
        damage = (self.atk * 5) / other.defense
        other.hp -= damage
        print(f"{self.name} deals {damage} damage to {other.name}.")

    def attack(self, other):
        self.mana -= 20
        damage = (self.atk) / other.defense
        other.hp -= damage
        print(f"{self.name} deals {damage} damage to {other.name}.")

    def defend(self):
        self.defense += 1
        print(f"{self.name} raises defense to {self.defense}.")

    def raise_attack(self):
        self.atk += 30
        print(f"{self.name} raise attack to {self.atk}")


class Tournament:
    def __init__(self, name, place, atk_mod, def_mod, hp_mod):
        self.name = name
        self.player1 = 0
        self.player2 = 0
        self.turn_limit = 20
        self.place = place
        self.atk_mod = atk_mod
        self.def_mod = def_mod
        self.hp_mod = hp_mod

    def __str__(self):
        return f"The tournament name is {self.name}, held in {self.place}! \n Adjustment details: ATK modified by {self.atk_mod}, DEF modified by {self.def_mod}, HP modified by {self.hp_mod}!"

    def pick_hero(self):
        i = 0
        while i < len(heroes):
            print(f"  {i+1}. {heroes[i]}")
            i += 1
        while True:
            self.player1 = int(input("Player 1 pick a hero: "))
            if self.player1 > len(heroes):
                print("Hero not found please choose again!")
                continue
            print(f"Player one has pick {heroes[self.player1 - 1].name}")
            self.player1 = heroes[self.player1 - 1]
            self.player1 = Hero(self.player1.name, self.player1.hp,
                                self.player1.atk, self.player1.defense)
            break
        i = 0
        while i < len(heroes):
            print(f"  {i+1}. {heroes[i]}")
            i += 1
        while True:
            self.player2 = int(input("Player 2 pick a hero: "))
            if self.player2 > len(heroes):
                print("Hero not found please choose again!")
                continue
            print(f"Player two has pick {heroes[self.player2 - 1].name}")
            self.player2 = heroes[self.player2 - 1]
            self.player2 = Hero(self.player2.name, self.player2.hp,
                                self.player2.atk, self.player2.defense)
            break
        self.turn_limit = int(input("Enter turn limit(maximum 20): "))
        if self.turn_limit < 0 or self.turn_limit > 20:
            print("You have entered invalid number, your turn is set to 20!")
            self.turn_limit = 20
        self.player1.hp += self.hp_mod
        self.player1.atk += self.atk_mod
        self.player1.defense += self.def_mod
        self.player2.hp += self.hp_mod
        self.player2.atk += self.atk_mod
        self.player2.defense += self.def_mod

    def combat(self):

        print("                                                 Battle Begin!")
        while self.player1.hp > 0 and self.player2.hp > 0:
            if self.turn_limit == 0:
                if self.player1.hp > self.player2.hp:
                    print("Player 1 wins the battle!")
                    self.player1.point += 1
                elif self.player2.hp > self.player1.hp:
                    print("Player 2 wins the battle!")
                    self.player2.point += 1
                else:
                    print("Battle Draw!")
                break
            print(f"{self.turn_limit} turns left")
            print(
                f"{self.player1.name} (HP: {self.player1.hp}) MP: {self.player1.mana} vs {self.player2.name} (HP: {self.player2.hp}) MP: {self.player2.mana}")
            while True:
                print("Player 1's turn:")
                skill1 = int(
                    input("Choose a skill for Player 1 (1: Attack, 2: Heavy Attack, 3: Defend, 4: Raise Attack): "))
                if skill1 == 1:
                    if self.player1.mana < 10:
                        print("Not enough mana, choose another skill")
                        continue
                    else:
                        self.player1.attack(self.player2)
                        print("Not enough mana, choose another skill")
                        break
                elif skill1 == 2:
                    if self.player1.mana < 40:
                        continue
                    else:
                        self.player1.heavy_attack(self.player2)
                        break
                elif skill1 == 3:
                    self.player1.defend()
                    break
                elif skill1 == 4:
                    self.player1.raise_attack()
                    break
                else:
                    print("Invalid input, choose another skill")
            if self.player2.hp <= 0:
                print("Player 1 wins the battle!")
                self.player1.point += 1
                break
            while True:
                print("Player 2's turn:")
                skill2 = int(
                    input("Choose a skill for Player 2 (1: Attack, 2: Heavy Attack, 3: Defend, 4: Raise Attack): "))
                if skill2 == 1:
                    if self.player2.mana < 10:
                        print("Not enough mana, choose another skill")
                        continue
                    else:
                        self.player2.attack(self.player1)
                        print("Not enough mana, choose another skill")
                        break
                elif skill2 == 2:
                    if self.player2.mana < 40:
                        continue
                    else:
                        self.player2.heavy_attack(self.player1)
                        break
                elif skill2 == 3:
                    self.player2.defend()
                    break
                elif skill2 == 4:
                    self.player2.raise_attack()
                    break
                else:
                    print("Invalid input, choose another skill")
            if self.player1.hp <= 0:
                print("Player 2 wins the battle!")
                self.player2.point += 1
                break

            self.turn_limit -= 1
            self.player1.mana += 20
            self.player2.mana += 20


# Scenario ------------------------------
hero1 = Hero("John", 100, 30, 8)
hero2 = Hero("Mike", 180, 40, 4)
hero3 = Hero("Tom", 130, 50, 4)
hero4 = Hero("Tim", 80, 70, 3)
heroes = [hero1, hero2, hero3, hero4]
fight1 = Tournament("Street Fight", "Sydney", 0, 0, 0)
fight2 = Tournament("Underground Fight", "New York", -20, 3, 30)
fight3 = Tournament("Subway Fight", "London", 50, 1, 0)
fight4 = Tournament("Super Fight", "Paris", 0, 3, 100)
fights = [fight1, fight2, fight3, fight4]
print("Welcome to 2023 combat game!")
play = input("Enter y to play(other for quit): ")
point1 = 0
point2 = 0
while play == "y":
    count = 1
    for t in fights:
        print(f"{count}. {t}")
        count += 1
    tour = int(input("Pick the tournament: "))
    if tour > len(fights):
        print("Invalid input!")
        continue
    tour = fights[tour-1]
    print(f"You have picked {tour.name}!")
    tour.pick_hero()
    tour.combat()
    if tour.player1.point > 0:
        point1 += 1
    elif tour.player2.point > 0:
        point2 += 2
    print(
        f"Player 1: {point1} point   VS   Player 2: {point2} point")
    play = input("Enter y to continue or other to exit: ")
print("Game end!")
