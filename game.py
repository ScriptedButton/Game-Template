import random

class Game:
    def __init__(self):
        self.xp = 50
        self.level = 0
        self.slain = 0
        self.damage = 0
        self.items = {"Sword":[0, 1], "Bow":[5, 2], "Gun":[10, 3], "Greatsword":[20, 4], "Master Sword":[50, 5]}
        self.inventory = []

    def menu(self):
        menu = """
        1) Enter the shop
        2) Enter the armory
        3) Enter the battlefield
        """
        print(menu)
        try:
            option = int(input("Select an option: "))
            if option == 1:
                self.shop()
            elif option == 2:
                self.armory()
            elif option == 3:
                self.pvp()
            else:
                print("Invalid option!")
            self.menu()
        except ValueError:
            print("Must be an integer!")
            self.menu()
    def pvp(self):
        enemies = random.randrange(1,20)
        for i in range(enemies):
            print("Total of", enemies, "enemies")
            health = random.randrange(1,20)
            while health > 0:
                fight = input("Swing your sword: ")
                if fight:
                    health -= self.damage
                    print("Swung!", health)
                else:
                    print("You retreat!")
                    self.menu()
            reward = random.randrange(1, 5)
            self.xp += reward
            self.level = .3 * self.xp
            print("Defeated!")
            self.slain += 1
            enemies -= 1
            print("-----" + "\n" + "Your Level: " + str(self.level) + "\n" + "Your XP: " + str(self.xp) + "\n" + "Total Slain: " + str(self.slain) + "\n" + "-----")
    def shop(self):
        print("Welcome to the shop!")
        print("We have a variety of items for you to select!")
        inv = self.inventory
        while True:
            print("You currently have", self.xp, "xp.")
            print("-- Shop Inventory --")
            for i in self.items:
                print("-", i, self.items[i][0])
            print("--------------------")
            item = input("Choose an item: ")
            try:
                if item in self.inventory:
                    sell = input("You already have this item, want to sell it: ")
                    if sell:
                        self.xp += self.items[item][0]
                        print("Sold!")
                        self.inventory.remove(item)
                    else:
                        break
                else:
                    if self.xp >= self.items[item][0]:
                        self.xp -= self.items[item][0]
                        print(item, "added to inventory!")
                        self.inventory.append(item)
                        break
                    else:
                        print("You cannot afford this item!")
                print("Your inventory:", inv)
            except KeyError:
                print("Invalid item!")

    def armory(self):
        print("Your inventory: ", self.inventory)
        item = input("Select an item to equip: ")
        self.damage = self.items[item][1]
        print("Damage of", item, ":", self.items[item][1])

# Start the game
g = Game()
g.menu()
