import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class myGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # calling gridlayout constructor
        super(myGridLayout,self).__init__(**kwargs)

        # setting the number of columns
        self.cols=2
        
        # adding widgets
        self.add_widget(Label(text='Name:'))

        # adding the inputBox
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)

        # creating a submit button
        self.submit=Button(text='Submit',font_size=20)

        #binding the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name=self.name.text
        print(name)


class ExpenseyApp(App):
    def build(self):
        return myGridLayout()
    

ExpenseyApp().run()