class weapon:
    def __init__(self, name, damage, price, rarity):
        self.name = name
        self.damage = damage
        self.price = price
        self.rarity = rarity

version = 1.0
rarities = ("common", "uncommon", "rare", "epic", "legendary", "mythic")
checkpointSecret = False
validPlayerClasses = ("wizard", "knight", "rogue", "armorer")

player = {

    "username" : "none",
    "playerClass" : "none",
    "money" : 0,
    "backpack" : [],
    "special" : "none",
    "weapon" : weapon("none", 0, 0, rarities[0]),
    "totalHealth" : 100,
    "currentHealth" : 100,

}

def varAssign(player):
    print("please enter a username:")
    player["username"] = input()
    print(
    "Wizard\n baseHealth = 80\n base damage = 1\n special = fireball\n"
    "Knight\n baseHealth = 110\n base damage = 2\n special = strike\n"
    "Rogue\n baseHealth = 50\n base damage = 3\n special = slash\n"
    "Armorer\n baseHealth = 150\n base damage = 1\n special = shield"
    )
    print("please enter a player class:")
    while True:
        player["playerClass"] = input()
        if player["playerClass"] in validPlayerClasses:
            break
        print("enter a valid argument")
    if player["playerClass"] == "wizard":
        player["backpack"].append("wizard orb")
        player["special"] = "spells"
        player["weapon"] = weapon("wooden staff", 5, 0, rarities[0])
        player["totalHealth"] = 80
        player["currentHealth"] = 80
    elif player["playerClass"] == "knight":
        player["backpack"].append("knight orb")
        player["special"] = "strike"
        player["weapon"] = weapon("wooden sword", 10, 0, rarities[0])
        player["totalHealth"] = 110
        player["currentHealth"] = 110
    elif player["playerClass"] == "rogue":
        player["backpack"].append("rogue orb")
        player["special"] = "slash"
        player["weapon"] = weapon("wooden dagger", 15, 0, rarities[0])
        player["totalHealth"] = 50
        player["currentHealth"] = 50
    elif player["playerClass"] == "armorer":
        player["backpack"].append("armorer orb")
        player["special"] = "bash"
        player["weapon"] = weapon("wooden shield", 5, 0, rarities[0])
        player["totalHealth"] = 150
        player["currentHealth"] = 150
        return player

def checkpoint():
    print("welcome to the checkpoint")
    print(
        "1 - save game",
        "2 - new game",
        "3 - load game",
        "4 - player stats",
        "5 - game help",
    )
    checkpointInput = input()
    match checkpointInput:
        case "0":
            print("you found a secret! +25 coins")
            player["money"] += 25
        case "1":
            pass
            #import json files
        case "2":
            pass
            #make new json file
        case "3":
            pass
            #load json file
        case "4":
            print(
                f"username = {player['username']}",
                f"player class = {player['playerClass']}",
                f"money = {player['money']}",
                f"items in backpack = {', '.join(player['backpack'])}",
                f"special = {player['special']}",
                f"total health = {player['totalHealth']}",
                f"current health = {player['currentHealth']}",
                "weapon stats//",
                f" name = {player['weapon'].name}"
                f" damage = {player['weapon'].damage}"
                f" price = {player['weapon'].price}"
                f" rarity = {player['weapon'].rarity}"
            )
        case "5":
            #read off of txt file
            pass
    