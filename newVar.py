class weapon:
    def __init__(self, name, damage, price, rarity):
        self.name = name
        self.damage = damage
        self.price = price
        self.rarity = rarity

# system variables
version = 1.0
rarities = ("common", "uncommon", "rare", "epic", "legendary", "mythic")
checkpointSecret = False
validPlayerClasses = ("wizard", "knight", "rogue", "armorer")

# user variables
username = "none"
playerClass = "none"
backpack = []
special = "none"
#weapon = weapon("none", 0, 0, rarities[0])
totHealth = "none"
curHealth = "none"

def varAssign():
    glob = globals()
    # variable assign
    print("enter a username")
    username = input()
    print(
    "Wizard\n baseHealth = 80\n base damage = 1\n special = fireball\n"
    "Knight\n baseHealth = 110\n base damage = 2\n special = strike\n"
    "Rogue\n baseHealth = 50\n base damage = 3\n special = slash\n"
    "Armorer\n baseHealth = 150\n base damage = 1\n special = shield\n"
    )
    print("enter a class")
    while True:
        playerClass = input()
        playerClass = playerClass.lower()
        if playerClass in validPlayerClasses:
            break
        else:
            print("invalid argument")
    if playerClass == "wizard":
        glob['backpack'] = ["glowing orb"]
        special = "spells"
        #weapon = weapon("wooden staff", 5, 0, rarities[0])
        totHealth = 80
        curHealth = totHealth
    elif playerClass == "knight":
        backpack = ["religious relic"]
        special = "strike"
        #weapon = weapon("wooden sword", 10, 0, rarities[0])
        totHealth = 110
        curHealth = totHealth
    elif playerClass == "rogue":
        backpack = ["silver fang"]
        special = "slash"
        #weapon = weapon("wooden dagger", 15, 0, rarities[0])
        totHealth = 50
        curHealth = totHealth
    elif playerClass == "armorer":
        backpack = ["golden plate"]
        special = "bash"
        #weapon = weapon("wooden shield", 5, 0, rarities[0])
        totHealth = 150
        curHealth = totHealth
