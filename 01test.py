#Importing of Gtk modules
import gi
#Asking for the version 3.0
gi.require_version('Gtk', '3.0')
#Importing Gtk
from gi.repository import Gtk

#Creating an empty window
win = Gtk.Window()
#Ensuring that the application is gonna finish with a click in close button
win.connect("destroy", Gtk.main_quit)
#Displaying the window
win.show_all()
#starting the GTK+ processing loop which we quit when the window is closed.
Gtk.main()
