
#Importing Gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#Class MyWindow from Gtk.Window()
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        
        #Creating a horizontal box
            #Have 6pixels of space between children
            #It's added to the window
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        #Creating the button Hello
            #Adding its handler
            #Adding the button to the box   
        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        #
        self.box.pack_start(self.button1, True, True, 0)
        #Creating the button Goodbye
            #Adding its handler
            #Adding the button to the box   
        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        ##pack_start() sorts from left to right
        ##pack_end()   sorts from right to left
    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()