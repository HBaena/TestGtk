import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RadioButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="RadioButton Demo")
        self.set_border_width(10)
        self.vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        hbox = Gtk.Box(spacing=6)
        label = Gtk.Label()
        label.set_markup("<big>Select a page</big>")
        self.vbox.pack_start(label, 1, 1, 0)
        self.vbox.pack_start(hbox, True, True, 0)
        self.add(self.vbox)
        
        button1 = Gtk.RadioButton.new_with_label_from_widget(None, "Facebook")
        button1.connect("toggled", self.on_button_toggled, "https://www.facebook.com")
        hbox.pack_start(button1, False, False, 0)
        button2 = Gtk.RadioButton.new_from_widget(button1)
        button2.set_label("Google")
        button2.connect("toggled", self.on_button_toggled, "https://www.google.com")
        hbox.pack_start(button2, False, False, 0)

        button3 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1,
            "YouTube")
        button3.connect("toggled", self.on_button_toggled, "https://www.youtube.com")
        hbox.pack_start(button3, False, False, 0)



        self.link = Gtk.LinkButton("http://www.facebook.org", "Go to the site!")
        self.vbox.pack_start(self.link, True, True, 0)

        self.vbox.show_all()

    def on_button_toggled(self, button, name):
        if button.get_active():
            self.link.set_uri(name)
            self.show_all()
    
#print dir(Gtk.LinkButton.props)
win = RadioButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()