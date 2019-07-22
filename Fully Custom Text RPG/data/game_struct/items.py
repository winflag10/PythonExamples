class item():
    def __init__(self):
        self.item_no = 0
        self.soulbound = False
        self.name = "default"
        self.stat = 0
        self.quantity = 1
        self.space = 1
        self.amount = 0
        self.consumable = False


    def __repr__(self):
        return ("\nThis is the default description")
########################################################################

    
class consumable(item):
    def __init__(self, name, stat, amount, space, soulbound, desc):
        item.__init__(self)
        self.name = name
        self.stat = stat
        self.amount = amount
        self.space = space
        self.soulbound = soulbound
        self.desc = desc
        self.consumbale = True
    def __repr__(self):
        return(self.desc)

    def consume(self, player):
        if self.name not in player.items:
            print("You do not have a " + self.name + " to use")
        else:
            player.inventory_slots_remaining += int(self.space)
            if player.items[self.name].quantity > 1:
                player.items[self.name].quantity -= 1
            else:
                del player.items[self.name]
            print("\nYou use a " + self.name)
            player.give_stat(int(self.stat),self.amount)

class weapon(item):
    def __init__(self, name, damage, ranged, space, soulbound, desc):
        item.__init__(self)
        self.name = name
        self.damage = damage
        self.space = space
        self.soulbound = soulbound
        self.desc = desc
        self.ranged = ranged
        
    def __repr__(self):
        return(self.desc)

class quest_item(item):
    def __init__(self, name, desc):
        item.__init__(self)
        self.name = name+"(Quest Item)"
        self.space = 0
        self.soulbound = True
        self.desc = desc

    def __repr__(self):
        return(self.desc)
