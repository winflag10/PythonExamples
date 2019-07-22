class player():
    def __init__(self, name, start_room):
        #Dont Change
        self.name = name
        self.items = {}
        self.class_name = "default"
        self.ID = 0
        #Stats
        self.health = 10#current health stat
        self.strength = 5#added to dice roll for attacks
        self.speed = 5#added to dice roll for evade enemy chance
        self.max_health = 10#health before damage
        self.base_health = 10#original character health stat
        self.base_strength = 5
        self.base_speed = 5
        #Inventory
        self.inventory_slots_remaining = 10
        self.inventory_slots = 10
        #Xp Stats
        self.xp = 0
        self.level = 1
        self.next_lvl_mult = 1.2
        self.next_level_xp_base = 100
        self.xp_mult = 1
        self.max_level = 50
        #weapon
        self.equipped_weapon = None
        self.room = start_room
        
    def __repr__(self):
        if self.equipped_weapon != None:
            print_format = "\n====================\nName:"+self.name+"\nClass:"+self.class_name+"\nLevel:"+str(self.level)+"\nHealth:"+str(self.health)+"/"+str(self.max_health)+"\nStrength:"+str(self.strength)+"\nSpeed:"+str(self.speed)+"\nInventory slots:"+str(self.inventory_slots_remaining)+"/"+str(self.inventory_slots)+"\nItems:\n"+self.inventory()+"\nEquipped Weapon:"+str(self.equipped_weapon.name)+"("+str(self.equipped_weapon.damage)+" Damage)"+"\n===================="
        else:
            print_format = "\n====================\nName:"+self.name+"\nClass:"+self.class_name+"\nLevel:"+str(self.level)+"\nHealth:"+str(self.health)+"/"+str(self.max_health)+"\nStrength:"+str(self.strength)+"\nSpeed:"+str(self.speed)+"\nInventory slots:"+str(self.inventory_slots_remaining)+"/"+str(self.inventory_slots)+"\nItems:\n"+self.inventory()+"\nEquipped Weapon:None"+"\n===================="
        return(print_format)

    def level_check(self):
        if self.level == 1:
            xp_to_level = self.next_level_xp_base
        else:
            xp_to_level = self.next_level_xp_base * (self.next_lvl_mult ** self.level)
        while self.xp >= xp_to_level:
            if self.level == self.max_level:
                return
            if self.level == 1:
                xp_to_level = self.next_level_xp_base
            else:
                xp_to_level = self.next_level_xp_base * (self.next_lvl_mult ** self.level)
            self.xp -= xp_to_level
            self.level += 1
            print("\nYou leveled up!\nYou are now level "+str(self.level))
            if self.level == self.max_level:
                print("\nYou are now max level!")

    def give_xp(self, amount):
        print("You recieve "+str(amount)+" xp")
        self.xp += amount
        if self.level == self.max_level:
            return
        self.level_check()


    def set_stat(self, statID, value):#1:health 2:strength 3:speed 4:xp 5:level    #used later to allow for save loads
        value = int(value)
        statID = int(statID)
        if statID == 1:
            self.health = value
            print("Health set to "+str(value))
        elif statID == 2:
            self.strength = value
            print("Strength set to "+str(value))
        elif statID == 3:
            self.speed = value
            print("Speed set to "+str(value))
        elif statID == 4:
            self.xp = value
            print("Xp set to "+str(value))
        elif statID == 5:
            self.level = value
            print("level set to "+str(value))
        else:
            print("Invalid stat ID")


    def give_stat(self, statID, value):#1:health 2:strength 3:speed 4:xp 5:level    #used later to allow for save loads
        value = int(value)
        statID = int(statID)
        if statID == 1:
            self.heal(value)
        elif statID == 2:
            self.strength += value
            print("You gain "+str(value)+" Strength!")
        elif statID == 3:
            self.speed += value
            print("You gain "+str(value)+" Speed!")
        elif statID == 4:
            self.xp += value
            print("You gain "+str(value)+" Xp!")
        elif statID == 5:
            self.level += value
            if amount > 1:
                print("You gain "+str(value)+" Levels!")
            else:
                print("You gain "+str(value)+" Level!")
        else:
            print("Invalid stat ID")


    def heal(self, amount):
        if int(self.health) == int(self.max_health):
            print("\nyou do not need healing you are already max health!")
        else:
            if (int(self.health) + int(amount)) >= int(self.max_health):
                self.health = int(self.max_health)
                print("\nYou have been healed by "+str(amount)+" and are back to your starting quota of "+str(self.max_health)+" Health")
            else:
                self.health += int(amount)
                print("\nYou have been healed by "+str(amount)+"HP and are now on "+str(self.health)+"/"+str(self.max_health)+" Health")



    def damage(self, amount):
        if (self.health - amount) <= 0:
            self.health = 0
            print("\nYou recieve a finishing blow of "+str(amount)+" Points")
            self.kill()
        else:
            self.health -= amount
            print("\nYou have been damaged by "+str(amount)+" Points\nYou are now on "+str(self.health)+"/"+str(self.max_health)+" Health")


    def kill(self):
        #not finished, will drop non soulbound items in the room you are in and give different messages for different classes as well as reducing xp
        print("You are dead")

    def attack(self, enemy, game_dict):
        if self.equipped_weapon == None:
            damage = 1
        else:
            damage = int(self.equipped_weapon.damage)
        #enemy = game_dict[enemy]
        enemy.health = int(enemy.health)
        
        if self.speed > enemy.speed:
            if enemy.health > 0:
                print("\nYour speed is greater than the enemies so you attack first")
                enemy.health -= damage
                print("You attack the "+enemy.name+" for "+str(damage)+" damage")
            if enemy.health <= 0:
                print("\nThe "+enemy.name+" dies")
                self.give_xp(enemy.drop_xp())
                drops = enemy.drop_item()
                for item in drops:
                    self.give(game_dict[item])
                if drops == []:
                    pass
            if enemy.health > 0:
                self.health -= enemy.damage
                print("The "+enemy.name+" attacks you for "+str(enemy.damage)+" damage")
        else:
            if enemy.health > 0:
                self.health -= enemy.damage
                print("The "+enemy.name+" attacks you for "+str(enemy.damage)+" damage")
                enemy.health -= damage
                print("You attack the "+enemy.name+" for "+str(damage)+" damage")
            if enemy.health <= 0:
                print("\nThe "+enemy.name+" dies")
                self.give_xp(enemy.drop_xp())
                drops = enemy.drop_item()
                print(drops)
                for item in drops:
                    self.give(game_dict[item])

                if drops == []:
                    pass
        if enemy.health < 0:
            enemy.health = 0
        if enemy.health != 0:
            print("The "+enemy.name+" is now on "+str(enemy.health)+"/"+str(enemy.max_health)+" health")
            print("you are now on "+str(self.health)+"/"+str(self.max_health)+" health")
        if enemy.health <= 0:
            if str(enemy.boss) == "True" or str(enemy.boss) == "true":
                print("The "+enemy.name+" was sent back to its own dimension.")
                del self.room.enemies[enemy.name] 
            else:
                enemy.respawn()
        return
    
        

    def give(self, item):
        if self.inventory_slots_remaining >= int(item.space):
            print("You pick up a "+str(item.name))
            if item.name not in self.items:
                self.items[item.name] = item
            else:
                self.items[item.name].quantity += 1
            self.inventory_slots_remaining -= int(item.space)
        else:
            print("\nYou try to pick up a "+str(item.name)+" but you do not have enough inventory room for this item\nYou need "+str(item.space - self.inventory_slots_remaining)+" more inventory slots")
            self.room.add_item(item)

    def inventory(self):
        temp_inv = []
        for item in self.items.values():
            to_append = "-"+item.name + "(" + str(item.space) + " Inventory Slots) " + " x" + str(item.quantity)
            temp_inv.append(to_append)
        return(",\n".join(temp_inv))



    def drop(self, item):
        if item.soulbound:
            print("your "+item.name+" is soulbound you cant drop it")
            return
        if item.name not in self.items:
            print("You do not have a " + item.name + " to drop")
        else:
            self.inventory_slots_remaining += item.space
            if self.items[item.name].quantity > 1:
                self.items[item.name].quantity -= 1
            else:
                del self.items[item.name]
            print("\nYou drop a " + item.name)
            self.room.add_item(item)
            
    def remove_item(self, item):
        if item.name not in self.items:
            print("Player does not have a " + item.name + " to remove")
        else:
            self.inventory_slots_remaining += int(item.space)
            if self.items[item.name].quantity > 1:
                self.items[item.name].quantity -= 1
            else:
                del self.items[item.name]

    def add_item(self, item):
        if self.inventory_slots_remaining >= int(item.space):
            if item.name not in self.items:
                self.items[item.name] = item
            else:
                self.items[item.name].quantity += 1
            self.inventory_slots_remaining -= int(item.space)
        else:
            print("\nYou try to recieve a "+str(item.name)+" but you do not have enough inventory, it falls to the floor\nYou need "+str(item.space - self.inventory_slots_remaining)+" more inventory slots")
            self.room.add_item(item)
            
    def equip(self, weapon):#if in inv    #### make so this only works is strength is high enough for weapon power
        if self.equipped_weapon != None:
            self.dequip(self.equipped_weapon)
        self.equipped_weapon = weapon
        self.remove_item(weapon)
        print("\nYou equip a "+weapon.name+" \nThis Weapon does "+str(weapon.damage)+" Damage")

    def dequip(self):
        if self.equipped_weapon == None:
            pass
        else:
            print("\nYou dequip your "+self.equipped_weapon.name)
            self.add_item(self.equipped_weapon)
            self.equipped_weapon = None

    def equipped(self):
        print("\nWeapon currently equipped: " +str(self.equipped_weapon.name))
        if self.equipped_weapon != None:
            print("This Weapon does "+str(self.equipped_weapon.damage)+" Damage")
        
    def move(self, direction, game_dict):
        direction = direction.upper()
        if direction not in "NESW":
            print("This is an invalid direction")
        else:
            if direction == "N":
                if self.room.exits[0].lower() == "none":
                    print("There is no room in this direction")
                else:
                    self.room = game_dict[self.room.exits[0]]
            if direction == "E":
                if self.room.exits[1].lower() == "none":
                    print("There is no room in this direction")
                else:
                    self.room = game_dict[self.room.exits[1]]
            if direction == "S":
                if self.room.exits[2].lower() == "none":
                    print("There is no room in this direction")
                else:
                    self.room = game_dict[self.room.exits[2]]
            if direction == "W":
                if self.room.exits[3].lower() == "none":
                    print("There is no room in this direction")
                else:
                    self.room = game_dict[self.room.exits[3]]

    def pickup(self,item):# item name in str format
        if item in self.room.items:
            if self.inventory_slots_remaining > int(self.room.items[item].space):
                self.give(self.room.items[item])
                self.room.remove_item(item)
            else:
                print("You cannot pickup this item as you do not have enough inventory space")
        else:
            print("There is not a "+item+" in this room")


        
