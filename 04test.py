import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def on_window_main_destroy(self, *args):
        Gtk.main_quit()

    def on_button_pressed(self, button):
        label = button.get_property("label")
        if label == "print": 
            print "Hello"
        elif label == "exit"  :
            Gtk.main_quit()
        elif label == "window":
            win = Gtk.Window()
            win.connect("destroy", Gtk.main_quit)
            win.show_all()
            Gtk.main()

#Builder from Gtk
builder = Gtk.Builder()
#Creating a window from a file
builder.add_from_file("ui/test.glade")
#Adding the handlers
builder.connect_signals(Handler())
#Adding "all window" to a window
window = builder.get_object("window_main")
#Showing the window
window.show_all()
#Starting Gtk process loop
Gtk.main()

