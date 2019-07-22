from kivy.config import Config
Config.set('graphics','resizable',0)
import random, copy, json, sys, os
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooser
from kivy.app import App
from kivy.graphics import *
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import ObjectProperty

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

def dismiss_popup(self):
    self._popup.dismiss()

class ScreenManagement(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class ConwaysScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class MainMenuLayout(FloatLayout):
    pass

class SettingsLayout(FloatLayout):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self,root):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load ruleset", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self,root):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save ruleset as", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename,root):
        try:
            with open(os.path.join(path, filename[0])) as stream:
                self.text_input = json.load(stream)
            self.ids["Rule1"].text = str(self.text_input[0])
            self.ids["Rule2"].text = str(self.text_input[1])
            self.ids["Rule3"].text = str(self.text_input[2])
        except:
            print("An error occurred while loading file")
        self.dismiss_popup()
        self.update_rules(root)
        
    def save(self, path, filename,root):
        try:
            with open(os.path.join(path, filename), 'w+') as stream:
                stream.write("")
                json_string = json.dump(self.text_input,stream)
        except:
            print("An error occurred while saving")
        self.dismiss_popup()

    def update_rules(self,root):
        self.text_input = [self.ids["Rule1"].text.replace("]","").replace("[","").split(","),self.ids["Rule2"].text.replace("]","").replace("[","").split(","),self.ids["Rule3"].text.replace("]","").replace("[","").split(",")]
        try:
            for i in range(len(self.text_input)):
                self.text_input[i] = [int(e) for e in self.text_input[i]]
            root.ids["conways"].ids["conways"].rules = self.text_input
        except:
            pass

        
    def __init__(self, **kwargs):
        super(SettingsLayout, self).__init__(**kwargs)
        self.text_input = ""
        self.bg = [0,0,0,1]
    def update(self,label,slider,*args):
        if label == "red":
            self.bg[0] = int(args[1])/255
        if label == "green":
            self.bg[1] = int(args[1])/255
        if label == "blue":
            self.bg[2] = int(args[1])/255
        with self.ids["live_color"].canvas.before:
            self.col = Color(self.bg[0], self.bg[1], self.bg[2], self.bg[3])
            Rectangle(pos = (535,80),size_hint = self.size_hint)
        self.ids[label].text = str(int(args[1]))
    def apply_color(self,root):
        root.ids["conways"].ids["conways"].mywidge.alivecol = self.bg
        with self.ids["current_color"].canvas.before:
            self.col = Color(self.bg[0], self.bg[1], self.bg[2], self.bg[3])
            Rectangle(pos = (425,80),size_hint = self.size_hint)
    def default(self,root):
        root.ids["conways"].ids["conways"].mywidge.alivecol = [122/255,207/255,214/255,1]
        with self.ids["current_color"].canvas.before:
            self.col = Color(122/255,207/255,214/255,1)
            Rectangle(pos = (425,80),size_hint = self.size_hint)
        

class ConwaysLayout(BoxLayout):
    def __init__(self, **kwargs):
        with open("assets/RuleSets/conways.rs","w+") as f:
            data = [[0,1,4,5,6,7,8],[2,3],[3]]
            f.write("")
            json_string = json.dump(data,f)
        with open("assets/RuleSets/conways.rs","r") as f:
            self.rules = json.load(f)#[[0,1,4,5,6,7,8],[2,3],[3]] Alive->Dead,Alive->Alive,Dead->Alive
        super(ConwaysLayout, self).__init__(**kwargs)
        Clock.schedule_once(self._finish_init)
    def _finish_init(self, dt):
        self.active = False
        Clock.schedule_interval(self.tick, 1/10)
        
    def random(self):
        grid = App.get_running_app().grid
        size = App.get_running_app().size
        for x in range(size):
            for y in range(size):
                grid[x][y] = random.randrange(2)
        self.mywidge.update_canvas()
    def clear(self):
        grid = App.get_running_app().grid
        size = App.get_running_app().size
        for x in range(size):
            for y in range(size):
                grid[x][y]=0
        self.mywidge.update_canvas()
    def play_pause(self,button):
        self.active = not self.active
        if button.text == "Play":
            button.text = "Pause"
        else:
            button.text = "Play"
    def tick(self,dt):
        if self.active:
            grid = App.get_running_app().grid
            size = App.get_running_app().size
            neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            new_grid = []
            for i in range(size):
                new_grid.append([0]*size)
            for x in range(size):
                for y in range(size):
                    total = 0
                    for neighbour in neighbours:
                        if x+neighbour[0] >= 0 and y+neighbour[1] >= 0 and x+neighbour[0] <= size-1 and y+neighbour[1] <= size-1:
                            total += grid[x+neighbour[0]][y+neighbour[1]]
                    #RULES#
                    if grid[x][y] == 1 and total in self.rules[0]:
                        new_grid[x][y]  = 0
                    elif grid[x][y] == 1 and total in self.rules[1]:
                        new_grid[x][y] = 1
                    elif grid[x][y] == 0 and total in self.rules[2]:
                        new_grid[x][y] = 1
                    else:
                        new_grid[x][y] = grid[x][y]
            App.get_running_app().grid  = copy.deepcopy(new_grid)
        self.mywidge.update_canvas()
                    
    
class CircleDrawer(Widget):
    def __init__(self, **kwargs):
        super(CircleDrawer, self).__init__(**kwargs)
        self.alivecol = [122/255,207/255,214/255,1]
        self.deadcol = [0.5,0.5,0.5,0.5]
    def on_touch_down(self,touch):
        size = App.get_running_app().size
        grid = App.get_running_app().grid
        x  = int(touch.pos[0]//(self.width/size))
        y  = int(touch.pos[1]//(self.height/size))
        if App.get_running_app().grid[x][y] == 1:
            App.get_running_app().grid[x][y] = 0
        else:
            App.get_running_app().grid[x][y] = 1
        self.update_canvas()
    def on_touch_move(self,touch):
        try:
            size = App.get_running_app().size
            grid = App.get_running_app().grid
            x  = int(touch.pos[0]//(self.width/size))
            y  = int(touch.pos[1]//(self.height/size))
            if App.get_running_app().grid[x][y] == 0:
                App.get_running_app().grid[x][y] = 1
            self.update_canvas()
        except:
            pass
    def update_canvas(self):
        grid = App.get_running_app().grid
        size = App.get_running_app().size
        cellheight = self.height//size
        cellwidth  = cellheight
        self.canvas.clear()
        with self.canvas:
            for x in range(size):
                for y in range(size):
                    if grid[x][y] == 0:
                        Color(self.deadcol[0],self.deadcol[1],self.deadcol[2],self.deadcol[3])
                    else:
                        Color(self.alivecol[0],self.alivecol[1],self.alivecol[2],self.alivecol[3])
                    Ellipse(pos=((x)*cellheight,(y)*cellwidth),size = (cellwidth,cellheight))

class ConwaysGameOfLife(App):
    
    def build(self):
        self.sM = ScreenManagement()
        
        self.size = 30
        self.grid = []
        for i in range(self.size):
            self.grid.append([0]*self.size)
        #Make the grid and set the amount of X by X circles to be in the grid  
        
        return presentation


presentation = Builder.load_file("assets/pres.kv")
ConwaysGameOfLife().run()










































