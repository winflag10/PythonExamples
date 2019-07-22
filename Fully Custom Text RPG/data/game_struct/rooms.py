class room:
    def __init__(self, room_name, desc,N,E,S,W,is_end,items_to_add,enemies_to_add):
        
        self.items = {}
        self.enemies = {}
        self.items_to_add = items_to_add.split("+")
        self.enemies_to_add = enemies_to_add.split("+")
        self.exits = [N,E,S,W]
        self.is_end = is_end
        self.desc = desc
        self.room_name = room_name
        

    def enterable(self, player):
        return True
        #if player.level >= 5:
        #    return True
        #else:
        #    return False

    def __repr__(self):
        return self.desc


    def update(self, game_dict):
        for item in self.items_to_add:
            if item != "0" and item != 0:
                self.add_item(game_dict[item.lower().replace(" ","_").replace("\n","")])
        for enemy in self.enemies_to_add:
            if enemy != "0" and enemy != 0:
                self.add_enemy(game_dict[enemy.lower().replace(" ","_").replace("\n","")])
    
    def add_item(self, item):
        if item.name not in self.items:
            self.items[item.name] = item
        else:
            self.items[item.name].quantity += 1

    def add_enemy(self, enemy):
        if enemy.name not in self.enemies:
            self.enemies[enemy.name] = enemy
        else:
            self.enemies[enemy.name].quantity += 1

    def examine(self):
        print(self.desc)
        if self.items == {}:
            print("There are no items in this room")
        else:
            print("Items in this room:")
            for item in self.items.keys():
                print(item)
        if self.enemies == {}:
            print("There are no enemies in this room")
        else:
            print("Enemies in this room:")
            for enemy in self.enemies.keys():
                print(enemy)

    def remove_item(self,item):
        if self.items[item].quantity > 1:
            self.items[item].quantity -= 1
        else:
            del self.items[item]


    def gen_map(self):
        import map_gen
        map_gen.gen_map_from_room(self)











        




    
