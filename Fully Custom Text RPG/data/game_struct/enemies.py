class enemy:
    def __init__(self, name, boss, xp, health, damage, speed, entry_desc, gamepath):
        import os
        self.name = name
        path = os.path.dirname(os.getcwd())+"/TextAdventure V2.0/"+gamepath+"/drop_tables/"+self.name+".txt"
        self.boss = boss
        self.xp = int(xp)
        self.speed = int(speed)
        self.health = int(health)
        self.max_health = int(health)
        self.damage = int(damage)
        self.entry_desc = entry_desc
        self.drop_table = open(path,"r").read().replace("/n","").replace(" ","")


    def __repr__(self):
        return self.entry_desc

    def drop_item(self):
        import random
        drops = []
        try:
            self.drop_table = self.drop_table.split(";")
        except:
            pass
        if self.drop_table[len(self.drop_table)-1] == "" or self.drop_table[len(self.drop_table)-1] == "\n":
            del self.drop_table[len(self.drop_table)-1]
        for item in self.drop_table:
            item = item.split(":")
            choice_list = []
            item[1] = float(item[1]) * 10
            for i in range(int(item[1])):
                choice_list.append(True)
            for i in range(1000-int(item[1])):
                choice_list.append(False)
            if random.choice(choice_list):
                drops.append(item[0])
        return drops

    def drop_xp(self):
        import random
        xp = self.xp
        return random.randrange(self.xp)+1
        
    def respawn(self):
        print("\nThe "+self.name+" respawns")
        self.health = self.max_health


