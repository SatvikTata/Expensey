import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class myGridLayout(GridLayout):
    def __init__(self, **kwargs):
        #calling gridlayout constructor
        super(myGridLayout,self).__init__(**kwargs)

        #setting the number of columns
        self.cols=1
        

        #creating a expense button
        self.create_expense=Button(text='Create an Expense',font_size=20)

        #binding the button
        self.create_expense.bind(on_press=self.pressed_create_exp)
        self.add_widget(self.create_expense)

        #creating a tracking button
        self.track_expense=Button(text='Track your Expense',font_size=20)
        self.track_expense.bind(on_press=self.pressed_track_exp)
        self.add_widget(self.track_expense)

    def pressed_create_exp(self,instance):
        self.add_widget(Label(text='Creating an Expense'))

    def pressed_track_exp(self,instance):
        self.add_widget(Label(text='Tracking you Expense'))


class ExpenseyApp(App):
    def build(self):
        return myGridLayout()
    

ExpenseyApp().run()