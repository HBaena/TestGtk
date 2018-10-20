
#widget is an istance of a widget
#event is the event that We want.   
    #fo example click, onFocus, etc
#callback is the name of our callback function
    #That is the function which it's gonna be running after the 
    #interaction with the widget
#data are the parameter which should be passed when the signal is issued
#handler_id is a particular number that identifies this particular signal-callback              

##handler_id = widget.connect("event", callback, data)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


#label declaration
##label = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)
#The same
label = Gtk.Label()
label.set_label("Hello World")
label.set_angle(25)
label.set_halign(Gtk.Align.END)

#Setter and getter
##widget.get_property("prop-name") 
##widget.set_property("prop-name", value).

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

