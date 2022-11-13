"""
# user variables

print(user.username)
print(user.playerClass)
print(user.backpack)
print(user.special)
print(user.totalHealth)
print(user.currentHealth)
print(user.money)

# user.weapon variables

print(user.weapon.name)
print(user.weapon.damage)
print(user.weapon.price)
print(user.weapon.rarity)

# var variables

print(version)
print(rarities)
print(checkPointSecret)
print(validPlayerClasses)
"""
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


# spaghetti code
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
    playerClass.lower()
    if playerClass in validPlayerClasses:
        break
    else:
        print("invalid argument")
if playerClass == "wizard":
    backpack = ["glowing orb"]
    special = "spells"
    weapon = weapon("wooden staff", 5, 0, rarities[0])
    totalHealth = 80
    currentHealth = totalHealth
elif playerClass == "knight":
    backpack = ["religious relic"]
    special = "strike"
    weapon = weapon("wooden sword", 10, 0, rarities[0])
    totalHealth = 110
    currentHealth = totalHealth
elif playerClass == "rogue":
    backpack = ["silver fang"]
    special = "slash"
    weapon = weapon("wooden dagger", 15, 0, rarities[0])
    totalHealth = 50
    currentHealth = totalHealth
elif playerClass == "armorer":
    backpack = ["golden plate"]
    special = "bash"
    weapon = weapon("wooden shield", 5, 0, rarities[0])
    totalHealth = 150
    currentHealth = totalHealth