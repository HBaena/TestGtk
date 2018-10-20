    
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

##Definition of StackWindow from Gtk.Window
class StackWindow(Gtk.Window):

    def __init__(self):
        ##Definition with a title and a border of 10 pixels
        Gtk.Window.__init__(self, title="Stack Demo", border_width = 10)
        ##A Box (vertical) with space of 6 pixels between its children
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        ##Add the box to the window
        self.add(vbox)

        stack = Gtk.Stack()
        ##The best are 6 and 7, (12,13, )
        stack.set_transition_type(7)
        stack.set_transition_duration(1000)
        
        checkbutton = Gtk.CheckButton("Click me!")
        stack.add_titled(checkbutton, "check", "Check Button")
        
        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "A label")

        hbox   = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2 )
        label2 = Gtk.Label()
        label2.set_markup("<big>Number</big>")
        entry  = Gtk.Entry(max_length = 15) 
        button = Gtk.Button(label="Press")
        button.connect("clicked", self.on_button_clicked, entry, stack)
        hbox.pack_start(label2, True, True, 0)
        hbox.pack_start(entry , True, True, 0)
        hbox.pack_start(button , True, True, 0)
        stack.add_titled(hbox, "Box", "Set transition")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)

    def on_button_clicked(self, widget, entry, stack):
        try:
            print "Yes"
            stack.set_transition_type( int(entry.get_text()) )
        except:
            print "No"
            stack.set_transition_type(7)
        finally:
            stack.set_transition_duration(1000)            

win = StackWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()