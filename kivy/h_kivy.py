import random
from kivy.core.window import Window

from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from matplotlib.pyplot import text
# from kivy.uix.gridlayout import GridLayout

# from kivy.config import Config
# Config.set('graphics', 'width', '500')
# Config.set('graphics', 'height', '700')

Window.size = (300, 700)

red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]

class MyApp(App):
    def build(self):
        
        # label = Label(text='Hello world kivy', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        
        # img = Image(source='/home/usman/Desktop/image/Usman.jpg', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        
        layout = BoxLayout(padding=10)
        colors = [red,green,blue,purple]
        
        for i in range(5):
            btn = Button(text="Button %s" % (i+1), font_size='10sp', size_hint=(0.1, 0.05), background_color=random.choice(colors))
            btn.bind(on_press=self.callback)
            
            layout.add_widget(btn)
        return layout
    
    def callback(self, event):
        txt = ['Weldone my boss!','I greet you','Are you human','Who are you']
        print(random.choice(txt))
  
if __name__=='__main__':
    MyApp().run()
