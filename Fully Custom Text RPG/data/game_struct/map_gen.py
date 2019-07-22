item_symbol = "*" 
enemy_symbol = "x"
boss_symbol = "?"
final_room_symbol = "!"


def display(room_map, exits_gen, whitespace):
    for i in room_map:
        print(whitespace*" " + i)
    for i in exits_gen:
        print(i)

def generate_symbols(item, enemy, boss, final_room):#takes true or false and generates symbols
    global item_symbol, final_room_symbol, enemy_symbol, boss_symbol 
    room_map =[" ----- ","|     |","|     |"," ----- "]
    if (item) and (not enemy):
        room_map[1] = "|  "+item_symbol+"  |"
    if (enemy) and (not item):
        room_map[1] = "|  "+enemy_symbol+"  |"
    if item and enemy:
        room_map[1] = "| "+item_symbol+" "+enemy_symbol+" |"
    if (boss) and (not final_room):
        room_map[2] = "|  "+boss_symbol+"  |"
    if (final_room) and (not boss):
        room_map[2] = "|  "+final_room_symbol+"  |"
    if boss and final_room:
        room_map[2] = "| "+boss_symbol+" "+final_room_symbol+" |"
    return(room_map)

def generate_exits(room_map, exits):#takes a map with symbols and exits and modifies map to have exits on
    exits_gen = []
    N, E, S, W = exits[0], exits[1], exits[2], exits[3]
    exits_gen.append("      N       "+(5+len(W)-(len(N)//2))*" " + N)
    exits_gen.append("      ˄       "+((5 + len(W)) * " ") + "˄")
    exits_gen.append("  W <   > E   "+"  " + W + " <   > " + E)
    exits_gen.append("      ˅       "+((5 + len(W)) * " ") + "˅")
    exits_gen.append("      S       "+(5+len(W)-(len(S)//2))*" " + S)
    return exits_gen, (16+len(W))



def gen_map(exits, item, enemy, boss, final_room):
    room_map = generate_symbols(item, enemy, boss, final_room)
    exits_gen, whitespace = generate_exits(room_map, exits)
    display(room_map, exits_gen, whitespace)

def gen_map_from_room(room): # pass in a room and have the gen_map parameters worked out for you
    boss = 0
    if room.items == {}:
        item = 0
    else:
        item = 1
    if room.enemies == {}:
        enemy = 0
    else:
        enemy = 1
    #boss = 0
    #for enemy in room.enemies:
    #    if enemy.boss:
    #        boss = 1
    if room.is_end in ["1",True,"True"]:
        final_room = 1
    else:
        final_room = 0
    gen_map(room.exits, item, enemy, boss, final_room)

if __name__ == "__main__":
    exits = ["TopMiddle","MiddleRight","BottomMiddle","MiddleLeft"]
    #exits = ["Top","Right","Bottom","Left"]
    item,enemy,boss,final_room = 1,0,1,0
    gen_map(exits, item, enemy, boss, final_room)







