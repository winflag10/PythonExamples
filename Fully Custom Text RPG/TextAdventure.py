import sys, time, random, os
sys.path.insert(0,"data/game_struct/")
import classes , items ,rooms, enemies, map_gen, type_text# make this work
startroom = ""
######################################IGNORE DO NOT CHANGE ABOVE######################################



#Main Script
def __init__(game_dict):
    #Character definition
    player = classes.archer("John",game_dict[game_dict["startroom"]])
    player.room.examine()
    player.room.gen_map()
    player.move("e",game_dict)
    player.move("s",game_dict)

    
    user = input("which item would you like to pick up?")
    if user.lower() in game_dict["item_list"]:
        player.pickup(user)
    else:
        print("This is not an item")

    player.equip(sword)
    player.attack(player.room.enemies["skeleton"],game_dict)
    
    #actions
    print(player)











































######################################IGNORE DO NOT CHANGE BELOW######################################



def choose_game():
    path = "data/games/"
    games = os.listdir(path)
    print("Installed games:")
    for item in games:
        print(item)
    while True:
        user = input("\nWhich game would you like to play?\n>")
        if user.lower() in games:
            print("You have chosen to play:"+user)
            return "data/games/"+user
            break
        else:
            print("This is an invalid input please try again.")
            
def load_items(path):
    item_list = []
    f = open(path+"/items.txt","r")
    data = f.read()
    data = data.split(";")
    if data[len(data)-1] == "\n" or data[len(data)-1] == "\n\n" or data[len(data)-1] == "":
        del data[len(data)-1]
    loaded_items = []
    for item in data:
        item = item.split(":")
        item_list.append(item[1].lower().replace(" ","_").replace("\n",""))
        if item[0].strip("\n") == "consumable":
            vars()[item[1]] = items.consumable(item[1],item[2],item[3],item[4],item[5],item[6])
            loaded_items.append(vars()[item[1]])
        elif item[0].strip("\n") == "weapon":
            vars()[item[1]] = items.weapon(item[1],item[2],item[3],item[4],item[5],item[6])
            loaded_items.append(vars()[item[1]])
        elif item[0].strip("\n") == "quest_item":
            vars()[item[1]] = items.quest_item(item[1],item[2])
            loaded_items.append(vars()[item[1]])
        else:
            print("Error Item:"+item[1]+" not loaded correctly")
    return loaded_items,item_list

def load_enemies(path):
    enemy_list = []
    f = open(path+"/enemies.txt","r")
    data = f.read()
    data = data.split(";")
    if data[len(data)-1] == "\n" or data[len(data)-1] == "\n\n" or data[len(data)-1] == "":
        del data[len(data)-1]
    loaded_enemies = []
    for enemy in data:
        enemy = enemy.split(":")
        enemy[0] = enemy[0].strip("\n")
        enemy_list.append(enemy[0])
        vars()[enemy[0]] = enemies.enemy(enemy[0],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5],enemy[6],path)
        loaded_enemies.append(vars()[enemy[0]])
    return loaded_enemies,enemy_list
    
def load_rooms(path):
    f = open(path+"/rooms.txt","r")
    data = f.read()
    data = data.split(";")
    loaded_rooms = []
    if data[len(data)-1] == "\n" or data[len(data)-1] == "\n\n" or data[len(data)-1] == "":
        del data[len(data)-1]
    for room in data:
        room = room.split(",")
        room[0] = room[0].strip("\n")
        vars()[room[0]] = rooms.room(room[0],room[1],room[2],room[3],room[4],room[5],room[6],room[7],room[8])
        loaded_rooms.append(vars()[room[0]])
    return loaded_rooms


def load_start_room(path):
    global startroom
    with open(path+"/startroom.txt","r") as f:
        startroom = f.readline().replace(" ","").replace("\n","")
    
if __name__ == "__main__":
    item_list ,enemy_list = [] ,[]
    gamepath = choose_game()
    load_start_room(gamepath)
    for item in load_items(gamepath)[0]:
        vars()[item.name.lower().replace(" ","_").replace("(quest_item)","")] = item
    item_list = load_items(gamepath)[1]
    for enemy in load_enemies(gamepath)[0]:
        vars()[enemy.name] = enemy
    enemy_list = load_enemies(gamepath)[1]
    for room in load_rooms(gamepath):
        vars()[room.room_name] = room
        game_dict = vars()
        vars()[room.room_name].update(game_dict)
    game_dict = vars()
    __init__(game_dict)














