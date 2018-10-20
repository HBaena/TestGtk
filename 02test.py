import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Usiing Gtk.Window class to create our MyWindow class
class MyWindow(Gtk.Window):
    #Constructor class
    def __init__(self):
        Gtk.Window.__init__(self, title="Window_main")
        #creatting a button from Gtk.Button class
        #With a label "Click Here"
        self.button = Gtk.Button(label="Click Here")
        #creating a listener to do something when the button is clicked
        self.button.connect("clicked", self.on_button_clicked)
        #Adding the button to the window
        self.add(self.button)
    #Creating the on_button_clicked listener
    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
