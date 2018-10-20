import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from classes import GenericWindow

class MyWindow(GenericWindow):
    """docstring for MyWindow"""
    def __init__(self, *arg):
        GenericWindow.__init__(self, arg[0])
        #Creatting and adding a grid (table)        
        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")
        ##grid_widget.attach(#1,#2,#3,#4,#5)
            #1   child (widget to add)
            #2   Number of columns on the left of child
            #3   Number's row             
            #4#5 Width and height (number of rows)
        ##grid_widget.attach_nex_to(#1,#2,#3,#4,#5)
            #1   child (widget to add)
            #2   sibling
            #3   position             
            #4#5 Width and height (number of rows)
        #Firts add
        grid.attach(button1, 0, 1, 2, 1)
        grid.attach(button2, 0, 2, 2, 1)
        grid.attach_next_to(button3, button2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(button5, 1, 4, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.LEFT, 1, 1)
        
window = MyWindow("Title")
window.show_all()
Gtk.main()