import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel,TabbedPanelHeader
#import button
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import  Scatter
import random
from kivy.uix.image import Image
from typing import Any,List
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import buildozer


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MyApp(App):
    """This is the root class and with the help of this call we are creating our personal widgets and
    some representation"""
    def build(self)->Any:
        kv_file = Builder.load_file("MyApp.kv")
        return kv_file

        """This function is use to initialize all the required widgets"""
        """
        t:Any=TabbedPanel()
        th:Any=TabbedPanelHeader(text="hii")
        box:Any=BoxLayout(orientation ='vertical')
        f:Any=FloatLayout()
        l:Any=Label(text="Welcome to my App")
        ti:Any=TextInput(text="Enter Your Name",multiline=False)
        b:Any=Button(text="Click")
        l1:Any=Label(text="default")
        s:Any=Scatter()

        box.add_widget(t)
        box.add_widget(f)
        f.add_widget(l)
        t.add_widget(th)
        #box.add_widget(ti)
        #f.add_widget(s)
        #s.add_widget(l)
        l.add_widget(b)
        """

        #ti.bind(text=l.setter("text"))

        #return box


    """
    def color(self,*args):
        This fuction is use to randomly set value of the Layout which is dependent on Text Input
        color:List=[1,1,0,1]
        color=[random.random() for i in range(3)]+[1]
    """






if __name__=="__main__":
    MyApp().run()

