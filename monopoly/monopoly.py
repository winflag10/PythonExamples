import random,time
class game():
    def __init__(self,spaces,*players):
        self.players = players
        self.board_list = ["  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  "]
        self.update()
        self.spaces = spaces
    def display(self):
        print(self.board)
    def clear_screen(self):
        for i in range(100):
            print("\n")
    def turn(self):
        for player in self.players:
            player.turn(spaces)
    def update(self):
        #update house positions here
        for player in self.players:
            if self.board_list[player.prev_pos%40] == player.symbol+" ":
                self.board_list[player.prev_pos] = "  "
            self.board_list[player.pos%40] = player.symbol+" "
        self.board = """
    |   |   |   |   |   |   |   |   |   |      
 {} | {}| {}| {}| {}| {}| {}| {}| {}| {}| {}
― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― 
 {} |                                   | {}
― ― |      ___                          | ― ―
 {} |     / c /                         | {}
― ― |    / c /                          | ― ―
 {} |   / c /                           | {}
― ― |    ¯¯¯                            | ― ―
 {} |                                   | {}
― ― |            Monopoly!              | ― ―
 {} |                                   | {}
― ― |                                   | ― ―
 {} |                         ___       | {}
― ― |                        / ? /      | ― ―
 {} |                       / ? /       | {}
― ― |                      / ? /        | ― ―
 {} |                       ¯¯¯         | {}
― ― |                                   | ― ―
 {} |                                   | {}
― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― 
 {} | {}| {}| {}| {}| {}| {}| {}| {}| {}| {}  
    |   |   |   |   |   |   |   |   |   |           
        """.format(self.board_list[0],self.board_list[1],self.board_list[2],self.board_list[3],self.board_list[4],self.board_list[5],self.board_list[6],self.board_list[7],self.board_list[8],self.board_list[9],self.board_list[10],self.board_list[39],self.board_list[11],self.board_list[38],self.board_list[12],self.board_list[37],self.board_list[13],self.board_list[36],self.board_list[14],self.board_list[35],self.board_list[15],self.board_list[34],self.board_list[16],self.board_list[33],self.board_list[17],self.board_list[32],self.board_list[18],self.board_list[31],self.board_list[19],self.board_list[30],self.board_list[29],self.board_list[28],self.board_list[27],self.board_list[26],self.board_list[25],self.board_list[24],self.board_list[23],self.board_list[22],self.board_list[21],self.board_list[20])
    

class player():
    def __init__(self,symbol="x"):
        self.symbol = symbol
        self.pos = 20
        self.prev_pos = 0
        self.bal = 1500
        self.double_count = 0
        self.properties = []
        self.in_jail = False
        self.GOOJF = 0
    def __repr__(self):#EXPAND THIS
        return """
---Profile---
Symbol:{}
Balance:{}
Get out of jail free cards:{}
Properties:{}
-------------
""".format(self.symbol,self.bal,self.GOOJF,self.properties)
        return self.symbol
    def __str__(self):
        return self.__repr__()
    def turn(self,spaces):
        while True:
            print("It is "+self.symbol+"'s turn")
            choice = input("Enter 1 to roll\nEnter 2 to view your profile\nEnter 3 to build property\n>")
            if choice == "1":
                break
            elif choice == "2":
                print(self)
            elif choice == "3":
                print("Houses not implemented yet")
            else:
                print("Invalid Input")
        self.roll1 = random.randrange(1,7)
        self.roll2 = random.randrange(1,7)
        self.roll = self.roll1+self.roll2
        print("\nplayer",self.symbol,"rolled a",str(self.roll1),"and a",str(self.roll2),"Total:",self.roll) 
        self.prev_pos = self.pos
        self.pos = (self.pos + self.roll)%40
        if self.prev_pos < 20 and self.pos >= 20:
            print("Advanced past GO, collected $200")
            self.bal += 200
        self.land(spaces)
        g.update()
        g.display()
        if self.roll1 == self.roll2:
            print("player",self.symbol,"rolled doubles so gets another turn")
            self.double_count += 1
            self.turn(spaces)
        else:
            self.double_count = 0#SEND TO JAIL IF 3 DOUBLES
    def land(self,spaces):
        print("player "+self.symbol+" landed on "+str(spaces[self.pos]))
        while True:
            if spaces[self.pos].am_property:
                if not spaces[self.pos].owned == True:
                    choice = input("Would you like to purchase this property?(y/n)\n>").lower()
                    if choice == "y":
                        if self.bal >= spaces[self.pos].price:
                            spaces[self.pos].owned = True
                            spaces[self.pos].owner = self
                            self.bal -= spaces[self.pos].price
                            self.properties.append(spaces[self.pos])
                            print("Player "+self.symbol+" purchased "+spaces[self.pos].name+" for $"+str(spaces[self.pos].price)+" and now has $"+str(self.bal)+ " left")
                            break
                        else:
                            print("Player "+self.symbol+" tried to purchase "+spaces[self.pos].name+" but can't afford it with current balance of $"+str(self.bal))
                            break
                    elif choice == "n":
                        print("Purchase rejected")
                        break
                    else:
                        print("Invalid Input")
                        continue
                else:
                    break
            else:
                break
        spaces[self.pos].call_event(self)
        if spaces[self.pos].am_property:
            if spaces[self.pos].owned == True and spaces[self.pos].owner != self:
                print("landed on another players square")
                if spaces[self.pos].group_id == "Station":
                    rent = 10#FIX THIS RENT SYSTEM
                    self.bal -= rent
                    spaces[self.pos].owner.bal += rent
                    print("Owner payed $"+str(rent)+" player "+self.symbol+ " new balance:$"+str(self.bal))
                elif spaces[self.pos].group_id == "Utility":
                    rent = 10
                    self.bal -= rent
                    spaces[self.pos].owner.bal += rent
                    print("Owner payed $"+str(rent)+" player "+self.symbol+ " new balance:$"+str(self.bal))
                else:
                    rent = spaces[self.pos].calc_rent()
                    self.bal -= rent
                    spaces[self.pos].owner.bal += rent
                    print("Owner payed $"+str(rent)+" player "+self.symbol+ " new balance:$"+str(self.bal))
        
        
class space():
    def __init__(self,name,am_property,event="community chest",price=0,group_id="NOT SET",rent=0,house1=0,house2=0,house3=0,house4=0,hotel=0,mortgage=0,house_price=0,hotel_price=0):
        self.name = "\n"+name
        self.am_property = am_property
        self.price = price
        self.group_id = group_id
        self.chance_cards = ["trafalgar","jail","pall_mall","repairs","fine15","collect150","kingscross","go","collect50","mayfair","back3","GOOJF","payall50"]
        self.used_chance = []
        self.community_chest_cards = ["GOOJF","repairs","collect25","collect200","collectall10","collect100","collect100","pay50","go","collect50","jail","pay50","pay100"]
        self.used_community_chest = []
        if am_property:
            self.owned = False
            self.owner = None
        self.event =event
        self.prices = [rent,house1,house2,house3,house4,hotel]
        self.mortgage = mortgage
        self.house_price = house_price
        self.hotel_price = hotel_price
        self.house_no = 0
    def __repr__(self):
        if self.am_property:
            to_return = str(self.name)+"\n-Group:"+str(self.group_id)
            if not self.owned:
                to_return += "\n-Not Owned\n-Cost:$"+str(self.price)
            else:
                to_return += "\n-Owned by "+self.owner.symbol
            return to_return
        else:
            return self.name
    def call_event(self,player):
        if self.event is not None:
            if self.event == "tax100":
                player.bal -= 100
                print(player.symbol+" has been fined $100, new balance:$"+str(player.bal))
            elif self.event == "tax200":
                player.bal -= 200
                print(player.symbol+" has been fined $200, new balance:$"+str(player.bal))
            elif self.event == "chance":
                random.shuffle(self.chance_cards)
                chosen = self.chance_cards.pop(0)
                self.used_chance.append(chosen)
                print("chance card drawn")
                self.card(chosen,player)
            elif self.event == "community chest":
                random.shuffle(self.community_chest_cards)
                chosen = self.community_chest_cards.pop(0)
                self.used_community_chest.append(chosen)
                print("community chest drawn")
                self.card(chosen,player)
            elif self.event == "go to jail":
                print("Player "+player.symbol+" moved to jail")
                player.pos = 30
                g.update()
            else:
                print("event "+self.event+" not coded")
    def card(self,card,player):
        if card == "trafalgar":
            print("Card:Go to Trafalgar Square")
            player.pos = 4
            player.land(g.spaces)
        elif card == "jail":
            print("Card:Go to jail")
            player.pos = 30
        elif card == "pall_mall":
            print("Card:Go to Pall Mall")
            player.pos = 31
        elif card == "repairs":
            print("Card:Your property is due for repair, pay $25 for each house and $100 for each hotel you own")
            #Fix me when houses are implemented
        elif card == "fine15":
            print("Card:You are caught speeding and fined $15")
            player.bal -= 15
        elif card == "collect150":
            print("Card:Your stock inflates and you collect $150")
            player.bal += 150
        elif card == "kingscross":
            print("Card:Go to King's Cross Station")
            player.pos = 25
            player.land(g.spaces)
        elif card == "go":
            print("Card:Advance to Go")
            player.pos = 20
            print("Advanced past GO, collected $200")
            player.bal += 200
        elif card == "collect50":
            print("It's your birthday! collect $50")
            player.bal += 50
        elif card == "mayfair":
            print("Card:Go to Mayfair")
            player.pos = 19
            player.land(g.spaces)
        elif card == "back3":
            print("Card:Move back 3 spaces")
            player.pos -= 3
            player.land(g.spaces)
        elif card == "GOOJF":
            print("Card:Recieve 1 get out of jail free card! Next time you go to jail you will immediately be released")
            player.GOOJF += 1
        elif card == "payall50":
            print("Card:You are elected as mayor, pay $50 to every player for their bribe")
            for other in g.players:
                if other != player:
                    other.bal+= 50
                    player.bal-= 50
        elif card == "collect25":
            print("Card:You win a beauty contest and recieve $25")
            player.bal+= 50
        elif card == "collect200":
            print("Bank error in your favour collect $200")
            player.bal+=200
        elif card == "collectall10":
            print("You take to petty crime and steal $10 from each player")
            for other in g.players:
                if other != player:
                    other.bal-=10
                    player.bal+= 10
        elif card == "collect100":
            print("Holiday fund matures, collect $100")
            player.bal+=100
        elif card == "pay50":
            print("Doctors fees, pay $50")
            player.bal-=50
        elif card == "pay100":
            print("You lose your wallet and lose $100")
            player.bal-=100
        g.update()
    def calc_rent(self):
        return self.prices[self.house_no]
                
spaces = []
spaces.append(space("Free Parking",False,None))
spaces.append(space("Strand",True,None,220,"Red",18,90,250,700,875,1050,110,150,150))
spaces.append(space("Chance",False,"chance"))
spaces.append(space("Fleet Street",True,None,220,"Red",18,90,250,700,875,1050,110,150,150))
spaces.append(space("Trafalgar Square",True,None,240,"Red",20,100,300,750,925,1100,120,150,150))
spaces.append(space("Fenchurch ST. Station",True,None,200,"Station"))
spaces.append(space("Leicester Square",True,None,260,"Yellow",22,110,330,800,975,1150,130,150,150))
spaces.append(space("Coventry Street",True,None,260,"Yellow",22,110,330,800,975,1150,130,150,150))
spaces.append(space("Water Works",True,None,150,"Utility"))
spaces.append(space("Piccadilly",True,None,280,"Yellow",24,120,360,850,1025,1200,140,150,150))
spaces.append(space("Go To Jail",False,"go to jail"))
spaces.append(space("Regent Street",True,None,300,"Green",26,130,390,900,1100,1275,150,200,200))
spaces.append(space("Oxford Street",True,None,300,"Green",26,130,390,900,1100,1275,150,200,200))
spaces.append(space("Community Chest",False,"community chest"))
spaces.append(space("Bond Street",True,None,320,"Green",28,150,450,1000,1200,1400,160,200,200))
spaces.append(space("Liverpool ST. Station",True,None,200,"Station"))
spaces.append(space("Chance",False,"chance"))
spaces.append(space("Park Lane",True,None,350,"Dark Blue",35,175,500,1100,1300,1500,175,200,200))
spaces.append(space("Super Tax",False,"tax100"))
spaces.append(space("Mayfair",True,None,400,"Dark Blue",50,200,600,1400,1700,2000,200,200,200))
spaces.append(space("Go",False,None))
spaces.append(space("Old Kent Road",True,None,60,"Brown",2,10,30,90,160,250,30,50,50))
spaces.append(space("Community Chest",False))
spaces.append(space("Whitechapel Road",True,None,60,"Brown",4,20,60,180,320,450,30,50,50))
spaces.append(space("Income Tax",False,"tax200"))
spaces.append(space("King's Cross Station",True,None,200,"Station"))
spaces.append(space("The Angel, Islington",True,None,100,"Light Blue",6,30,90,270,400,550,50,50,50))
spaces.append(space("Chance",False,"chance"))
spaces.append(space("Euston Road",True,None,100,"Light Blue",6,30,90,270,400,550))
spaces.append(space("Pentonville Road",True,None,120,"Light Blue",8,40,100,300,450,600))
spaces.append(space("Just Visiting Jail",False,None,0))
spaces.append(space("Pall Mall",True,None,140,"Pink",10,50,150,450,626,750,70,100,100))
spaces.append(space("Electric Company",True,None,100,"Utility"))
spaces.append(space("Whitehall",True,None,140,"Pink",10,50,150,450,625,750,70,100,100))
spaces.append(space("Northumberl'd Avenue",True,None,160,"Pink",12,60,180,500,700,900,80,100,100))
spaces.append(space("Marylybone Station",True,None,200,"Station"))
spaces.append(space("Bow Street",True,None,180,"Orange",14,70,200,550,750,950,90,100,100))
spaces.append(space("Community Chest",False,"community chest"))
spaces.append(space("Marlborough Street",True,None,180,"Orange",14,70,200,550,750,950,90,100,100))
spaces.append(space("Vine Street",True,None,200,"Orange",16,80,220,600,800,1000,100,100,100))
    
p1 = player("@")
p2 = player("x")
p3 = player("?")
p4 = player(">")

g=game(spaces,p1,p2,p3,p4)
g.update()
g.display()

for i in range(5):
    g.turn()






















#Make property info option that will format cards like this, numbers made up

"""
Pentonville Road
-Group:Light Blue
-Owned by @
 ――――――――――――
|            |
|――――――――――――
|  Rent:$26  |
|1house:$130 |
|2house:$390 |
|3house:$900 |
|4house:$1000|
|Hotel:$1275 |
 ――――――――――――
 -Mortgage value:100
 -House build price:100
 -Hotel build price:100
"""


